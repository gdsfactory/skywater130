"""Utilities for multi-layer routing using doroutes A* pathfinding."""

from functools import partial
from typing import Iterable, List, Tuple

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import LayerSpec, Port
import numpy as np

#from doroutes import find_route_astar
from sky130.pcells.vias import via_m1_m2


# Layer definitions for Sky130
LAYER_M1 = (68, 20)  # Metal 1 - Horizontal
LAYER_M2 = (69, 20)  # Metal 2 - Vertical


def _make_manhattan(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Convert a list of points to a proper Manhattan path.

    If consecutive points are not aligned (share neither x nor y),
    insert an intermediate jog point to make it Manhattan.
    Horizontal first (M1), then vertical (M2).
    """
    if len(points) < 2:
        return points

    result = [points[0]]

    for i in range(1, len(points)):
        p_prev = result[-1]
        p_curr = points[i]

        dx = abs(p_curr[0] - p_prev[0])
        dy = abs(p_curr[1] - p_prev[1])

        # Check if already aligned (Manhattan)
        if dx < 0.001 or dy < 0.001:
            result.append(p_curr)
        else:
            # Not aligned - insert a jog point (horizontal first)
            jog_point = (p_curr[0], p_prev[1])
            result.append(jog_point)
            result.append(p_curr)

    return result


def _is_horizontal(p1: Tuple[float, float], p2: Tuple[float, float]) -> bool:
    """Check if a segment between two points is horizontal."""
    return abs(p2[1] - p1[1]) < 0.001


def _straight_metal1(
    length: float,
    width: float,
) -> gf.Component:
    """Create a straight Metal 1 segment as a rectangle."""
    c = gf.Component()
    c.add_ref(gf.components.rectangle(size=(length, width), layer=LAYER_M1))
    return c


def _straight_metal2(
    length: float,
    width: float,
) -> gf.Component:
    """Create a straight Metal 2 segment as a rectangle."""
    c = gf.Component()
    c.add_ref(gf.components.rectangle(size=(width, length), layer=LAYER_M2))
    return c

def _calc_path_length(path: List[Tuple[float, float]]) -> float:
    """Calculate total Manhattan length of a path."""
    if len(path) < 2:
        return 0.0
    total = 0.0
    for i in range(len(path) - 1):
        dx = abs(path[i + 1][0] - path[i][0])
        dy = abs(path[i + 1][1] - path[i][1])
        total += dx + dy
    return total


def _is_valid_manhattan_path(path: List[Tuple[float, float]]) -> bool:
    """Check if path is valid Manhattan (no consecutive same-direction segments).
    
    A valid Manhattan path alternates between horizontal and vertical segments.
    Invalid examples:
    - Up then Up (two vertical segments in a row)
    - Left then Right (two horizontal segments in a row)
    """
    if len(path) < 3:
        return True  # Less than 3 points can't have backtracking
    
    tolerance = 0.001
    
    for i in range(len(path) - 2):
        p1, p2, p3 = path[i], path[i + 1], path[i + 2]
        
        # Determine direction of each segment
        seg1_horiz = abs(p2[1] - p1[1]) < tolerance  # Horizontal if Y doesn't change
        seg1_vert = abs(p2[0] - p1[0]) < tolerance   # Vertical if X doesn't change
        seg2_horiz = abs(p3[1] - p2[1]) < tolerance
        seg2_vert = abs(p3[0] - p2[0]) < tolerance
        
        # Invalid if two consecutive segments are both horizontal or both vertical
        if seg1_horiz and seg2_horiz:
            return False  # Two horizontal segments in a row
        if seg1_vert and seg2_vert:
            return False  # Two vertical segments in a row
    
    return True


def _simplify_path(corners: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Remove redundant corners that don't change direction.
    
    This post-processing step removes unnecessary intermediate points
    where the path continues in the same direction.
    Also removes duplicate consecutive points.
    """
    if not corners:
        return []
    
    # First pass: remove consecutive duplicates
    unique_corners = [corners[0]]
    for i in range(1, len(corners)):
        curr = corners[i]
        prev = unique_corners[-1]
        # Only keep if distance > tolerance
        if abs(curr[0] - prev[0]) > 0.001 or abs(curr[1] - prev[1]) > 0.001:
            unique_corners.append(curr)
            
    if len(unique_corners) < 3:
        return unique_corners
    
    # Second pass: remove collinear points
    result = [unique_corners[0]]
    for i in range(1, len(unique_corners) - 1):
        prev = unique_corners[i - 1]
        curr = unique_corners[i]
        next_pt = unique_corners[i + 1]
        
        # Calculate direction vectors
        dx1 = curr[0] - prev[0]
        dy1 = curr[1] - prev[1]
        dx2 = next_pt[0] - curr[0]
        dy2 = next_pt[1] - curr[1]
        
        # Normalize to direction only (sign matters, not magnitude)
        dir1 = (1 if dx1 > 0.001 else (-1 if dx1 < -0.001 else 0),
                1 if dy1 > 0.001 else (-1 if dy1 < -0.001 else 0))
        dir2 = (1 if dx2 > 0.001 else (-1 if dx2 < -0.001 else 0),
                1 if dy2 > 0.001 else (-1 if dy2 < -0.001 else 0))
        
        # Keep point only if direction changes
        if dir1 != dir2:
            result.append(curr)
    
    result.append(unique_corners[-1])
    return result


def _run_astar_rectilinear(
    polys: List,
    start_pos: Tuple[int, int, str],
    stop_pos: Tuple[int, int, str],
    bbox_tuple: Tuple[int, int, int, int],
    grid_unit_dbu: int,
    straight_width: int,
    bend_radius: int,
) -> List[Tuple[int, int]]:
    """Low-level A* rectilinear routing call.
    
    Returns list of corner points in DBU, or None if no route found.
    """
    from doroutes import doroutes as _doroutes
    
    # Build rectilinear bend pattern
    rectilinear_bend = [(i, 0) for i in range(1, bend_radius + 1)] + \
                      [(bend_radius, i) for i in range(1, bend_radius + 1)]
    
    try:
        print(straight_width)
        print(grid_unit_dbu)
        #input("debugging...")
        corners = _doroutes.show(
            polys=polys,
            start=start_pos,
            stop=stop_pos,
            bbox=bbox_tuple,
            grid_unit=grid_unit_dbu,
            straight_width=straight_width,
            discretized_bend_east_to_north=rectilinear_bend,
        )
        return corners
    except Exception as e:
        print(f"A* failed: {e}")
        return None


def _extract_polys_for_layers(
    kc, 
    layers: List[Tuple[int, int]], 
    dbu: float,
    port_points: List[Tuple[int, int]] = None,
):
    """Extract obstruction polygons from specified layers.
    
    Args:
        kc: KCell to extract polygons from.
        layers: List of (layer, datatype) tuples to extract.
        dbu: Database unit.
        port_points: Optional list of (x_dbu, y_dbu) port positions.
                    ONLY polygons containing these exact points are excluded.
                    All other polygons are hard obstructions - router must go around.
    
    Returns:
        List of polygon point arrays.
    """
    from kfactory import kdb
    import numpy as np
    
    # Collect all obstruction polygons
    all_polys = []
    for layer in layers:
        layer_idx = kc.kcl.layer(*layer)
        r = kdb.Region(kc.begin_shapes_rec(layer_idx))
        for poly in r.each():
            all_polys.append(poly)
    
    # Find and exclude ONLY polygons that contain port points
    excluded_indices = set()
    if port_points:
        for px, py in port_points:
            port_point = kdb.Point(px, py)
            for i, poly in enumerate(all_polys):
                if poly.inside(port_point):
                    excluded_indices.add(i)
                    break  # Only exclude ONE polygon per port
    
    # Convert remaining polygons to numpy arrays - these are ALL hard obstructions
    polys = []
    for i, poly in enumerate(all_polys):
        if i not in excluded_indices:
            pts = np.array([(p.x, p.y) for p in poly.each_point_hull()], dtype=np.int64)
            if len(pts) >= 3:
                polys.append(pts)
    
    return polys


def _get_pos_with_dir(port, dbu: float) -> Tuple[int, int, str]:
    """Convert port to (x_dbu, y_dbu, direction) tuple."""
    x, y = int(port.dcenter[0] / dbu), int(port.dcenter[1] / dbu)
    angle = port.orientation
    if angle is None:
        d = "o"
    elif abs(angle) < 1:
        d = "e"
    elif abs(angle - 90) < 1:
        d = "n"
    elif abs(angle - 180) < 1 or abs(angle + 180) < 1:
        d = "w"
    elif abs(angle - 270) < 1 or abs(angle + 90) < 1:
        d = "s"
    else:
        d = "o"
    return (x, y, d)


def route_hierarchical_astar(
    c: Component,
    start: Port,
    stop: Port,
    global_grid_unit: float = 2.0,  # Coarse grid for global routing
    detail_grid_unit: float = 0.25,  # Fine grid for detailed routing
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    detail_margin: float = 5.0,  # Margin around corners for detail routing (um)
) -> List[Tuple[float, float]]:
    """Hierarchical two-phase routing: global then detailed.
    
    Phase 1 (Global): Uses coarse grid to find general path quickly.
    Phase 2 (Detailed): Refines path segments near obstacles with fine grid.
    
    Args:
        c: Component to route in.
        start: Start port.
        stop: Stop port.
        global_grid_unit: Grid unit for global routing (um). Larger = faster.
        detail_grid_unit: Grid unit for detailed routing (um). Smaller = more accurate.
        width: Wire width (um).
        layers_to_avoid: Layers containing obstructions (polygons containing ports are auto-excluded).
        detail_margin: Margin around path for detailed routing refinement (um).
        
    Returns:
        List of corner points in um, or None if no route found.
    """
    if layers_to_avoid is None:
        layers_to_avoid = []
    
    dbu = c.kcl.dbu
    kc = c.kcl.kcells[c.name]
    
    # Validate layers
    _layers = [layer if isinstance(layer, tuple) else (layer, 0) for layer in layers_to_avoid]
    
    # Get port positions first (needed for polygon exclusion)
    start_pos = _get_pos_with_dir(start, dbu)
    stop_pos = _get_pos_with_dir(stop, dbu)
    
    # Port points for polygon exclusion - find and exclude the polygon containing each port
    port_points = [
        (start_pos[0], start_pos[1]),
        (stop_pos[0], stop_pos[1]),
    ]
    
    # Extract obstruction polygons, excluding polygons that contain ports
    polys = _extract_polys_for_layers(kc, _layers, dbu, port_points)
    
    # Invert stop orientation (port faces inward, we approach from opposite direction)
    stop_dir_map = {"n": "s", "s": "n", "e": "w", "w": "e", "o": "o"}
    stop_pos = (stop_pos[0], stop_pos[1], stop_dir_map[stop_pos[2]])
    
    # Calculate bounding box
    start_x, start_y = start_pos[0], start_pos[1]
    stop_x, stop_y = stop_pos[0], stop_pos[1]
    dist = max(abs(stop_x - start_x), abs(stop_y - start_y))
    padding = int(dist * 0.5)  # 50% margin for global routing
    
    comp_bbox = kc.bbox()
    min_x = min(start_x, stop_x, comp_bbox.left) - padding
    max_x = max(start_x, stop_x, comp_bbox.right) + padding
    min_y = min(start_y, stop_y, comp_bbox.bottom) - padding
    max_y = max(start_y, stop_y, comp_bbox.top) + padding
    
    bbox_tuple = (max_y, max_x, min_y, min_x)
    
    # ========== PHASE 1: GLOBAL ROUTING ==========
    print(f"[GLOBAL] Routing with grid_unit={global_grid_unit}um...")
    
    global_grid_dbu = int(global_grid_unit / dbu)
    width_dbu = int(width / dbu)
    global_straight_width = max(1, width_dbu // global_grid_dbu + 1)
    global_straight_width += (global_straight_width + 1) % 2
    global_bend_radius = max(1, (width_dbu + global_grid_dbu - 1) // global_grid_dbu)
    
    # Try with exact orientations first
    global_corners = _run_astar_rectilinear(
        polys=polys,
        start_pos=start_pos,
        stop_pos=stop_pos,
        bbox_tuple=bbox_tuple,
        grid_unit_dbu=global_grid_dbu,
        straight_width=global_straight_width,
        bend_radius=global_bend_radius,
    )
    
    # Fallback to omnidirectional if failed
    if global_corners is None:
        print("[GLOBAL] Retrying with relaxed orientations...")
        start_relaxed = (start_pos[0], start_pos[1], "o")
        stop_relaxed = (stop_pos[0], stop_pos[1], "o")
        global_corners = _run_astar_rectilinear(
            polys=polys,
            start_pos=start_relaxed,
            stop_pos=stop_relaxed,
            bbox_tuple=bbox_tuple,
            grid_unit_dbu=global_grid_dbu,
            straight_width=global_straight_width,
            bend_radius=global_bend_radius,
        )
    
    # Check for no route found (None or empty list)
    if not global_corners or len(global_corners) < 2:
        print("[GLOBAL] No route found!")
        return None
    
    print(f"[GLOBAL] Found path with {len(global_corners)} corners")
    
    # Convert to um
    global_path_um = [(p[0] * dbu, p[1] * dbu) for p in global_corners]
    
    # If no obstructions or detail not needed, return global path
    if not polys or detail_grid_unit >= global_grid_unit:
        print("[DETAIL] Skipping (no obstructions or detail not finer than global)")
        return global_path_um
    
    # ========== PHASE 2: DETAILED ROUTING ==========
    print(f"[DETAIL] Refining with grid_unit={detail_grid_unit}um...")
    
    detail_grid_dbu = int(detail_grid_unit / dbu)
    detail_straight_width = max(width, width_dbu // detail_grid_dbu + 1)
    detail_straight_width += (detail_straight_width + 1) % 2
    detail_bend_radius = max(1, (width_dbu + detail_grid_dbu - 1) // detail_grid_dbu)
    margin_dbu = int(detail_margin / dbu)
    
    # Refine each segment of the global path
    refined_path = [global_corners[0]]
    
    for i in range(len(global_corners) - 1):
        seg_start = global_corners[i]
        seg_end = global_corners[i + 1]
        
        # Create tight bounding box around this segment
        seg_min_x = min(seg_start[0], seg_end[0]) - margin_dbu
        seg_max_x = max(seg_start[0], seg_end[0]) + margin_dbu
        seg_min_y = min(seg_start[1], seg_end[1]) - margin_dbu
        seg_max_y = max(seg_start[1], seg_end[1]) + margin_dbu
        seg_bbox = (seg_max_y, seg_max_x, seg_min_y, seg_min_x)
        
        # Determine segment directions
        dx = seg_end[0] - seg_start[0]
        dy = seg_end[1] - seg_start[1]
        
        if abs(dx) > abs(dy):  # Horizontal segment
            start_dir = "e" if dx > 0 else "w"
            end_dir = "w" if dx > 0 else "e"
        else:  # Vertical segment
            start_dir = "n" if dy > 0 else "s"
            end_dir = "s" if dy > 0 else "n"
        
        seg_start_pos = (seg_start[0], seg_start[1], start_dir)
        seg_end_pos = (seg_end[0], seg_end[1], end_dir)
        
        # Try detailed routing for this segment
        print("detailed...")
        detail_corners = _run_astar_rectilinear(
            polys=polys,
            start_pos=seg_start_pos,
            stop_pos=seg_end_pos,
            bbox_tuple=seg_bbox,
            grid_unit_dbu=detail_grid_dbu,
            straight_width=detail_straight_width,
            bend_radius=detail_bend_radius,
        )
        detail_corners = None
        
        if detail_corners and len(detail_corners) > 1:
            # Add detailed path (skip first point as it's same as last added)
            refined_path.extend(detail_corners[1:])
        else:
            # Keep original segment if detail routing fails
            refined_path.append(seg_end)
    
    print(f"[DETAIL] Refined path has {len(refined_path)} corners")
    
    # Convert to um
    refined_path_um = [(p[0] * dbu, p[1] * dbu) for p in refined_path]
    return refined_path_um




# Minimum segment length to draw (skip segments shorter than this)
MIN_SEGMENT_LENGTH = 0.01  # 10nm minimum


def _draw_route_segments(
    c: Component,
    points_um: List[Tuple[float, float]],
    width: float,
    add_segment_ports: bool = False,
    port_name_prefix: str = "seg",
    horizontal_layer: tuple = LAYER_M1,
    vertical_layer: tuple = LAYER_M2,
    add_vias: bool = True,
) -> List[Port]:
    """Draw metal segments and vias for a route path.
    
    Args:
        c: Component to add segments to.
        points_um: List of corner points in um.
        width: Wire width in um.
        add_segment_ports: If True, add a port to each straight segment.
        port_name_prefix: Prefix for port names (default: "seg").
        horizontal_layer: Layer tuple for horizontal segments.
        vertical_layer: Layer tuple for vertical segments.
        add_vias: If True, add vias at corners between horizontal and vertical segments.
    
    Returns:
        List of ports added to segments (empty if add_segment_ports=False).
    """
    segment_ports = []
    
    # If single-layer routing (checking if layers are same), add corner patches
    if horizontal_layer == vertical_layer:
        for p in points_um:
            patch = c.add_ref(gf.components.rectangle(size=(width, width), layer=horizontal_layer))
            patch.dcenter = p

    if len(points_um) < 2:
        return segment_ports
    
    for i in range(len(points_um) - 1):
        p_curr = points_um[i]
        p_next = points_um[i + 1]
        
        # Skip segments where points are too close together
        dx = abs(p_next[0] - p_curr[0])
        dy = abs(p_next[1] - p_curr[1])
        if dx < MIN_SEGMENT_LENGTH and dy < MIN_SEGMENT_LENGTH:
            continue  # Skip this zero-length segment entirely

        horiz = _is_horizontal(p_curr, p_next)

        if horiz:
            # Horizontal segment
            x_min = min(p_curr[0], p_next[0])
            x_max = max(p_curr[0], p_next[0])
            length = x_max - x_min
            y = p_curr[1]

            if length >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(length, width), layer=horizontal_layer)
                )
                rect.dmove((x_min, y - width / 2))
                
                # Add port at segment center if requested
                if add_segment_ports:
                    port_center = (x_min + length / 2, y)
                    port_name = f"{port_name_prefix}"
                    port = c.add_port(
                        name=port_name,
                        center=port_center,
                        width=0.01,
                        orientation=0,  # Horizontal segment
                        layer=(horizontal_layer[0], 16),
                        port_type="electrical"
                    )
                    segment_ports.append(port)
                    c.draw_ports()
        else:
            # Vertical segment
            y_min = min(p_curr[1], p_next[1])
            y_max = max(p_curr[1], p_next[1])
            length = y_max - y_min
            x = p_curr[0]

            if length >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(width, length), layer=vertical_layer)
                )
                rect.dmove((x - width / 2, y_min))
                
                # Add port at segment center if requested
                if add_segment_ports:
                    port_center = (x, y_min + length / 2)
                    port_name = f"{port_name_prefix}"
                    port = c.add_port(
                        name=port_name,
                        center=port_center,
                        width=0.01,
                        orientation=90,  # Vertical segment
                        layer=(vertical_layer[0], 16),
                        port_type="electrical"
                    )
                    segment_ports.append(port)
                    c.draw_ports()

        # Place via at each corner (intermediate points only)
        if add_vias and i < len(points_um) - 2:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = p_next
    
    return segment_ports


def route_hierarchical(
    c: Component,
    start: Port,
    stop: Port,
    global_grid_unit: float = 2.0,
    detail_grid_unit: float = 0.25,
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    detail_margin: float = 5.0,
    add_segment_ports: bool = False,
    port_name_prefix: str = "seg",
) -> List[Port]:
    """Route using hierarchical two-phase approach: global then detailed.
    
    This is the recommended routing function for designs with:
    - Large distances (>10um) between ports
    - Small features (<1um) that need to be avoided
    
    Phase 1 (Global): Uses coarse 2um grid to find general path quickly.
    Phase 2 (Detailed): Refines path with fine 0.25um grid near obstacles.
    
    Polygons containing the start/end ports are automatically excluded from
    obstructions, allowing the router to connect to ports on device metal.
    
    If routing fails on the primary layer (e.g. blocked by device metal),
    the router attempts a "via-escape" strategy: placing vias at the start/end
    ports and routing on the layer above (e.g. M2) which is often less congested.
    
    Args:
        c: Component to add the route to.
        start: Start port.
        stop: Stop port.
        global_grid_unit: Grid unit for global routing (um). Default 2.0.
        detail_grid_unit: Grid unit for detailed routing (um). Default 0.25.
        width: Width of the metal traces (um).
        layers_to_avoid: Layers containing obstructions.
        detail_margin: Margin around path for detailed routing (um).
        add_segment_ports: If True, add a port to each straight segment.
        port_name_prefix: Prefix for port names (default: "seg").
    
    Returns:
        List of ports added to segments (empty if add_segment_ports=False or routing fails).
    """
    # Get the hierarchical path
    path = route_hierarchical_astar(
        c=c,
        start=start,
        stop=stop,
        global_grid_unit=global_grid_unit,
        detail_grid_unit=detail_grid_unit,
        width=width,
        layers_to_avoid=layers_to_avoid,
        detail_margin=detail_margin,
    )
    
    # If M1 routing failed, try via-escape strategy: route on M2
    if path is None:
        print("[VIA-ESCAPE] M1 routing blocked - trying Escape via BBox Top...")
        
        # Calculate escape Y coordinate based on actual obstructions
        # This ensures we route Horizontal segments (M1) in clear space
        
        # Extract all obstruction polygons (M1, M2, etc.) to find the max Y
        # This is more robust than component bbox which might be stale or incomplete
        # Extract obstruction polygons (M1, M2, etc.) to find the max Y
        # This is more robust than component bbox which might be stale or incomplete
        obstruction_polys = _extract_polys_for_layers(
            c.kcl.kcells[c.name],
            layers_to_avoid or [],
            c.kcl.dbu,
            None  # No port exclusion needed for obtaining global max Y
        )
        # Separate M2 polygons for M2-specific path checking
        m2_polys = _extract_polys_for_layers(
            c.kcl.kcells[c.name],
            [LAYER_M2],
            c.kcl.dbu,
            None
        )
        
        # Initialize flag for M2 horizontal routing
        use_m2_horiz = False
        
        # Check if ports are vertically aligned (same X within tolerance)
        x_tolerance = 0.01  # 10nm tolerance
        y_tolerance = 0.01
        ports_vertically_aligned = abs(start.dcenter[0] - stop.dcenter[0]) < x_tolerance
        ports_horizontally_aligned = abs(start.dcenter[1] - stop.dcenter[1]) < y_tolerance
        
        dbu = c.kcl.dbu
        clearance = detail_margin  # Clearance in um
        
        # Get port positions
        start_x, start_y = start.dcenter[0], start.dcenter[1]
        stop_x, stop_y = stop.dcenter[0], stop.dcenter[1]
        
        # Helper function to check if a point is inside a polygon bbox
        def point_in_poly_bbox(px, py, poly):
            """Check if a point is inside a polygon's bounding box."""
            if len(poly) < 3:
                return False
            poly_x_min, poly_x_max = poly[:, 0].min() * dbu, poly[:, 0].max() * dbu
            poly_y_min, poly_y_max = poly[:, 1].min() * dbu, poly[:, 1].max() * dbu
            return poly_x_min <= px <= poly_x_max and poly_y_min <= py <= poly_y_max
        
        # Helper function to check if a path segment is blocked by any obstruction
        def segment_blocked(p1, p2, polys, excluded_points=None, margin_um=0.1):
            """Check if a segment from p1 to p2 is blocked by any polygon.
            
            Args:
                excluded_points: List of (x, y) points. Polygons containing these points
                                are excluded from blocking check (for ports on device metal).
            """
            x1, y1 = p1[0], p1[1]  # Already in um
            x2, y2 = p2[0], p2[1]
            
            # Determine if segment is horizontal or vertical
            is_horizontal = abs(y2 - y1) < 0.001
            is_vertical = abs(x2 - x1) < 0.001
            
            for poly in polys:
                if len(poly) < 3:
                    continue
                    
                # Skip polygons that contain any of the excluded points (port locations)
                if excluded_points:
                    skip_poly = False
                    for ex, ey in excluded_points:
                        if point_in_poly_bbox(ex, ey, poly):
                            skip_poly = True
                            break
                    if skip_poly:
                        continue
                
                # Polygon bounds in um
                poly_x_min, poly_x_max = poly[:, 0].min() * dbu, poly[:, 0].max() * dbu
                poly_y_min, poly_y_max = poly[:, 1].min() * dbu, poly[:, 1].max() * dbu
                
                if is_horizontal:
                    # Horizontal segment at y = y1, from x1 to x2
                    seg_x_min, seg_x_max = min(x1, x2), max(x1, x2)
                    seg_y = y1
                    if (poly_y_min - margin_um <= seg_y <= poly_y_max + margin_um and
                        seg_x_min < poly_x_max and seg_x_max > poly_x_min):
                        return True
                        
                elif is_vertical:
                    # Vertical segment at x = x1, from y1 to y2
                    seg_y_min, seg_y_max = min(y1, y2), max(y1, y2)
                    seg_x = x1
                    if (poly_x_min - margin_um <= seg_x <= poly_x_max + margin_um and
                        seg_y_min < poly_y_max and seg_y_max > poly_y_min):
                        return True
                else:
                    # Non-Manhattan segment - use simple bbox overlap
                    seg_x_min, seg_x_max = min(x1, x2), max(x1, x2)
                    seg_y_min, seg_y_max = min(y1, y2), max(y1, y2)
                    if (seg_x_min <= poly_x_max and seg_x_max >= poly_x_min and
                        seg_y_min <= poly_y_max and seg_y_max >= poly_y_min):
                        return True
            return False
        
        def path_blocked(path, polys, excluded_points=None):
            """Check if any segment of a path is blocked."""
            for i in range(len(path) - 1):
                if segment_blocked(path[i], path[i + 1], polys, excluded_points):
                    return True
            return False
        
        def find_blocking_obs_for_path(path, polys):
            """Find all obstructions that block any segment of a path."""
            blocking = []
            for i in range(len(path) - 1):
                p1, p2 = path[i], path[i + 1]
                x1, y1 = p1[0] / dbu, p1[1] / dbu
                x2, y2 = p2[0] / dbu, p2[1] / dbu
                seg_x_min, seg_x_max = min(x1, x2), max(x1, x2)
                seg_y_min, seg_y_max = min(y1, y2), max(y1, y2)
                
                for poly in polys:
                    if len(poly) < 3:
                        continue
                    poly_x_min, poly_x_max = poly[:, 0].min(), poly[:, 0].max()
                    poly_y_min, poly_y_max = poly[:, 1].min(), poly[:, 1].max()
                    
                    if (seg_x_min <= poly_x_max and seg_x_max >= poly_x_min and
                        seg_y_min <= poly_y_max and seg_y_max >= poly_y_min):
                        blocking.append({
                            'x_min': poly_x_min * dbu, 'x_max': poly_x_max * dbu,
                            'y_min': poly_y_min * dbu, 'y_max': poly_y_max * dbu
                        })
            return blocking
        
        print(f"[VIA-ESCAPE] Evaluating routes from ({start_x:.3f}, {start_y:.3f}) to ({stop_x:.3f}, {stop_y:.3f})")
        
        # Generate candidate paths - ALWAYS try direct paths first (minimum wirelength)
        candidate_paths = []
        
        # Direct L-paths (optimal wirelength if unobstructed)
        # Horizontal-first: start -> horizontal -> vertical -> stop
        path_h_first = [
            (start_x, start_y),
            (stop_x, start_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('direct_h_first', path_h_first))
        
        # Vertical-first: start -> vertical -> horizontal -> stop
        path_v_first = [
            (start_x, start_y),
            (start_x, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('direct_v_first', path_v_first))
        
        # For aligned ports, also add the direct path
        if ports_vertically_aligned:
            path_direct = [(start_x, start_y), (stop_x, stop_y)]
            candidate_paths.append(('direct_vertical', path_direct))
        elif ports_horizontally_aligned:
            path_direct = [(start_x, start_y), (stop_x, stop_y)]
            candidate_paths.append(('direct_horizontal', path_direct))
            # Also try pure M2 route (horizontal)
            candidate_paths.append(('direct_m2_horizontal', path_direct))
        
        # Find obstructions that would block each path type
        # This allows us to calculate MINIMUM escape distances
        
        def find_blockers_for_horizontal_segment(y_coord, x_min, x_max, polys, excluded_points):
            """Find obstructions blocking a horizontal segment at y_coord from x_min to x_max."""
            blockers = []
            for poly in polys:
                if len(poly) < 3:
                    continue
                # Skip polygons containing excluded points (ports)
                skip = False
                if excluded_points:
                    for ex, ey in excluded_points:
                        if point_in_poly_bbox(ex, ey, poly):
                            skip = True
                            break
                if skip:
                    continue
                    
                poly_x_min, poly_x_max = poly[:, 0].min() * dbu, poly[:, 0].max() * dbu
                poly_y_min, poly_y_max = poly[:, 1].min() * dbu, poly[:, 1].max() * dbu
                
                # Check if segment overlaps with polygon
                if (poly_y_min - 0.1 <= y_coord <= poly_y_max + 0.1 and
                    x_min < poly_x_max and x_max > poly_x_min):
                    blockers.append({
                        'x_min': poly_x_min, 'x_max': poly_x_max,
                        'y_min': poly_y_min, 'y_max': poly_y_max
                    })
            return blockers
        
        def find_blockers_for_vertical_segment(x_coord, y_min, y_max, polys, excluded_points):
            """Find obstructions blocking a vertical segment at x_coord from y_min to y_max."""
            blockers = []
            for poly in polys:
                if len(poly) < 3:
                    continue
                skip = False
                if excluded_points:
                    for ex, ey in excluded_points:
                        if point_in_poly_bbox(ex, ey, poly):
                            skip = True
                            break
                if skip:
                    continue
                    
                poly_x_min, poly_x_max = poly[:, 0].min() * dbu, poly[:, 0].max() * dbu
                poly_y_min, poly_y_max = poly[:, 1].min() * dbu, poly[:, 1].max() * dbu
                
                if (poly_x_min - 0.1 <= x_coord <= poly_x_max + 0.1 and
                    y_min < poly_y_max and y_max > poly_y_min):
                    blockers.append({
                        'x_min': poly_x_min, 'x_max': poly_x_max,
                        'y_min': poly_y_min, 'y_max': poly_y_max
                    })
            return blockers
        
        port_points = [(start_x, start_y), (stop_x, stop_y)]
        
        # Calculate optimal escape distances based on ACTUAL blockers
        # For horizontal-first L-path: check horizontal at start_y and vertical at stop_x
        h_blockers_at_start = find_blockers_for_horizontal_segment(
            start_y, min(start_x, stop_x), max(start_x, stop_x), obstruction_polys, port_points)
        v_blockers_at_stop = find_blockers_for_vertical_segment(
            stop_x, min(start_y, stop_y), max(start_y, stop_y), obstruction_polys, port_points)
        
        # For vertical-first L-path: check vertical at start_x and horizontal at stop_y
        v_blockers_at_start = find_blockers_for_vertical_segment(
            start_x, min(start_y, stop_y), max(start_y, stop_y), obstruction_polys, port_points)
        h_blockers_at_stop = find_blockers_for_horizontal_segment(
            stop_y, min(start_x, stop_x), max(start_x, stop_x), obstruction_polys, port_points)
        
        # Collect all blockers to determine escape bounds
        all_blockers = h_blockers_at_start + v_blockers_at_stop + v_blockers_at_start + h_blockers_at_stop
        
        if all_blockers:
            # Calculate escape bounds from actual blockers (not ALL obstructions)
            blocker_x_min = min(b['x_min'] for b in all_blockers)
            blocker_x_max = max(b['x_max'] for b in all_blockers)
            blocker_y_min = min(b['y_min'] for b in all_blockers)
            blocker_y_max = max(b['y_max'] for b in all_blockers)
        else:
            blocker_x_min = min(start_x, stop_x) - clearance
            blocker_x_max = max(start_x, stop_x) + clearance
            blocker_y_min = min(start_y, stop_y) - clearance
            blocker_y_max = max(start_y, stop_y) + clearance

        # Force a minimum escape distance if blockers are too close to ports
        # This helps when the obstruction is exactly the device itself
        min_escape = 1.0 # 1um minimum escape
        if blocker_x_min > min(start_x, stop_x) - min_escape:
            blocker_x_min = min(start_x, stop_x) - min_escape
        if blocker_x_max < max(start_x, stop_x) + min_escape:
            blocker_x_max = max(start_x, stop_x) + min_escape
        if blocker_y_min > min(start_y, stop_y) - min_escape:
            blocker_y_min = min(start_y, stop_y) - min_escape
        if blocker_y_max < max(start_y, stop_y) + min_escape:
            blocker_y_max = max(start_y, stop_y) + min_escape
        
        # Generate escape paths with OPTIMAL escape distances
        # Escape LEFT - minimum X to clear blockers
        escape_x_left = blocker_x_min - clearance
        path_left = [
            (start_x, start_y),
            (escape_x_left, start_y),
            (escape_x_left, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('escape_left', path_left))
        
        # Escape RIGHT - minimum X to clear blockers  
        escape_x_right = blocker_x_max + clearance
        path_right = [
            (start_x, start_y),
            (escape_x_right, start_y),
            (escape_x_right, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('escape_right', path_right))
        
        # Escape TOP
        escape_y_top = blocker_y_max + clearance
        path_top = [
            (start_x, start_y),
            (start_x, escape_y_top),
            (stop_x, escape_y_top),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('escape_top', path_top))
        
        # Escape BOTTOM
        escape_y_bottom = blocker_y_min - clearance
        path_bottom = [
            (start_x, start_y),
            (start_x, escape_y_bottom),
            (stop_x, escape_y_bottom),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('escape_bottom', path_bottom))
        
        # S-shaped routes for complex scenarios
        path_up_left = [
            (start_x, start_y),
            (start_x, escape_y_top),
            (escape_x_left, escape_y_top),
            (escape_x_left, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('s_up_left', path_up_left))
        
        path_up_right = [
            (start_x, start_y),
            (start_x, escape_y_top),
            (escape_x_right, escape_y_top),
            (escape_x_right, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('s_up_right', path_up_right))
        
        path_down_left = [
            (start_x, start_y),
            (start_x, escape_y_bottom),
            (escape_x_left, escape_y_bottom),
            (escape_x_left, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('s_down_left', path_down_left))
        
        path_down_right = [
            (start_x, start_y),
            (start_x, escape_y_bottom),
            (escape_x_right, escape_y_bottom),
            (escape_x_right, stop_y),
            (stop_x, stop_y)
        ]
        candidate_paths.append(('s_down_right', path_down_right))
        
        # Evaluate all candidate paths - select shortest UNBLOCKED path
        best_path = None
        best_length = float('inf')
        best_name = None
        
        for name, candidate in candidate_paths:
            # First simplify to remove redundant points
            simplified = _simplify_path(candidate)
            
            # Validate: no consecutive same-direction segments
            if not _is_valid_manhattan_path(simplified):
                print(f"[VIA-ESCAPE] Path '{name}': INVALID (consecutive same-direction)")
                continue
            
            # Check if path is blocked (excluding polygons that contain the ports)
            port_points = [(start_x, start_y), (stop_x, stop_y)]
            # For direct M2 horizontal, check only M2 polygons
            polys_to_check = m2_polys if name == 'direct_m2_horizontal' else obstruction_polys
            is_blocked = path_blocked(simplified, polys_to_check, port_points)
            
            # Calculate length
            length = _calc_path_length(simplified)
            status = "BLOCKED" if is_blocked else "CLEAR"
            print(f"[VIA-ESCAPE] Path '{name}': length={length:.3f}um, {status}")
            
            # Only consider unblocked paths
            if not is_blocked and length < best_length:
                best_length = length
                best_path = simplified
                best_name = name
        
        if best_path is not None:
            path = best_path
            use_m2_horiz = (best_name == 'direct_m2_horizontal')
            print(f"[VIA-ESCAPE] Selected '{best_name}' route with length {best_length:.3f}um (minimum wirelength)")
            
    # Default to False if not set (normal routing)
    if 'use_m2_horiz' not in locals():
        use_m2_horiz = False
    
    if path is None:
        print("Hierarchical routing failed - no path found on M1 or M2")
        return []
    
    # Force first and last points to exact port centers
    path[0] = tuple(start.dcenter)
    path[-1] = tuple(stop.dcenter)
    
    # Ensure Manhattan and simplify
    path = _make_manhattan(path)
    path = _simplify_path(path)
    
    print(f"Route from {start.dcenter} to {stop.dcenter}")
    print(f"Final path ({len(path)} points): {path}")
    
    # Draw the segments - this enforces Horizontal=M1, Vertical=M2
    # Unless use_m2_horiz is True, in which case Horizontal=M2
    horiz_layer = LAYER_M2 if use_m2_horiz else LAYER_M1
    vert_layer = LAYER_M2
    add_vias = not use_m2_horiz
    
    segment_ports = _draw_route_segments(
        c, path, width,
        add_segment_ports=add_segment_ports,
        port_name_prefix=port_name_prefix,
        horizontal_layer=horiz_layer,
        vertical_layer=vert_layer,
        add_vias=add_vias
    )
    
    # Handle start/end layer transitions
    # This automatically adds vias if start/end ports (M1) don't match first/last segment M2
    if len(path) >= 2:
        first_horiz = _is_horizontal(path[0], path[1])
        first_layer = horiz_layer if first_horiz else vert_layer
        
        def _get_layer_tuple(port: Port, component: Component):
            if hasattr(port, "layer"):
                layer_idx = port.layer
                info = component.kcl.get_info(layer_idx)
                return (info.layer, info.datatype)
            return None

        start_layer = _get_layer_tuple(start, c)
        if start_layer and start_layer != first_layer:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = path[0]

        last_horiz = _is_horizontal(path[-2], path[-1])
        last_layer = horiz_layer if last_horiz else vert_layer
        stop_layer = _get_layer_tuple(stop, c)
        if stop_layer and stop_layer != last_layer:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = path[-1]
    
    return segment_ports


def route_multilayer_3d(
    c: Component,
    start: Port,
    stop: Port,
    grid_unit: float = 1.0,
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    add_segment_ports: bool = False,
    port_name_prefix: str = "seg",
    via_cost: float = 10.0,
    wrong_way_penalty: float = 8.0,
) -> List[Port]:
    """Route using the new 3D multi-layer A* router.
    
    This uses the Rust-based show_3d function which builds a 3D grid
    with per-layer obstructions and finds a path using cost-weighted A*.
    
    Metal 1 (layer 0) is treated as Horizontal-preferred.
    Metal 2 (layer 1) is treated as Vertical-preferred.
    Vias are placed automatically at layer transitions.
    
    Args:
        c: Component to add the route to.
        start: Start port.
        stop: Stop port.
        grid_unit: Grid resolution in um.
        width: Wire width in um.
        layers_to_avoid: Layers containing obstructions (per-layer).
        add_segment_ports: If True, add a port to each straight segment.
        port_name_prefix: Prefix for port names.
        via_cost: Cost weight for via transitions.
        wrong_way_penalty: Penalty for routing against preferred direction.
    
    Returns:
        List of ports added to segments.
    """
    from doroutes import doroutes as _doroutes
    
    if layers_to_avoid is None:
        layers_to_avoid = []
    
    dbu = c.kcl.dbu
    kc = c.kcl.kcells[c.name]
    
    _layers = [layer if isinstance(layer, tuple) else (layer, 0) for layer in layers_to_avoid]
    
    # Get port positions
    start_pos = _get_pos_with_dir(start, dbu)
    stop_pos = _get_pos_with_dir(stop, dbu)
    
    # Invert stop orientation (port faces inward, we approach from opposite direction)
    stop_dir_map = {"n": "s", "s": "n", "e": "w", "w": "e", "o": "o"}
    stop_pos = (stop_pos[0], stop_pos[1], stop_dir_map[stop_pos[2]])
    
    # Port points for polygon exclusion
    port_points = [
        (start_pos[0], start_pos[1]),
        (stop_pos[0], stop_pos[1]),
    ]
    
    # Extract per-layer obstruction polygons separately
    # M1 metal blocks only layer 0, M2 metal blocks only layer 1
    # This enables the router to escape via layer transitions
    m1_polys = _extract_polys_for_layers(kc, [LAYER_M1], dbu, port_points) if LAYER_M1 in _layers else []
    m2_polys = _extract_polys_for_layers(kc, [LAYER_M2], dbu, port_points) if LAYER_M2 in _layers else []
    
    polys_per_layer = [
        m1_polys,  # Layer 0 (M1) — only M1 obstructions
        m2_polys,  # Layer 1 (M2) — only M2 obstructions
    ]
    
    # Bounding box
    start_x, start_y = start_pos[0], start_pos[1]
    stop_x, stop_y = stop_pos[0], stop_pos[1]
    dist = max(abs(stop_x - start_x), abs(stop_y - start_y))
    padding = int(dist * 0.5)
    
    comp_bbox = kc.bbox()
    min_x = min(start_x, stop_x, comp_bbox.left) - padding
    max_x = max(start_x, stop_x, comp_bbox.right) + padding
    min_y = min(start_y, stop_y, comp_bbox.bottom) - padding
    max_y = max(start_y, stop_y, comp_bbox.top) + padding
    
    bbox_tuple = (max_y, max_x, min_y, min_x)
    
    grid_unit_dbu = int(grid_unit / dbu)
    
    # Helper to get layer tuple from port
    def _get_layer_tuple_local(port, component):
        if hasattr(port, "layer"):
            layer_idx = port.layer
            info = component.kcl.get_info(layer_idx)
            return (info.layer, info.datatype)
        return None
    
    # Determine start/stop layer from port layer
    start_layer_idx = 0  # Default to M1
    stop_layer_idx = 0
    
    start_layer = _get_layer_tuple_local(start, c)
    stop_layer = _get_layer_tuple_local(stop, c)
    
    if start_layer == LAYER_M2:
        start_layer_idx = 1
    if stop_layer == LAYER_M2:
        stop_layer_idx = 1
    
    # Prepare start/stop with layer info
    start_3d = (start_x, start_y, start_layer_idx, start_pos[2])
    stop_3d = (stop_x, stop_y, stop_layer_idx, stop_pos[2])
    
    # Debug: show grid dimensions
    grid_w = (max_x - min_x) // grid_unit_dbu
    grid_h = (max_y - min_y) // grid_unit_dbu
    num_m1_polys = len(m1_polys) if 'm1_polys' in dir() else len(polys_per_layer[0])
    num_m2_polys = len(m2_polys) if 'm2_polys' in dir() else len(polys_per_layer[1])
    print(f"[3D ROUTE] Grid: {grid_w}x{grid_h} x 2 layers = {grid_w*grid_h*2} cells")
    print(f"[3D ROUTE] Obstructions: M1={num_m1_polys}, M2={num_m2_polys}")
    print(f"[3D ROUTE] from ({start_x*dbu:.3f}, {start_y*dbu:.3f}, L{start_layer_idx}) "
          f"to ({stop_x*dbu:.3f}, {stop_y*dbu:.3f}, L{stop_layer_idx})")
    print(f"[3D ROUTE] BBox: ({min_x*dbu:.1f}, {min_y*dbu:.1f}) -> ({max_x*dbu:.1f}, {max_y*dbu:.1f})")
    
    try:
        corners_3d, num_vias = _doroutes.show_3d(
            polys_per_layer=polys_per_layer,
            start=start_3d,
            stop=stop_3d,
            bbox=bbox_tuple,
            grid_unit=grid_unit_dbu,
            layer_directions=["h", "v"],  # M1=horizontal, M2=vertical
            via_cost=via_cost,
            wrong_way_penalty=wrong_way_penalty,
        )
    except Exception as e:
        print(f"[3D ROUTE] Failed: {e}")
        # Retry with larger bounding box and finer grid
        print("[3D ROUTE] Retrying with expanded bounding box and finer grid...")
        try:
            # Expand bbox by 50% more
            retry_padding = int(padding * 2.0) # Double the original padding
            retry_min_x = min_x - padding 
            retry_max_x = max_x + padding
            retry_min_y = min_y - padding
            retry_max_y = max_y + padding
            retry_bbox = (retry_max_y, retry_max_x, retry_min_y, retry_min_x)
            
            # Use finer grid
            retry_grid_unit = grid_unit * 0.5
            retry_grid_unit_dbu = int(retry_grid_unit / dbu)
             
            # Update grid dimensions for log
            r_grid_w = (retry_max_x - retry_min_x) // retry_grid_unit_dbu
            r_grid_h = (retry_max_y - retry_min_y) // retry_grid_unit_dbu
            print(f"[3D ROUTE RETRY] Grid: {r_grid_w}x{r_grid_h} x 2 layers")
            
            corners_3d, num_vias = _doroutes.show_3d(
                polys_per_layer=polys_per_layer,
                start=start_3d,
                stop=stop_3d,
                bbox=retry_bbox,
                grid_unit=retry_grid_unit_dbu,
                layer_directions=["h", "v"],
                via_cost=via_cost,
                wrong_way_penalty=wrong_way_penalty,
            )
        except Exception as e2:
            print(f"[3D ROUTE] Retry failed: {e2}")
            # Fallback to existing hierarchical router
            print("[3D ROUTE] Falling back to hierarchical router...")
            return route_hierarchical(
                c, start, stop,
                global_grid_unit=grid_unit * 2,
                detail_grid_unit=grid_unit,
                width=width,
                layers_to_avoid=layers_to_avoid,
                add_segment_ports=add_segment_ports,
                port_name_prefix=port_name_prefix,
            )
    
    print(f"[3D ROUTE] Found path with {len(corners_3d)} corners, {num_vias} vias")
    
    # Manhattanize the 3D path to fix any diagonal segments
    # The A* router or simplification might return diagonal jumps for off-grid points
    manhattan_corners = []
    if len(corners_3d) > 0:
        manhattan_corners.append(corners_3d[0])
        
        for i in range(1, len(corners_3d)):
            prev = manhattan_corners[-1]
            curr = corners_3d[i]
            
            # Check for layer transition (via)
            if prev[2] != curr[2]:
                manhattan_corners.append(curr)
                continue
                
            # Check for diagonal movement on same layer
            dx = abs(curr[0] - prev[0])
            dy = abs(curr[1] - prev[1])
            
            if dx > 1 and dy > 1: # Tolerance of 1 DBU
                # Diagonal! Split into L-shape based on layer preference
                layer_idx = curr[2]
                # Even layer (0, 2...) -> Horizontal preference (M1) -> Move H then V
                # Odd layer (1, 3...) -> Vertical preference (M2) -> Move V then H
                # (Assuming M1=H, M2=V as per standard Sky130 usage here)
                
                if layer_idx % 2 == 0: # M1 (Horizontal)
                    # Add intermediate point: (curr.x, prev.y)
                    # First leg Horizontal, second Vertical
                    intermediate = (curr[0], prev[1], layer_idx)
                    manhattan_corners.append(intermediate)
                else: # M2 (Vertical)
                    # Add intermediate point: (prev.x, curr.y)
                    # First leg Vertical, second Horizontal
                    intermediate = (prev[0], curr[1], layer_idx)
                    manhattan_corners.append(intermediate)
            
            manhattan_corners.append(curr)

    corners_3d = manhattan_corners
    
    # Via Straightening: Remove small detours around vias
    # Identify pattern: P[i-1] -> P[i](via start) -> P[i+1](via end) -> P[i+2]
    # If P[i-1] and P[i+2] align (same X or Y), but P[i]/P[i+1] are offset, align them.
    if len(corners_3d) >= 4:
        for i in range(1, len(corners_3d) - 2):
            p_prev = corners_3d[i-1]
            p_via_start = corners_3d[i]
            p_via_end = corners_3d[i+1]
            p_next = corners_3d[i+2]
            
            # Check if this is a via transition
            if p_via_start[2] == p_via_end[2]:
                continue # Not a via
            if p_prev[2] != p_via_start[2] or p_via_end[2] != p_next[2]:
                continue # Complex transition, skip
                
            # Check Y-alignment (Horizontal Check)
            if abs(p_prev[1] - p_next[1]) < 0.001: 
                common_y = p_prev[1]
                # Check if via is detoured from this Y
                if abs(p_via_start[1] - common_y) > 0.001:
                    # Check if detour is small (e.g. <= 2 grid units)
                    # We can use a simpler heuristic: just straighten if distance is reasonable
                    # Assuming < 3um for a local jog
                    if abs(p_via_start[1] - common_y) * dbu < 3.0: 
                        # Straighten!
                        # Update via coordinates to match the common Y
                        corners_3d[i] = (p_via_start[0], common_y, p_via_start[2])
                        corners_3d[i+1] = (p_via_end[0], common_y, p_via_end[2])
                        
            # Check X-alignment (Vertical Check)
            elif abs(p_prev[0] - p_next[0]) < 0.001:
                common_x = p_prev[0]
                # Check if via is detoured from this X
                if abs(p_via_start[0] - common_x) > 0.001:
                     if abs(p_via_start[0] - common_x) * dbu < 3.0:
                        corners_3d[i] = (common_x, p_via_start[1], p_via_start[2])
                        corners_3d[i+1] = (common_x, p_via_end[1], p_via_end[2])

    
    # Force first and last corners to exact port positions (undo grid snapping)
    # After forcing, re-manhattanize any resulting diagonal first/last segments
    if len(corners_3d) >= 2:
        corners_3d[0] = (start_x, start_y, corners_3d[0][2])
        corners_3d[-1] = (stop_x, stop_y, corners_3d[-1][2])
        
        # Fix diagonal created at start (first segment)
        if corners_3d[0][2] == corners_3d[1][2]:  # Same layer
            dx = abs(corners_3d[1][0] - corners_3d[0][0])
            dy = abs(corners_3d[1][1] - corners_3d[0][1])
            if dx > 1 and dy > 1:  # Diagonal (both x and y differ by > 1 DBU)
                layer_idx = corners_3d[0][2]
                if layer_idx % 2 == 0:  # M1 (H pref): horizontal first
                    intermediate = (corners_3d[1][0], corners_3d[0][1], layer_idx)
                else:  # M2 (V pref): vertical first
                    intermediate = (corners_3d[0][0], corners_3d[1][1], layer_idx)
                corners_3d.insert(1, intermediate)
        
        # Fix diagonal created at end (last segment)
        if corners_3d[-1][2] == corners_3d[-2][2]:  # Same layer
            dx = abs(corners_3d[-1][0] - corners_3d[-2][0])
            dy = abs(corners_3d[-1][1] - corners_3d[-2][1])
            if dx > 1 and dy > 1:  # Diagonal
                layer_idx = corners_3d[-1][2]
                if layer_idx % 2 == 0:  # M1 (H pref): arrive via vertical then horizontal
                    intermediate = (corners_3d[-1][0], corners_3d[-2][1], layer_idx)
                else:  # M2 (V pref): arrive via horizontal then vertical
                    intermediate = (corners_3d[-2][0], corners_3d[-1][1], layer_idx)
                corners_3d.insert(-1, intermediate)
    
    # Via coalescing: eliminate small same-layer jog segments near via transitions
    # When the A* grid snaps a via position, it can create tiny segments between
    # the exact port position and the grid-aligned via. This pass moves the via
    # to absorb those jogs.
    min_jog_dbu = grid_unit_dbu  # Segments shorter than 1 grid unit are jogs
    
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(corners_3d) - 1:
            # Find via transitions (different layer)
            if corners_3d[i][2] != corners_3d[i + 1][2]:
                via_start_idx = i
                via_end_idx = i + 1
                
                # Check for small segment BEFORE via
                if via_start_idx > 0 and corners_3d[via_start_idx - 1][2] == corners_3d[via_start_idx][2]:
                    prev = corners_3d[via_start_idx - 1]
                    curr = corners_3d[via_start_idx]
                    seg_len = abs(curr[0] - prev[0]) + abs(curr[1] - prev[1])
                    if 0 < seg_len < min_jog_dbu:
                        # Move via to previous point's position (absorb the jog)
                        corners_3d[via_start_idx] = (prev[0], prev[1], curr[2])
                        corners_3d[via_end_idx] = (prev[0], prev[1], corners_3d[via_end_idx][2])
                        # Previous point is now redundant (same position/layer as via start)
                        corners_3d.pop(via_start_idx - 1)
                        changed = True
                        continue
                
                # Check for small segment AFTER via
                if via_end_idx + 1 < len(corners_3d) and corners_3d[via_end_idx][2] == corners_3d[via_end_idx + 1][2]:
                    curr = corners_3d[via_end_idx]
                    nxt = corners_3d[via_end_idx + 1]
                    seg_len = abs(nxt[0] - curr[0]) + abs(nxt[1] - curr[1])
                    if 0 < seg_len < min_jog_dbu:
                        # Move via to next point's position (absorb the jog)
                        corners_3d[via_start_idx] = (nxt[0], nxt[1], corners_3d[via_start_idx][2])
                        corners_3d[via_end_idx] = (nxt[0], nxt[1], curr[2])
                        # Next point is now redundant
                        corners_3d.pop(via_end_idx + 1)
                        changed = True
                        continue
            i += 1
    
    # Remove consecutive duplicate points (same position and layer)
    deduped = [corners_3d[0]]
    for j in range(1, len(corners_3d)):
        prev = deduped[-1]
        curr = corners_3d[j]
        if prev[0] == curr[0] and prev[1] == curr[1] and prev[2] == curr[2]:
            continue
        deduped.append(curr)
    corners_3d = deduped
    
    # Debug: print final path
    print(f"[3D ROUTE] Final path ({len(corners_3d)} corners):")
    for idx, (cx, cy, cz) in enumerate(corners_3d):
        print(f"  [{idx}] ({cx*dbu:.3f}, {cy*dbu:.3f}) L{cz} ({'M1' if cz==0 else 'M2'})")
    
    # Convert corners to um with layer information
    segment_ports = []
    
    # Helper to draw a single segment (horizontal or vertical)
    def _draw_seg(p_start, p_end, seg_layer):
        """Draw a single manhattan segment between two um-coordinate points."""
        sdx = abs(p_end[0] - p_start[0])
        sdy = abs(p_end[1] - p_start[1])
        
        if sdx < MIN_SEGMENT_LENGTH and sdy < MIN_SEGMENT_LENGTH:
            return  # Zero-length
        
        is_horiz = sdy < 0.001
        
        if is_horiz:
            x_min = min(p_start[0], p_end[0])
            x_max = max(p_start[0], p_end[0])
            seg_len = x_max - x_min
            y = p_start[1]
            if seg_len >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(seg_len, width), layer=seg_layer)
                )
                rect.dmove((x_min, y - width / 2))
                
                if add_segment_ports:
                    port_center = (x_min + seg_len / 2, y)
                    port = c.add_port(
                        name=f"{port_name_prefix}",
                        center=port_center,
                        width=0.01,
                        orientation=0,
                        layer=(seg_layer[0], 16),
                        port_type="electrical"
                    )
                    segment_ports.append(port)
                    c.draw_ports()
        else:
            y_min = min(p_start[1], p_end[1])
            y_max = max(p_start[1], p_end[1])
            seg_len = y_max - y_min
            x = p_start[0]
            if seg_len >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(width, seg_len), layer=seg_layer)
                )
                rect.dmove((x - width / 2, y_min))
                
                if add_segment_ports:
                    port_center = (x, y_min + seg_len / 2)
                    port = c.add_port(
                        name=f"{port_name_prefix}",
                        center=port_center,
                        width=0.01,
                        orientation=90,
                        layer=(seg_layer[0], 16),
                        port_type="electrical"
                    )
                    segment_ports.append(port)
                    c.draw_ports()
    
    # Add corner patches to ensure connectivity at bends
    for x, y, z in corners_3d:
        layer = LAYER_M1 if z == 0 else LAYER_M2
        patch = c.add_ref(gf.components.rectangle(size=(width, width), layer=layer))
        patch.dcenter = (x * dbu, y * dbu)
        
    if len(corners_3d) < 2:
        return segment_ports
    
    for i in range(len(corners_3d) - 1):
        x0, y0, z0 = corners_3d[i]
        x1, y1, z1 = corners_3d[i + 1]
        
        # Convert to um
        p0 = (x0 * dbu, y0 * dbu)
        p1 = (x1 * dbu, y1 * dbu)
        
        # Check for layer transition (via needed)
        if z0 != z1:
            # Place via at transition point
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = p0
            
            # If via transition also changes position, draw connecting segment
            # on the DESTINATION layer from the via location to the next point
            pos_dx = abs(p1[0] - p0[0])
            pos_dy = abs(p1[1] - p0[1])
            if pos_dx > 0.001 or pos_dy > 0.001:
                dest_layer = LAYER_M1 if z1 == 0 else LAYER_M2
                if pos_dx > 0.001 and pos_dy > 0.001:
                    # Diagonal - split into manhattan segments
                    if z1 % 2 == 0:  # M1 dest: horizontal first
                        mid = (p1[0], p0[1])
                    else:  # M2 dest: vertical first
                        mid = (p0[0], p1[1])
                    _draw_seg(p0, mid, dest_layer)
                    patch = c.add_ref(gf.components.rectangle(size=(width, width), layer=dest_layer))
                    patch.dcenter = mid
                    _draw_seg(mid, p1, dest_layer)
                else:
                    _draw_seg(p0, p1, dest_layer)
            continue
        
        # Determine layer from z index
        layer = LAYER_M1 if z0 == 0 else LAYER_M2
        
        # Check if segment is diagonal (both dx and dy nonzero)
        dx = abs(p1[0] - p0[0])
        dy = abs(p1[1] - p0[1])
        
        if dx < MIN_SEGMENT_LENGTH and dy < MIN_SEGMENT_LENGTH:
            continue  # Skip zero-length segments
        
        if dx > 0.001 and dy > 0.001:
            # Diagonal segment - split into H + V based on layer preference
            if z0 % 2 == 0:  # M1: horizontal first
                mid = (p1[0], p0[1])
                _draw_seg(p0, mid, layer)
                # Add corner patch at bend
                patch = c.add_ref(gf.components.rectangle(size=(width, width), layer=layer))
                patch.dcenter = mid
                _draw_seg(mid, p1, layer)
            else:  # M2: vertical first
                mid = (p0[0], p1[1])
                _draw_seg(p0, mid, layer)
                patch = c.add_ref(gf.components.rectangle(size=(width, width), layer=layer))
                patch.dcenter = mid
                _draw_seg(mid, p1, layer)
        else:
            # Pure horizontal or vertical - draw directly
            _draw_seg(p0, p1, layer)
    
    return segment_ports

