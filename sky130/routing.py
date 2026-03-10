"""Routing functions with obstacle avoidance for sky130 PDK."""

from typing import Any, Sequence

import gdsfactory as gf
import klayout.dbcore as kdb
import networkx as nx
import numpy as np
import numpy.typing as npt
from gdsfactory.component import Component
from gdsfactory.typings import (
    ComponentSpec,
    CrossSectionSpec,
    LayerSpec,
    Port,
)
from gdsfactory.routing.route_astar import _generate_grid, _parse_bbox_to_array, _extract_all_bbox


class Route:
    """Container for route results."""
    def __init__(self, references: list[Any], length: float, length_effective: float, ports: list[Port]):
        self.references = references
        self.length = length
        self.length_effective = length_effective
        self.ports = ports


def _mark_layer_obstacles(
    grid: np.ndarray,
    component: Component,
    layer: LayerSpec,
    x_vals: np.ndarray,
    y_vals: np.ndarray,
    resolution: float,
    distance: float,
) -> None:
    """Mark existing geometry on a layer as obstacles in the grid.
    
    Args:
        grid: Grid array to modify in-place.
        component: Component containing geometry.
        layer: Layer to extract geometry from.
        x_vals: X coordinate array.
        y_vals: Y coordinate array.
        resolution: Grid resolution in um.
        distance: Clearance distance in um.
    """
    try:
        polygons = component.get_polygons(by='name', layers=[layer])
    except Exception:
        return
    
    if not polygons:
        return
    
    # Get layer name - handle both string and tuple formats
    layer_name = None
    
    # If layer is already a string, try it directly
    if isinstance(layer, str):
        if layer in polygons:
            layer_name = layer
        else:
            # Try with 'drawing' suffix
            for suffix in ['drawing', '']:
                test_name = f"{layer}{suffix}" if suffix else layer
                if test_name in polygons:
                    layer_name = test_name
                    break
    elif isinstance(layer, tuple):
        # Try common naming conventions for tuple layers
        for name in [f"met{layer[0]-67}drawing", f"M{layer[0]-67}", f"({layer[0]}, {layer[1]})", str(layer)]:
            if name in polygons:
                layer_name = name
                break
    
    # Fall back to first key if still not found
    if layer_name is None:
        for key in polygons.keys():
            layer_name = key
            break
    
    if layer_name is None or layer_name not in polygons:
        return

    
    for poly in polygons[layer_name]:
        bbox = poly.bbox()
        # Convert from nm to um
        xmin_um = bbox.left / 1000 - distance
        xmax_um = bbox.right / 1000 + distance
        ymin_um = bbox.bottom / 1000 - distance
        ymax_um = bbox.top / 1000 + distance
        
        # Convert to grid indices
        xmin_idx = int(np.clip(np.floor((xmin_um - x_vals.min()) / resolution), 0, len(x_vals) - 1))
        xmax_idx = int(np.clip(np.ceil((xmax_um - x_vals.min()) / resolution), 0, len(x_vals) - 1))
        ymin_idx = int(np.clip(np.floor((ymin_um - y_vals.min()) / resolution), 0, len(y_vals) - 1))
        ymax_idx = int(np.clip(np.ceil((ymax_um - y_vals.min()) / resolution), 0, len(y_vals) - 1))
        
        # Mark as obstacle
        grid[xmin_idx:xmax_idx + 1, ymin_idx:ymax_idx + 1] = 1


def _simplify_manhattan_path(waypoints: list[list[float]], min_segment_length: float = 0.5) -> list[list[float]]:
    """Simplify a Manhattan path by removing unnecessary waypoints.
    
    This removes:
    - Collinear points (points on the same line)
    - Very short segments that can be merged
    - Redundant direction changes
    
    Args:
        waypoints: List of [x, y] waypoints.
        min_segment_length: Minimum segment length to keep.
        
    Returns:
        Simplified list of waypoints.
    """
    if len(waypoints) <= 2:
        return waypoints
    
    # First pass: remove collinear points
    simplified = [waypoints[0]]
    for i in range(1, len(waypoints) - 1):
        prev = simplified[-1]
        curr = waypoints[i]
        next_pt = waypoints[i + 1]
        
        # Check if curr is collinear with prev and next
        # For Manhattan paths, collinear means same x or same y for all three
        same_x = np.isclose(prev[0], curr[0]) and np.isclose(curr[0], next_pt[0])
        same_y = np.isclose(prev[1], curr[1]) and np.isclose(curr[1], next_pt[1])
        
        if not (same_x or same_y):
            simplified.append(curr)
    
    simplified.append(waypoints[-1])
    
    # Second pass: merge very short segments
    if len(simplified) <= 2:
        return simplified
    
    merged = [simplified[0]]
    i = 1
    while i < len(simplified) - 1:
        curr = simplified[i]
        next_pt = simplified[i + 1]
        
        # Calculate segment length
        dx = abs(curr[0] - merged[-1][0])
        dy = abs(curr[1] - merged[-1][1])
        segment_len = max(dx, dy)  # Manhattan distance
        
        if segment_len < min_segment_length:
            # Try to skip this point if it doesn't create non-Manhattan path
            prev = merged[-1]
            # Check if prev -> next is still Manhattan
            dx_skip = abs(next_pt[0] - prev[0])
            dy_skip = abs(next_pt[1] - prev[1])
            
            if np.isclose(dx_skip, 0) or np.isclose(dy_skip, 0):
                # Can skip current point
                i += 1
                continue
        
        merged.append(curr)
        i += 1
    
    merged.append(simplified[-1])
    
    # Third pass: remove redundant zigzags (e.g., right-up-right can become just right-up)
    if len(merged) <= 3:
        return merged
    
    final = [merged[0], merged[1]]
    for i in range(2, len(merged)):
        prev_prev = final[-2]
        prev = final[-1]
        curr = merged[i]
        
        # Check if prev_prev -> prev and prev -> curr are in same direction
        # and could be combined
        dx1 = prev[0] - prev_prev[0]
        dy1 = prev[1] - prev_prev[1]
        dx2 = curr[0] - prev[0]
        dy2 = curr[1] - prev[1]
        
        # If both horizontal or both vertical, combine
        if (np.isclose(dy1, 0) and np.isclose(dy2, 0)) or (np.isclose(dx1, 0) and np.isclose(dx2, 0)):
            # Same direction, replace prev with curr
            final[-1] = curr
        else:
            final.append(curr)
    
    # Fourth pass: remove very short zigzag sequences (especially at start/end)
    # These occur when A* path goes slightly past the target then backtracks
    min_zigzag_length = min_segment_length * 2
    
    changed = True
    while changed and len(final) > 3:
        changed = False
        
        # Check first few segments
        if len(final) > 3:
            # Check if segments 0->1 and 1->2 are both very short
            seg1_len = max(abs(final[1][0] - final[0][0]), abs(final[1][1] - final[0][1]))
            seg2_len = max(abs(final[2][0] - final[1][0]), abs(final[2][1] - final[1][1]))
            
            if seg1_len < min_zigzag_length and seg2_len < min_zigzag_length:
                # Try to skip the intermediate point
                # Check if we can go directly from start to point 2 via Manhattan
                start = final[0]
                target = final[2]
                if np.isclose(start[0], target[0]) or np.isclose(start[1], target[1]):
                    # Can go directly
                    final.pop(1)
                    changed = True
        
        # Check last few segments
        if len(final) > 3 and not changed:
            seg_m1_len = max(abs(final[-1][0] - final[-2][0]), abs(final[-1][1] - final[-2][1]))
            seg_m2_len = max(abs(final[-2][0] - final[-3][0]), abs(final[-2][1] - final[-3][1]))
            
            if seg_m1_len < min_zigzag_length and seg_m2_len < min_zigzag_length:
                target = final[-1]
                from_pt = final[-3]
                if np.isclose(from_pt[0], target[0]) or np.isclose(from_pt[1], target[1]):
                    final.pop(-2)
                    changed = True
    
    return final



def route_astar(
    component: Component,
    port1: Port | list[Port],
    port2: Port | list[Port],
    resolution: float = 0.5,
    avoid_layers: Sequence[LayerSpec] | None = None,
    distance: float = 1,
    cross_section: CrossSectionSpec = "strip",
    bend: ComponentSpec = gf.components.bend_euler,
    straight: ComponentSpec = "straight",
    avoid_same_layer: bool = False,
    **kwargs: Any,
) -> Route:
    """Route A* with support for list of ports, sequential avoidance, and port exclusion zones.
    
    Args:
        component: Component to route within.
        port1: Source port(s).
        port2: Destination port(s).
        resolution: Grid resolution in um.
        avoid_layers: Additional layers to treat as obstacles.
        distance: Clearance distance from obstacles in um.
        cross_section: Cross-section specification for routes.
        bend: Bend component to use.
        straight: Straight component to use.
        avoid_same_layer: If True, automatically avoid existing geometry on the routing layer.
        **kwargs: Additional arguments for cross-section.
        
    Returns:
        Route object containing references, length, and ports.
    """
    # Normalize to lists
    if isinstance(port1, list):
        if not isinstance(port2, list) or len(port1) != len(port2):
            raise ValueError("If port1 is a list, port2 must be a list of the same length.")
    else:
        port1 = [port1]
        port2 = [port2]

    # Initialize accumulation
    references = []
    length = 0.0
    length_effective = 0.0
    ports = []
    
    # Get cross-section to determine routing layer
    cross_section_obj = gf.get_cross_section(cross_section, **kwargs)
    width = cross_section_obj.width
    radius = cross_section_obj.radius if cross_section_obj.radius else 0.0
    
    # Determine routing layer from cross-section
    routing_layer = None
    if hasattr(cross_section_obj, 'layer'):
        routing_layer = cross_section_obj.layer
    elif hasattr(cross_section_obj, 'sections') and cross_section_obj.sections:
        routing_layer = cross_section_obj.sections[0].layer
    
    # Build complete avoid_layers list
    all_avoid_layers = list(avoid_layers) if avoid_layers else []
    
    # Generate initial obstacle grid
    # IMPORTANT: Pass empty list [] instead of None to avoid blocking all device bboxes
    grid_static, x, y = _generate_grid(component, resolution, all_avoid_layers, distance)

    
    # Dynamic grid for tracking previously routed paths
    grid_dynamic = np.zeros_like(grid_static)
    
    # Ensure 1D coordinate arrays
    if x.ndim == 2:
        x_vals = x[0, :]
        y_vals = y[:, 0]
    else:
        x_vals = x
        y_vals = y

    # If avoid_same_layer, mark existing routing layer geometry as obstacles
    # NOTE: This is disabled by default because blocking all same-layer geometry
    # prevents routing between devices. Sequential route avoidance is handled
    # via grid_dynamic which tracks previously routed paths.
    # Set avoid_same_layer=True only if you need to avoid existing metal geometry
    # that is NOT device ports (e.g., power rails, other pre-existing routes).
    if avoid_same_layer and routing_layer is not None:
        _mark_layer_obstacles(grid_static, component, routing_layer, x_vals, y_vals, resolution, distance)


    def get_index(val: float, array: np.ndarray) -> int:
        """Convert um coordinate to grid index."""
        idx = int(round((val - array.min()) / resolution))
        return max(0, min(len(array) - 1, idx))

    # Port exclusion radius: ensure we can reach ports even if they're in obstacle areas
    # Use 5um minimum to cover typical device widths when avoiding same-layer geometry
    port_exclusion_um = 5.0 if avoid_same_layer else (width + distance)
    port_exclusion_radius = max(3, int(np.ceil(port_exclusion_um / resolution)))

    
    # Minimum segment length for simplification
    min_segment_length = max(resolution * 2, width * 2)
    
    for route_idx, (p1, p2) in enumerate(zip(port1, port2)):
        # Create working copy of static grid for this route
        grid_working = grid_static.copy()
        
        # Get port positions in um
        port1x = p1.x / 1000
        port1y = p1.y / 1000
        port2x = p2.x / 1000
        port2y = p2.y / 1000
        
        # Get port grid indices
        p1_ix = get_index(port1x, x_vals)
        p1_iy = get_index(port1y, y_vals)
        p2_ix = get_index(port2x, x_vals)
        p2_iy = get_index(port2y, y_vals)
        
        # Create port exclusion zones - unblock areas around ports
        for (px, py) in [(p1_ix, p1_iy), (p2_ix, p2_iy)]:
            for di in range(-port_exclusion_radius, port_exclusion_radius + 1):
                for dj in range(-port_exclusion_radius, port_exclusion_radius + 1):
                    ni, nj = px + di, py + dj
                    if 0 <= ni < grid_working.shape[0] and 0 <= nj < grid_working.shape[1]:
                        grid_working[ni, nj] = 0
        
        # Build navigation graph
        G = nx.grid_2d_graph(len(x_vals), len(y_vals))
        
        # Remove obstacle nodes
        nodes_to_remove = []
        for i in range(len(x_vals)):
            for j in range(len(y_vals)):
                if grid_working[i, j] == 1 or grid_dynamic[i, j] == 1:
                    nodes_to_remove.append((i, j))
        G.remove_nodes_from(nodes_to_remove)
        
        # Get start/end nodes
        start_node = (p1_ix, p1_iy)
        end_node = (p2_ix, p2_iy)
        
        # Verify nodes exist in graph
        if start_node not in G:
            valid_nodes = sorted(G.nodes)
            if not valid_nodes:
                print(f"WARNING: No valid nodes in graph for route {route_idx}")
                continue
            start_node = min(
                valid_nodes,
                key=lambda n: (np.sqrt((n[0] - p1_ix)**2 + (n[1] - p1_iy)**2), n[0], n[1])
            )
            
        if end_node not in G:
            valid_nodes = sorted(G.nodes)
            if not valid_nodes:
                print(f"WARNING: No valid nodes in graph for route {route_idx}")
                continue
            end_node = min(
                valid_nodes,
                key=lambda n: (np.sqrt((n[0] - p2_ix)**2 + (n[1] - p2_iy)**2), n[0], n[1])
            )
        
        # A* heuristic (Manhattan distance)
        def heuristic(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])
        
        # Find path
        try:
            path = nx.astar_path(G, start_node, end_node, heuristic=heuristic)
        except nx.NetworkXNoPath:
            print(f"WARNING: No path found for route {route_idx}: {p1.name} -> {p2.name}")
            continue
        except Exception as e:
            print(f"WARNING: Path finding failed for route {route_idx}: {e}")
            continue
        
        # Convert path to waypoints (in um) - only keep turning points
        raw_path = [[x_vals[i], y_vals[j]] for i, j in path]
        
        # Extract only the turning points from the path
        if len(raw_path) <= 2:
            waypoints_grid = raw_path
        else:
            waypoints_grid = [raw_path[0]]
            for i in range(1, len(raw_path) - 1):
                prev = raw_path[i - 1]
                curr = raw_path[i]
                next_pt = raw_path[i + 1]
                
                # Check if this is a turning point (direction change)
                dx1 = curr[0] - prev[0]
                dy1 = curr[1] - prev[1]
                dx2 = next_pt[0] - curr[0]
                dy2 = next_pt[1] - curr[1]
                
                # Direction changes when one axis switches from moving to static or vice versa
                is_turn = (np.isclose(dx1, 0) != np.isclose(dx2, 0)) or (np.isclose(dy1, 0) != np.isclose(dy2, 0))
                
                if is_turn:
                    waypoints_grid.append(curr)
            
            waypoints_grid.append(raw_path[-1])
        
        # Ensure minimum standoff from ports - INSERT new waypoints if needed
        # This is critical because grid paths often don't align with port orientations
        min_standoff_um = max(1.5, width * 2)  # At least 1.5um or 2x wire width
        
        # Get port orientations
        angle1 = p1.orientation if p1.orientation is not None else 0
        angle2 = p2.orientation if p2.orientation is not None else 0
        
        # Port facing direction vectors
        # 0° = facing right (+x), 90° = facing up (+y), 180° = left, 270° = down
        import math
        def port_facing_direction(angle):
            rad = math.radians(angle)
            dx = math.cos(rad)
            dy = math.sin(rad)
            # Snap to cardinal direction
            if abs(dx) > abs(dy):
                return (1 if dx > 0 else -1, 0)
            else:
                return (0, 1 if dy > 0 else -1)
        
        dir1 = port_facing_direction(angle1)
        dir2 = port_facing_direction(angle2)
        
        # Create standoff point for port1 - always insert at start
        standoff1_x = port1x + dir1[0] * min_standoff_um
        standoff1_y = port1y + dir1[1] * min_standoff_um
        
        # Create standoff point for port2 - always insert at end
        standoff2_x = port2x + dir2[0] * min_standoff_um
        standoff2_y = port2y + dir2[1] * min_standoff_um
        
        # Build new waypoints list with standoffs
        # Structure: port1 -> standoff1 -> grid path -> standoff2 -> port2
        new_waypoints_grid = [[standoff1_x, standoff1_y]]
        
        # Check if we can skip grid waypoints and use a direct route
        # This is the case when there are no obstacles to avoid
        # Direct route is possible if standoff1 and standoff2 can be connected simply
        use_direct_route = True
        
        # Only use direct route if standoff points are far enough apart
        standoff_dist = abs(standoff1_x - standoff2_x) + abs(standoff1_y - standoff2_y)
        if standoff_dist > 2 * min_standoff_um:
            # Check if grid path has any significant waypoints (turns around obstacles)
            # If all grid waypoints are near the standoff points, we can use direct route
            significant_waypoints = []
            for wp in waypoints_grid:
                dist1 = max(abs(wp[0] - standoff1_x), abs(wp[1] - standoff1_y))
                dist2 = max(abs(wp[0] - standoff2_x), abs(wp[1] - standoff2_y))
                # Keep waypoints that are far from both standoffs
                if dist1 >= min_standoff_um * 2 and dist2 >= min_standoff_um * 2:
                    significant_waypoints.append(wp)
            
            if len(significant_waypoints) > 0:
                # There are obstacles - use grid path
                use_direct_route = False
                for wp in significant_waypoints:
                    new_waypoints_grid.append(wp)
        
        # Add standoff2 at end
        new_waypoints_grid.append([standoff2_x, standoff2_y])
        
        waypoints_grid = new_waypoints_grid


        
        # Now build final waypoints: port1 -> path -> port2
        # with proper Manhattan connections
        final_waypoints = [[port1x, port1y]]
        
        for wp in waypoints_grid:
            last = final_waypoints[-1]
            
            # Skip if same position
            if np.isclose(last[0], wp[0]) and np.isclose(last[1], wp[1]):
                continue
            
            # Ensure Manhattan: add intermediate if diagonal
            if not np.isclose(last[0], wp[0]) and not np.isclose(last[1], wp[1]):
                # Check port orientation for first segment
                if len(final_waypoints) == 1:
                    # First segment - respect port1 orientation
                    angle1 = p1.orientation if p1.orientation is not None else 0
                    if abs(angle1 - 90) < 45 or abs(angle1 - 270) < 45:
                        # Port faces vertical - go vertical first
                        final_waypoints.append([last[0], wp[1]])
                    else:
                        # Port faces horizontal - go horizontal first
                        final_waypoints.append([wp[0], last[1]])
                else:
                    # Default: horizontal then vertical
                    final_waypoints.append([wp[0], last[1]])
            
            final_waypoints.append(wp)
        
        # Add port2 with proper connection
        last = final_waypoints[-1]
        if not (np.isclose(last[0], port2x) and np.isclose(last[1], port2y)):
            if not np.isclose(last[0], port2x) and not np.isclose(last[1], port2y):
                # Need intermediate - use port2 orientation
                angle2 = p2.orientation if p2.orientation is not None else 0
                if abs(angle2 - 90) < 45 or abs(angle2 - 270) < 45:
                    # Port faces vertical - arrive vertically
                    final_waypoints.append([port2x, last[1]])
                else:
                    # Port faces horizontal - arrive horizontally
                    final_waypoints.append([last[0], port2y])
            final_waypoints.append([port2x, port2y])
        
        # Apply final simplification
        cleaned_waypoints = _simplify_manhattan_path(final_waypoints, min_segment_length)
        
        # Additional cleanup: ensure minimum distance from ports for proper bend placement
        # Remove points that are too close to start/end ports but maintain Manhattan routing
        min_standoff = max(2.0, width * 3)  # 2um minimum standoff
        
        if len(cleaned_waypoints) > 3:
            # Check first waypoint after start - but keep Manhattan structure
            wp = cleaned_waypoints[1]
            dx = abs(wp[0] - port1x)
            dy = abs(wp[1] - port1y)
            dist = max(dx, dy)
            if dist < min_standoff and len(cleaned_waypoints) > 3:
                # Replace with a point that maintains Manhattan routing
                wp_next = cleaned_waypoints[2]
                if np.isclose(wp[0], wp_next[0]):
                    # Vertical segment follows - keep x, move closer to next y
                    cleaned_waypoints[1] = [wp[0], port1y]
                elif np.isclose(wp[1], wp_next[1]):
                    # Horizontal segment follows - keep y, move closer to next x
                    cleaned_waypoints[1] = [port1x, wp[1]]
            
            # Check last waypoint before end
            wp = cleaned_waypoints[-2]
            dx = abs(wp[0] - port2x)
            dy = abs(wp[1] - port2y)
            dist = max(dx, dy)
            if dist < min_standoff and len(cleaned_waypoints) > 3:
                wp_prev = cleaned_waypoints[-3]
                if np.isclose(wp[0], wp_prev[0]):
                    # Vertical segment precedes
                    cleaned_waypoints[-2] = [wp[0], port2y]
                elif np.isclose(wp[1], wp_prev[1]):
                    # Horizontal segment precedes
                    cleaned_waypoints[-2] = [port2x, wp[1]]
        
        # Ensure we have at least a valid 2-point path
        if len(cleaned_waypoints) < 2:
            cleaned_waypoints = [[port1x, port1y], [port2x, port2y]]
        
        # Final Manhattan validation - ensure all segments are orthogonal
        valid_waypoints = [cleaned_waypoints[0]]
        for i in range(1, len(cleaned_waypoints)):
            prev = valid_waypoints[-1]
            curr = cleaned_waypoints[i]
            
            if not np.isclose(prev[0], curr[0]) and not np.isclose(prev[1], curr[1]):
                # Diagonal - insert intermediate
                valid_waypoints.append([curr[0], prev[1]])
            
            valid_waypoints.append(curr)
        
        cleaned_waypoints = valid_waypoints
        
        # For very close ports, just use direct connection
        port_dist = abs(port1x - port2x) + abs(port1y - port2y)
        if port_dist < min_standoff:
            # Just connect directly - let route_single handle it
            if np.isclose(port1x, port2x) or np.isclose(port1y, port2y):
                # Already Manhattan
                cleaned_waypoints = [[port1x, port1y], [port2x, port2y]]
            else:
                # Need intermediate
                cleaned_waypoints = [[port1x, port1y], [port2x, port1y], [port2x, port2y]]
        
        # Convert to DBU points
        final_points_dbu = [kdb.Point(int(round(pt[0] * 1000)), int(round(pt[1] * 1000))) for pt in cleaned_waypoints]
        
        # Remove duplicate DBU points
        final_points = [final_points_dbu[0]]
        for pt in final_points_dbu[1:]:
            if pt != final_points[-1]:
                final_points.append(pt)
        
        # Aggressive short segment removal - route_single fails with segments under ~500nm
        min_segment_dbu = 1000  # 1um minimum segment length in DBU (nm)
        
        def is_manhattan(p1, p2):
            return p1.x == p2.x or p1.y == p2.y
        
        # Remove short segments - only if result is still Manhattan
        # Single pass to avoid infinite loop
        i = 1
        while i < len(final_points) - 1 and len(final_points) > 2:
            prev_pt = final_points[i - 1]
            curr_pt = final_points[i]
            next_pt = final_points[i + 1]
            
            # Calculate segment length from prev to curr
            seg_len = max(abs(curr_pt.x - prev_pt.x), abs(curr_pt.y - prev_pt.y))
            
            if seg_len < min_segment_dbu:
                # Try to remove this point if result is Manhattan
                if is_manhattan(prev_pt, next_pt):
                    final_points.pop(i)
                    # Don't increment i - check the new point at this index
                    continue
            i += 1
        
        # Check last segment - if too short, try to fix
        if len(final_points) > 2:
            seg_len = max(abs(final_points[-1].x - final_points[-2].x), 
                         abs(final_points[-1].y - final_points[-2].y))
            if seg_len < min_segment_dbu:
                # Try removing second-to-last if result is Manhattan
                prev_pt = final_points[-3] if len(final_points) > 2 else final_points[0]
                end_pt = final_points[-1]
                if is_manhattan(prev_pt, end_pt):
                    final_points.pop(-2)

        
        # Ensure exact port positions
        if final_points:
            final_points[0] = kdb.Point(p1.x, p1.y)
            final_points[-1] = kdb.Point(p2.x, p2.y)
        else:
            final_points = [kdb.Point(p1.x, p1.y), kdb.Point(p2.x, p2.y)]





        # Mark path nodes as occupied for subsequent routes
        # Use wider buffer for better spacing
        spacing_radius = max(2, int(np.ceil((width + distance) / resolution)))
        for i, j in path:
            for di in range(-spacing_radius, spacing_radius + 1):
                for dj in range(-spacing_radius, spacing_radius + 1):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < grid_dynamic.shape[0] and 0 <= nj < grid_dynamic.shape[1]:
                        grid_dynamic[ni, nj] = 1

        # Create physical route
        def wire_corner_safe(**kw):
            kw.pop('radius', None)
            return gf.components.wire_corner(**kw)

        # Filter kwargs for route_single
        rs_kwargs = kwargs.copy()
        rs_kwargs.pop('radius', None)

        # Detect electrical routing
        is_electrical = False
        if hasattr(cross_section_obj, "sections") and cross_section_obj.sections:
            if cross_section_obj.sections[0].port_types:
                if "electrical" in cross_section_obj.sections[0].port_types:
                    is_electrical = True
        
        bend_component = wire_corner_safe if is_electrical else bend

        try:
            # Convert kdb.Point to tuples for gdsfactory compatibility (coordinates in nm -> um)
            waypoints_um = [(pt.x / 1000, pt.y / 1000) for pt in final_points]
            
            r = gf.routing.route_single(
                component=component,
                port1=p1,
                port2=p2,
                waypoints=waypoints_um,
                cross_section=cross_section,
                bend=bend_component,
                straight=straight,
                port_type="electrical" if is_electrical else None,
                **rs_kwargs
            )
            
            if hasattr(r, 'references'):
                references.extend(r.references)
            elif hasattr(r, 'instances'):
                references.extend(r.instances)
                
            if hasattr(r, 'length'):
                length += r.length
            if hasattr(r, 'ports'):
                ports.extend(r.ports)
                
        except Exception as e:
            print(f"WARNING: route_single failed for route {route_idx}: {e}")
            continue

    return Route(references, length, length_effective, ports)
