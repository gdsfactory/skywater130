"""Utilities for multi-layer routing using doroutes A* pathfinding."""

from functools import partial
from typing import Iterable, List, Tuple

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import LayerSpec, Port
import numpy as np

from doroutes import find_route_astar
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
    detail_straight_width = max(1, width_dbu // detail_grid_dbu + 1)
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
        detail_corners = _run_astar_rectilinear(
            polys=polys,
            start_pos=seg_start_pos,
            stop_pos=seg_end_pos,
            bbox_tuple=seg_bbox,
            grid_unit_dbu=detail_grid_dbu,
            straight_width=detail_straight_width,
            bend_radius=detail_bend_radius,
        )
        
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


def route_multilayer_astar(
    c: Component,
    start: Port,
    stop: Port,
    grid_unit: float = 0.5,  # Increased default for faster routing
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    rectilinear: bool = True,
    bend_radius: int = 1,  # Configurable bend radius in grid units
) -> None:
    """Route between start and stop ports using Metal1 (Horizontal) and Metal2 (Vertical).

    Uses `find_route_astar` from doroutes for pathfinding, then places:
    - Metal 1 rectangles for horizontal segments
    - Metal 2 rectangles for vertical segments
    - via_m1_m2 at every corner (layer transition point)

    Args:
        c: Component to add the route to.
        start: Start port.
        stop: Stop port.
        grid_unit: Discretization unit for A* algorithm (um). Larger = faster but less precise.
        width: Width of the metal traces (um).
        layers_to_avoid: Layers containing obstructions.
        rectilinear: If True, use square 90° corners instead of smooth bends.
        bend_radius: Bend radius in grid units (larger = fewer corners allowed).
    """
    if layers_to_avoid is None:
        layers_to_avoid = []

    dbu = c.kcl.dbu
    grid_unit_dbu = int(grid_unit / dbu)

    # 1. Find the path (corners) using A*
    if rectilinear:
        # Rectilinear mode: use simple L-pattern for square corners
        # Import doroutes directly to call show() with custom bend pattern
        from doroutes import doroutes as _doroutes
        from kfactory import kdb
        import numpy as np
        
        kc = c.kcl.kcells[c.name]
        
        # Get validated layers
        _layers = [layer if isinstance(layer, tuple) else (layer, 0) for layer in layers_to_avoid]
        
        # Extract polygons from layers to avoid
        polys = []
        for layer in _layers:
            layer_idx = kc.kcl.layer(*layer)
            r = kdb.Region(kc.begin_shapes_rec(layer_idx))
            for poly in r.each():
                pts = np.array([(p.x, p.y) for p in poly.each_point_hull()], dtype=np.int64)
                polys.append(pts)
        
        # OPTIMIZATION: Tighter bounding box based on actual start/stop distance
        start_x = int(start.dcenter[0] / dbu)
        start_y = int(start.dcenter[1] / dbu)
        stop_x = int(stop.dcenter[0] / dbu)
        stop_y = int(stop.dcenter[1] / dbu)
        
        # Calculate distance and use proportional padding
        dist_x = abs(stop_x - start_x)
        dist_y = abs(stop_y - start_y)
        max_dist = max(dist_x, dist_y, grid_unit_dbu * 10)  # Minimum 10 grid units
        padding = int(max_dist * 0.3)  # 30% margin around the route
        
        # Use tighter bounds derived from start/stop positions
        min_x = min(start_x, stop_x) - padding
        max_x = max(start_x, stop_x) + padding
        min_y = min(start_y, stop_y) - padding
        max_y = max(start_y, stop_y) + padding
        
        # Also include component bbox to ensure we can route around obstacles
        comp_bbox = kc.bbox()
        min_x = min(min_x, comp_bbox.left - padding // 2)
        max_x = max(max_x, comp_bbox.right + padding // 2)
        min_y = min(min_y, comp_bbox.bottom - padding // 2)
        max_y = max(max_y, comp_bbox.top + padding // 2)
        
        bbox_tuple = (max_y, max_x, min_y, min_x)  # (north, east, south, west)
        
        # Get start/stop positions and orientations
        def get_pos_with_dir(port):
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
        
        start_pos = get_pos_with_dir(start)
        stop_pos = get_pos_with_dir(stop)
        # Invert stop orientation (port faces inward)
        stop_dir_map = {"n": "s", "s": "n", "e": "w", "w": "e", "o": "o"}
        stop_pos = (stop_pos[0], stop_pos[1], stop_dir_map[stop_pos[2]])
        
        # Rectilinear bend pattern: simple L-shape
        # Calculate bend_radius from wire width to ensure minimum straight = wire width
        # bend_radius in grid units = ceil(width / grid_unit)
        width_dbu = int(width / dbu)
        effective_bend_radius = max(bend_radius, (width_dbu + grid_unit_dbu - 1) // grid_unit_dbu)
        
        rectilinear_bend = [(i, 0) for i in range(1, effective_bend_radius + 1)] + \
                          [(effective_bend_radius, i) for i in range(1, effective_bend_radius + 1)]
        
        # Calculate straight width in grid units
        straight_width = width_dbu // grid_unit_dbu + 1
        straight_width += (straight_width + 1) % 2
        
        # Debug output
        print(f"DEBUG: start_pos={start_pos}, stop_pos={stop_pos}")
        print(f"DEBUG: effective_bend_radius={effective_bend_radius}, straight_width={straight_width}")
        print(f"DEBUG: grid_unit_dbu={grid_unit_dbu}, width_dbu={width_dbu}")
        print(f"DEBUG: bbox={bbox_tuple}")
        print(f"DEBUG: num_polys={len(polys)}")
        
        corners = None
        
        # First try with exact orientations
        try:
            corners = _doroutes.show(
                polys=polys,
                start=start_pos,
                stop=stop_pos,
                bbox=bbox_tuple,
                grid_unit=grid_unit_dbu,
                straight_width=straight_width,
                discretized_bend_east_to_north=rectilinear_bend,
            )
        except Exception as e:
            print(f"A* with exact orientations failed: {e}")
        
        # If failed, try with relaxed orientations (omnidirectional)
        if corners is None:
            print("DEBUG: Retrying with relaxed orientations...")
            start_pos_relaxed = (start_pos[0], start_pos[1], "o")
            stop_pos_relaxed = (stop_pos[0], stop_pos[1], "o")
            try:
                corners = _doroutes.show(
                    polys=polys,
                    start=start_pos_relaxed,
                    stop=stop_pos_relaxed,
                    bbox=bbox_tuple,
                    grid_unit=grid_unit_dbu,
                    straight_width=straight_width,
                    discretized_bend_east_to_north=rectilinear_bend,
                )
            except Exception as e:
                print(f"A* rectilinear pathfinding failed (relaxed): {e}")
                return
    else:
        # Original mode: use via-based bend specification
        bend_spec = partial(via_m1_m2, width=width)
        straight_spec = "straight_metal1"
        
        try:
            corners = find_route_astar(
                c=c,
                start=start,
                stop=stop,
                straight=straight_spec,
                bend=bend_spec,
                layers=layers_to_avoid,
                grid_unit=grid_unit_dbu,
            )
        except Exception as e:
            print(f"A* pathfinding failed: {e}")
            return

    if not corners:
        print("No route found!")
        return

    # 2. Convert corners from DBU to um
    points_um = [(p[0] * dbu, p[1] * dbu) for p in corners]

    # Force first and last points to be exactly at port centers
    points_um[0] = tuple(start.dcenter)
    points_um[-1] = tuple(stop.dcenter)

    # 3. Make the path strictly Manhattan by inserting jog points where needed
    points_um = _make_manhattan(points_um)
    
    # OPTIMIZATION: Simplify path by removing redundant corners
    points_um = _simplify_path(points_um)

    print(f"Route from {start.dcenter} to {stop.dcenter}")
    print(f"Simplified Manhattan points ({len(points_um)}): {points_um}")

    # 4. Draw segments and vias
    for i in range(len(points_um) - 1):
        p_curr = points_um[i]
        p_next = points_um[i + 1]

        horiz = _is_horizontal(p_curr, p_next)

        if horiz:
            # Horizontal segment on M1
            x_min = min(p_curr[0], p_next[0])
            x_max = max(p_curr[0], p_next[0])
            length = x_max - x_min
            y = p_curr[1]

            if length >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(length, width), layer=LAYER_M1)
                )
                rect.dmove((x_min, y - width / 2))
        else:
            # Vertical segment on M2
            y_min = min(p_curr[1], p_next[1])
            y_max = max(p_curr[1], p_next[1])
            length = y_max - y_min
            x = p_curr[0]

            if length >= 0.001:
                rect = c.add_ref(
                    gf.components.rectangle(size=(width, length), layer=LAYER_M2)
                )
                rect.dmove((x - width / 2, y_min))

        # Place via at each corner (intermediate points only, not start/end yet)
        if i < len(points_um) - 2:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = p_next

    # 5. Handle start/end layer transitions
    if len(points_um) >= 2:
        # Check start: does the first segment match the start port's layer?
        first_horiz = _is_horizontal(points_um[0], points_um[1])
        first_layer = LAYER_M1 if first_horiz else LAYER_M2

        # Port.layer is an int layer index; convert to (layer, datatype) tuple
        def _get_layer_tuple(port: Port, component: Component):
            if hasattr(port, "layer"):
                layer_idx = port.layer
                info = component.kcl.get_info(layer_idx)
                return (info.layer, info.datatype)
            return None

        start_layer = _get_layer_tuple(start, c)
        if start_layer and start_layer != first_layer:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = points_um[0]

        # Check end: does the last segment match the stop port's layer?
        last_horiz = _is_horizontal(points_um[-2], points_um[-1])
        last_layer = LAYER_M1 if last_horiz else LAYER_M2
        stop_layer = _get_layer_tuple(stop, c)
        if stop_layer and stop_layer != last_layer:
            via = c.add_ref(via_m1_m2(width=width, length=width))
            via.dcenter = points_um[-1]


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
            # No blockers - use port bounds
            blocker_x_min = min(start_x, stop_x) - clearance
            blocker_x_max = max(start_x, stop_x) + clearance
            blocker_y_min = min(start_y, stop_y) - clearance
            blocker_y_max = max(start_y, stop_y) + clearance
        
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
