"""Utilities for multi-layer routing using doroutes A* pathfinding."""

from dataclasses import dataclass
from itertools import permutations
from functools import partial
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import LayerSpec, Port
import numpy as np

#from doroutes import find_route_astar
from sky130.pcells.vias import via_m1_m2


# Layer definitions for Sky130
LAYER_M1 = (68, 20)  # Metal 1 - Horizontal
LAYER_M2 = (69, 20)  # Metal 2 - Vertical

_DRC = {
    "min_width": {
        LAYER_M1: 0.14,
        LAYER_M2: 0.14,
    },
    "min_via_pad": {
        LAYER_M1: 0.29,
        LAYER_M2: 0.29,
    },
    # via_m1_m2 draws landing metals as (width + enclosure) on M1/M2.
    "via_metal_enclosure_add": 0.07,
}


@dataclass
class PortGeometry:
    width_x: float
    width_y: float
    exit_dir: str
    bbox_dbu: Optional[Tuple[int, int, int, int]]
    dev_center_dbu: Optional[Tuple[int, int]]
    layer_tuple: Optional[Tuple[int, int]]
    below_cut_count: int

    @property
    def width_along(self) -> float:
        return self.width_y if self.exit_dir == "h" else self.width_x

    @property
    def width_across(self) -> float:
        return self.width_x if self.exit_dir == "h" else self.width_y


@dataclass(frozen=True)
class RouteNetSpec:
    """Single-net specification for deterministic multi-net routing."""

    name: str
    start: Port
    stop: Port
    port_name_prefix: str = "seg"


def _deterministic_clearance_attempts(
    clearance: float,
    clearance_ladder: Tuple[float, ...],
) -> List[float]:
    """Return deterministic clearance attempts: requested first, then ladder order."""
    attempts: List[float] = []
    if clearance > 0:
        attempts.append(float(clearance))
    for c in clearance_ladder:
        c = float(c)
        if c > 0 and c not in attempts:
            attempts.append(c)
    return attempts


def _bbox_overlap(a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]) -> bool:
    """Axis-aligned bbox overlap check."""
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return ax0 < bx1 and ax1 > bx0 and ay0 < by1 and ay1 > by0


def _segment_envelope_um(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    width_um: float,
) -> Tuple[float, float, float, float]:
    """Conservative rectangular envelope for a segment with finite width."""
    half = max(0.0, width_um / 2.0)
    x0, y0 = p1
    x1, y1 = p2
    return (min(x0, x1) - half, min(y0, y1) - half, max(x0, x1) + half, max(y0, y1) + half)


def _rect_envelope_um(
    center: Tuple[float, float],
    width_um: float,
    height_um: float,
) -> Tuple[float, float, float, float]:
    """Rectangular envelope from center and explicit width/height."""
    x, y = center
    return (x - width_um / 2.0, y - height_um / 2.0, x + width_um / 2.0, y + height_um / 2.0)


def _via_envelope_um(
    center: Tuple[float, float],
    pad_w_um: float,
    pad_h_um: float,
) -> Tuple[float, float, float, float]:
    """Rectangular via envelope from center and pad dimensions."""
    x, y = center
    return (x - pad_w_um / 2.0, y - pad_h_um / 2.0, x + pad_w_um / 2.0, y + pad_h_um / 2.0)


def _via_pad_size_um(width_um: float) -> float:
    """Square via pad size used for M1<->M2 transitions."""
    return max(width_um, _DRC["min_via_pad"][LAYER_M1], _DRC["min_via_pad"][LAYER_M2])


def _via_metal_footprint_um(via_pad_um: float) -> float:
    """Actual M1/M2 square metal footprint produced by via_m1_m2."""
    return via_pad_um + float(_DRC["via_metal_enclosure_add"])


def _is_via_legal_on_both_layers(
    center_um: Tuple[float, float],
    via_pad_um: float,
    m1_bboxes: List[Tuple[float, float, float, float]],
    m2_bboxes: List[Tuple[float, float, float, float]],
) -> bool:
    """True if via envelope at center is clear on both adjacent routing layers."""
    via_metal = _via_metal_footprint_um(via_pad_um)
    via_box = _via_envelope_um(center_um, via_metal, via_metal)
    if any(_bbox_overlap(via_box, obox) for obox in m1_bboxes):
        return False
    if any(_bbox_overlap(via_box, obox) for obox in m2_bboxes):
        return False
    return True


def _deterministic_via_candidate_centers(
    base_center_um: Tuple[float, float],
    step_um: float,
    radius_um: float,
    max_candidates: int,
    dbu: float,
) -> List[Tuple[float, float]]:
    """Generate stable nearby via centers around base point, snapped to DBU."""
    step = max(step_um, dbu)
    max_ring = max(0, int(round(radius_um / step)))
    centers: List[Tuple[float, float]] = []
    seen = set()

    def _append(center: Tuple[float, float]) -> None:
        key = (int(round(center[0] / dbu)), int(round(center[1] / dbu)))
        if key in seen:
            return
        seen.add(key)
        centers.append((key[0] * dbu, key[1] * dbu))

    _append(base_center_um)
    if len(centers) >= max_candidates:
        return centers

    for md in range(1, max_ring + 1):
        offsets = []
        for ix in range(-md, md + 1):
            iy_abs = md - abs(ix)
            if iy_abs == 0:
                offsets.append((ix, 0))
            else:
                offsets.append((ix, iy_abs))
                offsets.append((ix, -iy_abs))
        offsets = sorted(
            set(offsets),
            key=lambda p: (
                0 if (p[0] == 0 or p[1] == 0) else 1,
                0 if (p[0] > 0 and p[1] == 0) else 1 if (p[0] == 0 and p[1] > 0) else 2 if (p[0] < 0 and p[1] == 0) else 3 if (p[0] == 0 and p[1] < 0) else 4 if (p[0] > 0 and p[1] > 0) else 5 if (p[0] < 0 and p[1] > 0) else 6 if (p[0] < 0 and p[1] < 0) else 7,
                abs(p[1]),
                abs(p[0]),
            ),
        )
        for ix, iy in offsets:
            _append((base_center_um[0] + ix * step, base_center_um[1] + iy * step))
            if len(centers) >= max_candidates:
                return centers

    return centers


def _resolve_legal_via_center(
    base_center_um: Tuple[float, float],
    via_pad_um: float,
    m1_bboxes: List[Tuple[float, float, float, float]],
    m2_bboxes: List[Tuple[float, float, float, float]],
    dbu: float,
    relocate_step_um: float = 0.14,
    relocate_radius_um: float = 1.0,
    max_candidates: int = 64,
    allow_relocate: bool = True,
) -> Optional[Tuple[float, float]]:
    """Return first legal via center (base first), else None."""
    if not allow_relocate:
        return (
            base_center_um
            if _is_via_legal_on_both_layers(base_center_um, via_pad_um, m1_bboxes, m2_bboxes)
            else None
        )
    for center in _deterministic_via_candidate_centers(
        base_center_um,
        step_um=relocate_step_um,
        radius_um=relocate_radius_um,
        max_candidates=max_candidates,
        dbu=dbu,
    ):
        if _is_via_legal_on_both_layers(center, via_pad_um, m1_bboxes, m2_bboxes):
            return center
    return None


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
    buffer_dbu: int = 0,
):
    """Extract obstruction polygons from specified layers.
    
    Args:
        kc: KCell to extract polygons from.
        layers: List of (layer, datatype) tuples to extract.
        dbu: Database unit.
        port_points: Optional list of (x_dbu, y_dbu) port positions.
                    ONLY polygons containing these exact points are excluded.
                    All other polygons are hard obstructions - router must go around.
        buffer_dbu: Optional obstruction inflation in DBU.
    
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
    
    # Convert remaining polygons to region, optionally inflating by clearance.
    obstruction_region = kdb.Region()
    for i, poly in enumerate(all_polys):
        if i not in excluded_indices:
            obstruction_region.insert(poly)

    if buffer_dbu > 0:
        obstruction_region = obstruction_region.sized(buffer_dbu)

    polys = []
    for poly in obstruction_region.each():
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


def _below_cut_layer_for_metal(layer_tuple: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    """Return immediate below-metal cut layer for a routed metal layer."""
    mapping = {
        LAYER_M1: (67, 44),  # mcon under M1
        LAYER_M2: (68, 44),  # via1 under M2
    }
    return mapping.get(layer_tuple)


def _count_below_port_cuts(kc, port_poly, layer_tuple: Optional[Tuple[int, int]]) -> int:
    """Count lower-cut shapes whose centers are inside the selected port polygon."""
    from kfactory import kdb

    if layer_tuple is None:
        return 0
    cut_layer = _below_cut_layer_for_metal(layer_tuple)
    if cut_layer is None:
        return 0

    cut_idx = kc.kcl.layer(*cut_layer)
    cut_region = kdb.Region(kc.begin_shapes_rec(cut_idx))
    count = 0
    for cut in cut_region.each():
        bbox = cut.bbox()
        center = kdb.Point((bbox.left + bbox.right) // 2, (bbox.bottom + bbox.top) // 2)
        if port_poly.inside(center):
            count += 1
    return count


def _fanout_hops_from_cut_count(cut_count: int) -> int:
    """Deterministic width-fanout horizon from below-cut density."""
    if cut_count <= 1:
        return 0
    if cut_count <= 3:
        return 1
    if cut_count <= 6:
        return 2
    return 3


def _segment_direction_width(port_geom: PortGeometry, is_horizontal: bool, fallback: float) -> float:
    """Port-side snapped width for a segment direction."""
    raw = port_geom.width_y if is_horizontal else port_geom.width_x
    return max(float(_DRC["min_width"][LAYER_M1]), fallback, raw)


def _selected_straight_width(
    start_geom: PortGeometry,
    stop_geom: PortGeometry,
    fallback_width: float,
) -> float:
    """Select route width from the smaller port polygon's longer edge."""
    area_start = float(start_geom.width_x * start_geom.width_y)
    area_stop = float(stop_geom.width_x * stop_geom.width_y)
    selected = start_geom if area_start <= area_stop else stop_geom
    candidate = max(float(selected.width_x), float(selected.width_y))
    _ = fallback_width  # retained for call-site compatibility
    return max(float(_DRC["min_width"][LAYER_M1]), candidate)


def _selected_polygon_meta(start_geom: PortGeometry, stop_geom: PortGeometry) -> Tuple[str, str]:
    """Return selected endpoint ('start'|'stop') and its longer-side axis ('h'|'v')."""
    area_start = float(start_geom.width_x * start_geom.width_y)
    area_stop = float(stop_geom.width_x * stop_geom.width_y)
    selected = "start" if area_start <= area_stop else "stop"  # source tie-break
    geom = start_geom if selected == "start" else stop_geom
    axis = "h" if geom.width_y >= geom.width_x else "v"
    return selected, axis


def _first_same_layer_segment_idx(corners_3d: List[Tuple[int, int, int]]) -> Optional[Tuple[int, int]]:
    for i in range(len(corners_3d) - 1):
        x0, y0, z0 = corners_3d[i]
        x1, y1, z1 = corners_3d[i + 1]
        if z0 == z1 and (x0 != x1 or y0 != y1):
            return (i, i + 1)
    return None


def _last_same_layer_segment_idx(corners_3d: List[Tuple[int, int, int]]) -> Optional[Tuple[int, int]]:
    for i in range(len(corners_3d) - 2, -1, -1):
        x0, y0, z0 = corners_3d[i]
        x1, y1, z1 = corners_3d[i + 1]
        if z0 == z1 and (x0 != x1 or y0 != y1):
            return (i, i + 1)
    return None


def _has_local_backtrack_corners(corners_3d: List[Tuple[int, int, int]]) -> bool:
    """Detect immediate A->B->A position reversals."""
    if len(corners_3d) < 3:
        return False
    for i in range(1, len(corners_3d) - 1):
        a = corners_3d[i - 1]
        b = corners_3d[i]
        c = corners_3d[i + 1]
        if a[0] == c[0] and a[1] == c[1] and not (a[0] == b[0] and a[1] == b[1]):
            return True
    return False


def _has_local_backtrack_path(path: List[Tuple[float, float]], tol: float = 1e-6) -> bool:
    """Detect immediate A->B->A position reversals in 2D path."""
    if len(path) < 3:
        return False
    for i in range(1, len(path) - 1):
        a = path[i - 1]
        b = path[i]
        c = path[i + 1]
        if abs(a[0] - c[0]) <= tol and abs(a[1] - c[1]) <= tol:
            if abs(a[0] - b[0]) > tol or abs(a[1] - b[1]) > tol:
                return True
    return False


def _enforce_axis_on_corners_endpoint(
    corners_3d: List[Tuple[int, int, int]],
    endpoint: str,
    axis: str,
    jog_dbu: int = 1,
    mode: str = "hard",
) -> bool:
    """Ensure first/last same-layer segment matches required axis via local jog insertion."""
    if len(corners_3d) < 2:
        return False

    pair = _first_same_layer_segment_idx(corners_3d) if endpoint == "start" else _last_same_layer_segment_idx(corners_3d)
    if pair is None:
        return False
    i, j = pair
    p0 = corners_3d[i]
    p1 = corners_3d[j]
    is_h = p0[1] == p1[1]
    if (axis == "h" and is_h) or (axis == "v" and not is_h):
        return False

    original = list(corners_3d)
    if endpoint == "start":
        if axis == "h":
            xj = p1[0] if p1[0] != p0[0] else p0[0] + jog_dbu
            jog = (xj, p0[1], p0[2])
        else:
            yj = p1[1] if p1[1] != p0[1] else p0[1] + jog_dbu
            jog = (p0[0], yj, p0[2])
        corners_3d.insert(j, jog)
    else:
        if axis == "h":
            xj = p0[0] if p0[0] != p1[0] else p1[0] - jog_dbu
            jog = (xj, p1[1], p1[2])
        else:
            yj = p0[1] if p0[1] != p1[1] else p1[1] - jog_dbu
            jog = (p1[0], yj, p1[2])
        corners_3d.insert(j, jog)
    if _has_local_backtrack_corners(corners_3d):
        corners_3d[:] = original
        return False
    if mode == "prefer":
        # Prefer mode is best-effort only; keep original if still misaligned.
        pair2 = _first_same_layer_segment_idx(corners_3d) if endpoint == "start" else _last_same_layer_segment_idx(corners_3d)
        if pair2 is None:
            corners_3d[:] = original
            return False
        q0 = corners_3d[pair2[0]]
        q1 = corners_3d[pair2[1]]
        q_is_h = q0[1] == q1[1]
        if not ((axis == "h" and q_is_h) or (axis == "v" and not q_is_h)):
            corners_3d[:] = original
            return False
    return True


def _enforce_axis_on_path_endpoint(
    path: List[Tuple[float, float]],
    endpoint: str,
    axis: str,
    jog_um: float = 0.001,
    mode: str = "hard",
) -> bool:
    """Ensure first/last path segment matches required axis via local jog insertion."""
    if len(path) < 2:
        return False
    if endpoint == "start":
        p0 = path[0]
        p1 = path[1]
        is_h = abs(p1[1] - p0[1]) < 0.001
        if (axis == "h" and is_h) or (axis == "v" and not is_h):
            return False
        original = list(path)
        if axis == "h":
            xj = p1[0] if abs(p1[0] - p0[0]) > 0.001 else p0[0] + jog_um
            path.insert(1, (xj, p0[1]))
        else:
            yj = p1[1] if abs(p1[1] - p0[1]) > 0.001 else p0[1] + jog_um
            path.insert(1, (p0[0], yj))
        if _has_local_backtrack_path(path):
            path[:] = original
            return False
        return True

    p0 = path[-2]
    p1 = path[-1]
    is_h = abs(p1[1] - p0[1]) < 0.001
    if (axis == "h" and is_h) or (axis == "v" and not is_h):
        return False
    original = list(path)
    if axis == "h":
        xj = p0[0] if abs(p0[0] - p1[0]) > 0.001 else p1[0] - jog_um
        path.insert(len(path) - 1, (xj, p1[1]))
    else:
        yj = p0[1] if abs(p0[1] - p1[1]) > 0.001 else p1[1] - jog_um
        path.insert(len(path) - 1, (p1[0], yj))
    if _has_local_backtrack_path(path):
        path[:] = original
        return False
    return True


def _build_segment_widths_dynamic(
    corners_3d: List[Tuple[int, int, int]],
    start_geom: PortGeometry,
    stop_geom: PortGeometry,
    body_width: float,
    fallback_width: float,
    dynamic_width: bool,
) -> List[float]:
    """Compute per-segment widths using selected-port uniform straight width."""
    n_segs = len(corners_3d) - 1 if len(corners_3d) >= 2 else 0
    if n_segs <= 0:
        return []
    if not dynamic_width:
        return [fallback_width] * n_segs

    _ = body_width  # kept for call-site compatibility
    uniform_w = _selected_straight_width(start_geom, stop_geom, fallback_width)
    return [uniform_w] * n_segs


def _build_corner_patches_from_segments(
    plan_segments: List[Tuple[Tuple[float, float], Tuple[float, float], Tuple[int, int], float]],
) -> List[Tuple[Tuple[float, float], Tuple[int, int], float, float]]:
    """Build anisotropic corner patches from adjacent straight segments.

    Patch width follows horizontal segment width(s) and patch height follows
    vertical segment width(s) at each same-layer segment junction.
    """
    endpoint_map: Dict[Tuple[float, float, Tuple[int, int]], List[Tuple[bool, float]]] = {}
    for p0, p1, layer, seg_w in plan_segments:
        is_h = abs(p1[1] - p0[1]) < 0.001
        key0 = (p0[0], p0[1], layer)
        key1 = (p1[0], p1[1], layer)
        endpoint_map.setdefault(key0, []).append((is_h, seg_w))
        endpoint_map.setdefault(key1, []).append((is_h, seg_w))

    patches: List[Tuple[Tuple[float, float], Tuple[int, int], float, float]] = []
    for (x, y, layer), entries in endpoint_map.items():
        h_widths = [w for is_h, w in entries if is_h]
        v_widths = [w for is_h, w in entries if not is_h]
        if not h_widths or not v_widths:
            continue
        min_w = float(_DRC["min_width"][LAYER_M1 if layer == LAYER_M1 else LAYER_M2])
        patch_w = max(min_w, max(h_widths))
        patch_h = max(min_w, max(v_widths))
        patches.append(((x, y), layer, patch_w, patch_h))
    return patches


def _transition_target_via_width(
    corners_3d: List[Tuple[int, int, int]],
    seg_widths: List[float],
    transition_idx: int,
    fallback_width: float,
) -> float:
    """Target via-driving width from neighboring straight segments around a layer transition."""
    widths: List[float] = []
    n = len(seg_widths)
    for cand in (transition_idx - 1, transition_idx, transition_idx + 1):
        if 0 <= cand < n:
            widths.append(float(seg_widths[cand]))
    if not widths:
        widths.append(float(fallback_width))
    return max(widths)


def _via_pad_candidates(target_pad_um: float) -> List[float]:
    """Deterministic descending via-pad fallback ladder down to minimum legal pad."""
    min_pad = _via_pad_size_um(0.0)
    target = max(min_pad, float(target_pad_um))
    vals = [target]
    for scale in (0.85, 0.70, 0.55, 0.40, 0.25):
        vals.append(max(min_pad, target * scale))
    vals.append(min_pad)
    out: List[float] = []
    for v in sorted(vals, reverse=True):
        if not out or abs(v - out[-1]) > 1e-6:
            out.append(v)
    return out


def _get_port_geometry(
    port,
    kc,
    dbu: float,
    default_width: float = 0.25,
) -> PortGeometry:
    """Extract axis-aware port geometry from the containing metal polygon."""
    from kfactory import kdb

    px_dbu = int(port.dcenter[0] / dbu)
    py_dbu = int(port.dcenter[1] / dbu)
    port_point = kdb.Point(px_dbu, py_dbu)

    layer_tuple = None
    if hasattr(port, "layer"):
        info = kc.kcl.get_info(port.layer)
        layer_tuple = (info.layer, info.datatype)

    if layer_tuple is None:
        return PortGeometry(default_width, default_width, "o", None, None, None, 0)

    layer_idx = kc.kcl.layer(*layer_tuple)
    region = kdb.Region(kc.begin_shapes_rec(layer_idx))

    best_poly = None
    best_area = 0
    for poly in region.each():
        if poly.inside(port_point):
            area = poly.area()
            if area > best_area:
                best_area = area
                best_poly = poly

    if best_poly is None:
        return PortGeometry(default_width, default_width, "o", None, None, layer_tuple, 0)

    bbox = best_poly.bbox()
    x_extent_um = max(_DRC["min_width"][LAYER_M1], (bbox.right - bbox.left) * dbu)
    y_extent_um = max(_DRC["min_width"][LAYER_M1], (bbox.top - bbox.bottom) * dbu)
    exit_dir = "h" if y_extent_um >= x_extent_um else "v"
    bbox_dbu = (bbox.left, bbox.bottom, bbox.right, bbox.top)
    dev_center = ((bbox.left + bbox.right) // 2, (bbox.bottom + bbox.top) // 2)
    below_cut_count = _count_below_port_cuts(kc, best_poly, layer_tuple)

    return PortGeometry(
        width_x=x_extent_um,
        width_y=y_extent_um,
        exit_dir=exit_dir,
        bbox_dbu=bbox_dbu,
        dev_center_dbu=dev_center,
        layer_tuple=layer_tuple,
        below_cut_count=below_cut_count,
    )


def route_hierarchical_astar(
    c: Component,
    start: Port,
    stop: Port,
    global_grid_unit: float = 2.0,  # Coarse grid for global routing
    detail_grid_unit: float = 0.25,  # Fine grid for detailed routing
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    detail_margin: float = 5.0,  # Margin around corners for detail routing (um)
    clearance: float = 0.14,
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
        clearance: Minimum obstruction offset in um.
        
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
    buffer_dbu = int(round(max(0.0, clearance) / dbu))
    polys = _extract_polys_for_layers(kc, _layers, dbu, port_points, buffer_dbu=buffer_dbu)
    
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
            via_w = _via_pad_size_um(width)
            via = c.add_ref(via_m1_m2(width=via_w, length=via_w))
            via.dcenter = p_next
    
    return segment_ports


def _draw_dynamic_geometry_for_corners(
    c: Component,
    corners_3d: List[Tuple[int, int, int]],
    start_geom: PortGeometry,
    stop_geom: PortGeometry,
    body_width: float,
    width: float,
    dynamic_width: bool,
    m1_polys: List[np.ndarray],
    m2_polys: List[np.ndarray],
    start_xy_dbu: Tuple[int, int],
    stop_xy_dbu: Tuple[int, int],
    dbu: float,
    clearance: float,
    add_segment_ports: bool,
    port_name_prefix: str,
) -> Optional[List[Port]]:
    """Draw dynamic-width route geometry from layered corners.

    Returns:
        List of segment ports if drawing succeeds, otherwise None.
    """
    if len(corners_3d) < 2:
        return []

    seg_widths = _build_segment_widths_dynamic(
        corners_3d=corners_3d,
        start_geom=start_geom,
        stop_geom=stop_geom,
        body_width=body_width,
        fallback_width=width,
        dynamic_width=dynamic_width,
    )

    port_points_um = [(start_xy_dbu[0] * dbu, start_xy_dbu[1] * dbu), (stop_xy_dbu[0] * dbu, stop_xy_dbu[1] * dbu)]
    m1_bboxes = []
    m2_bboxes = []
    for poly in m1_polys:
        if len(poly) >= 3:
            box = (
                float(poly[:, 0].min()) * dbu,
                float(poly[:, 1].min()) * dbu,
                float(poly[:, 0].max()) * dbu,
                float(poly[:, 1].max()) * dbu,
            )
            if not any(box[0] <= px <= box[2] and box[1] <= py <= box[3] for px, py in port_points_um):
                m1_bboxes.append(box)
    for poly in m2_polys:
        if len(poly) >= 3:
            box = (
                float(poly[:, 0].min()) * dbu,
                float(poly[:, 1].min()) * dbu,
                float(poly[:, 0].max()) * dbu,
                float(poly[:, 1].max()) * dbu,
            )
            if not any(box[0] <= px <= box[2] and box[1] <= py <= box[3] for px, py in port_points_um):
                m2_bboxes.append(box)

    width_profiles: List[List[float]] = [list(seg_widths)]
    if dynamic_width and seg_widths:
        min_seg_w = max(float(_DRC["min_width"][LAYER_M1]), float(width))
        for scale in (0.9, 0.8, 0.7, 0.6, 0.5):
            trial = [max(min_seg_w, sw * scale) for sw in seg_widths]
            if any(
                all(abs(a - b) <= 1e-6 for a, b in zip(trial, existing))
                for existing in width_profiles
            ):
                continue
            width_profiles.append(trial)

    base_corners = [tuple(c) for c in corners_3d]
    for trial_idx, seg_widths_trial in enumerate(width_profiles):
        corners_trial = [tuple(c) for c in base_corners]
        geom_blocked = False
        via_pad_by_transition: Dict[int, float] = {}
        for i in range(len(corners_trial) - 1):
            x0, y0, z0 = corners_trial[i]
            _, _, z1 = corners_trial[i + 1]
            if z0 == z1:
                continue
            target_w = _transition_target_via_width(corners_trial, seg_widths_trial, i, width)
            target_pad = _via_pad_size_um(target_w)
            base_center = (x0 * dbu, y0 * dbu)
            allow_relocate = i > 0 and (i + 1) < (len(corners_trial) - 1)
            resolved = None
            chosen_pad = None
            for via_pad in _via_pad_candidates(target_pad):
                candidate = _resolve_legal_via_center(
                    base_center_um=base_center,
                    via_pad_um=via_pad,
                    m1_bboxes=m1_bboxes,
                    m2_bboxes=m2_bboxes,
                    dbu=dbu,
                    relocate_step_um=max(clearance, 0.14),
                    relocate_radius_um=max(1.0, 2.0 * clearance),
                    max_candidates=64,
                    allow_relocate=allow_relocate,
                )
                if candidate is None:
                    continue
                resolved = candidate
                chosen_pad = via_pad
                break
            if resolved is None or chosen_pad is None:
                geom_blocked = True
                break
            via_pad_by_transition[i] = chosen_pad
            if resolved != base_center:
                rx = int(round(resolved[0] / dbu))
                ry = int(round(resolved[1] / dbu))
                corners_trial[i] = (rx, ry, z0)
                corners_trial[i + 1] = (rx, ry, z1)

        plan_segments: List[Tuple[Tuple[float, float], Tuple[float, float], Tuple[int, int], float]] = []
        plan_vias: List[Tuple[Tuple[float, float], float]] = []

        def _plan_add_segment(p0: Tuple[float, float], p1: Tuple[float, float], layer: Tuple[int, int], seg_w: float) -> None:
            dx = abs(p1[0] - p0[0])
            dy = abs(p1[1] - p0[1])
            if dx < MIN_SEGMENT_LENGTH and dy < MIN_SEGMENT_LENGTH:
                return
            if dx > 0.001 and dy > 0.001:
                mid = (p1[0], p0[1]) if layer == LAYER_M1 else (p0[0], p1[1])
                _plan_add_segment(p0, mid, layer, seg_w)
                _plan_add_segment(mid, p1, layer, seg_w)
                return
            plan_segments.append((p0, p1, layer, seg_w))

        for i in range(len(corners_trial) - 1):
            x0, y0, z0 = corners_trial[i]
            x1, y1, z1 = corners_trial[i + 1]
            seg_w = seg_widths_trial[i] if i < len(seg_widths_trial) else width
            p0 = (x0 * dbu, y0 * dbu)
            p1 = (x1 * dbu, y1 * dbu)
            if z0 != z1:
                via_pad = via_pad_by_transition.get(
                    i,
                    _via_pad_size_um(_transition_target_via_width(corners_trial, seg_widths_trial, i, width)),
                )
                plan_vias.append((p0, via_pad))
                _plan_add_segment(p0, p1, LAYER_M1 if z1 == 0 else LAYER_M2, seg_w)
            else:
                _plan_add_segment(p0, p1, LAYER_M1 if z0 == 0 else LAYER_M2, seg_w)

        plan_patches = _build_corner_patches_from_segments(plan_segments)

        if not geom_blocked:
            for p0, p1, layer, seg_w in plan_segments:
                seg_box = _segment_envelope_um(p0, p1, seg_w)
                target = m1_bboxes if layer == LAYER_M1 else m2_bboxes
                if any(_bbox_overlap(seg_box, obox) for obox in target):
                    geom_blocked = True
                    break

        if not geom_blocked:
            for center, layer, patch_w, patch_h in plan_patches:
                patch_box = _rect_envelope_um(center, patch_w, patch_h)
                target = m1_bboxes if layer == LAYER_M1 else m2_bboxes
                if any(_bbox_overlap(patch_box, obox) for obox in target):
                    geom_blocked = True
                    break

        if not geom_blocked:
            for center, via_w in plan_vias:
                if not _is_via_legal_on_both_layers(center, via_w, m1_bboxes, m2_bboxes):
                    geom_blocked = True
                    break

        if geom_blocked:
            continue

        if trial_idx > 0:
            print(
                f"[ROUTE] Dynamic straight width downgraded by profile {trial_idx} "
                "for legal geometry."
            )

        segment_ports: List[Port] = []
        for center, layer, patch_w, patch_h in plan_patches:
            patch = c.add_ref(gf.components.rectangle(size=(patch_w, patch_h), layer=layer))
            patch.dcenter = center

        for center, via_w in plan_vias:
            via = c.add_ref(via_m1_m2(width=via_w, length=via_w))
            via.dcenter = center

        for p0, p1, layer, seg_w in plan_segments:
            is_horiz = abs(p1[1] - p0[1]) < 0.001
            if is_horiz:
                x_min = min(p0[0], p1[0])
                x_max = max(p0[0], p1[0])
                seg_len = x_max - x_min
                if seg_len >= 0.001:
                    rect = c.add_ref(gf.components.rectangle(size=(seg_len, seg_w), layer=layer))
                    rect.dmove((x_min, p0[1] - seg_w / 2))
                    if add_segment_ports:
                        port = c.add_port(
                            name=f"{port_name_prefix}",
                            center=(x_min + seg_len / 2, p0[1]),
                            width=0.01,
                            orientation=0,
                            layer=(layer[0], 16),
                            port_type="electrical",
                        )
                        segment_ports.append(port)
                        c.draw_ports()
            else:
                y_min = min(p0[1], p1[1])
                y_max = max(p0[1], p1[1])
                seg_len = y_max - y_min
                if seg_len >= 0.001:
                    rect = c.add_ref(gf.components.rectangle(size=(seg_w, seg_len), layer=layer))
                    rect.dmove((p0[0] - seg_w / 2, y_min))
                    if add_segment_ports:
                        port = c.add_port(
                            name=f"{port_name_prefix}",
                            center=(p0[0], y_min + seg_len / 2),
                            width=0.01,
                            orientation=90,
                            layer=(layer[0], 16),
                            port_type="electrical",
                        )
                        segment_ports.append(port)
                        c.draw_ports()

        return segment_ports

    return None


def route_hierarchical(
    c: Component,
    start: Port,
    stop: Port,
    global_grid_unit: float = 2.0,
    detail_grid_unit: float = 0.25,
    width: float = 0.25,
    layers_to_avoid: Iterable[LayerSpec] = None,
    detail_margin: float = 5.0,
    clearance: float = 0.14,
    clearance_ladder: Tuple[float, ...] = (0.14, 0.10, 0.07),
    deterministic: bool = True,
    add_segment_ports: bool = False,
    port_name_prefix: str = "seg",
    dynamic_width: bool = True,
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
        dynamic_width: If True, use polygon-driven endpoint snapping and dynamic segment widths.
        layers_to_avoid: Layers containing obstructions.
        detail_margin: Margin around path for detailed routing (um).
        clearance: Preferred minimum obstruction offset in um.
        clearance_ladder: Deterministic fallback offsets in um.
        deterministic: Enable deterministic candidate ordering/tie-breaks.
        add_segment_ports: If True, add a port to each straight segment.
        port_name_prefix: Prefix for port names (default: "seg").
    
    Returns:
        List of ports added to segments (empty if add_segment_ports=False or routing fails).
    """
    dbu = c.kcl.dbu
    kc = c.kcl.kcells[c.name]
    _layers = [layer if isinstance(layer, tuple) else (layer, 0) for layer in (layers_to_avoid or [])]

    start_x, start_y = start.dcenter[0], start.dcenter[1]
    stop_x, stop_y = stop.dcenter[0], stop.dcenter[1]
    start_dbu = (int(start_x / dbu), int(start_y / dbu))
    stop_dbu = (int(stop_x / dbu), int(stop_y / dbu))
    port_points_um = [(start_x, start_y), (stop_x, stop_y)]
    port_points_dbu = [start_dbu, stop_dbu]

    def _get_layer_tuple_local(port: Port, component: Component):
        if hasattr(port, "layer"):
            info = component.kcl.get_info(port.layer)
            return (info.layer, info.datatype)
        return None

    def _poly_bboxes_um(polys: List[np.ndarray]) -> List[Tuple[float, float, float, float]]:
        bboxes = []
        for poly in polys:
            if len(poly) < 3:
                continue
            x0 = float(poly[:, 0].min()) * dbu
            x1 = float(poly[:, 0].max()) * dbu
            y0 = float(poly[:, 1].min()) * dbu
            y1 = float(poly[:, 1].max()) * dbu
            bboxes.append((x0, y0, x1, y1))
        return bboxes

    def _bbox_contains_any_point(
        bbox: Tuple[float, float, float, float],
        points: List[Tuple[float, float]],
    ) -> bool:
        x0, y0, x1, y1 = bbox
        for px, py in points:
            if x0 <= px <= x1 and y0 <= py <= y1:
                return True
        return False

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
        clearance=clearance,
    )

    # Validate A* result including required corner/start-end vias.
    use_m2_horiz = False
    if path is not None and len(path) >= 2:
        path = _simplify_path(_make_manhattan(path))
        start_layer = _get_layer_tuple_local(start, c)
        stop_layer = _get_layer_tuple_local(stop, c)

        buffer_dbu = int(round(max(0.0, clearance) / dbu))
        m1_polys = (
            _extract_polys_for_layers(kc, [LAYER_M1], dbu, port_points_dbu, buffer_dbu=buffer_dbu)
            if LAYER_M1 in _layers else []
        )
        m2_polys = (
            _extract_polys_for_layers(kc, [LAYER_M2], dbu, port_points_dbu, buffer_dbu=buffer_dbu)
            if LAYER_M2 in _layers else []
        )
        m1_bboxes = [b for b in _poly_bboxes_um(m1_polys) if not _bbox_contains_any_point(b, port_points_um)]
        m2_bboxes = [b for b in _poly_bboxes_um(m2_polys) if not _bbox_contains_any_point(b, port_points_um)]

        path_blocked = False
        for i in range(len(path) - 1):
            p0 = path[i]
            p1 = path[i + 1]
            seg_layer = LAYER_M1 if _is_horizontal(p0, p1) else LAYER_M2
            seg_box = _segment_envelope_um(p0, p1, width)
            target = m1_bboxes if seg_layer == LAYER_M1 else m2_bboxes
            if any(_bbox_overlap(seg_box, obox) for obox in target):
                path_blocked = True
                break

        if not path_blocked:
            via_points = []
            if len(path) >= 3:
                via_points.extend(path[1:-1])
            first_layer = LAYER_M1 if _is_horizontal(path[0], path[1]) else LAYER_M2
            if start_layer and start_layer != first_layer:
                via_points.append(path[0])
            last_layer = LAYER_M1 if _is_horizontal(path[-2], path[-1]) else LAYER_M2
            if stop_layer and stop_layer != last_layer:
                via_points.append(path[-1])

            via_w = _via_pad_size_um(width)
            for vpt in via_points:
                if not _is_via_legal_on_both_layers(vpt, via_w, m1_bboxes, m2_bboxes):
                    path_blocked = True
                    break

        if path_blocked:
            print(
                "[ROUTE] Initial A* path violates corner/via obstruction clearance; "
                "switching to via-escape search."
            )
            path = None
    
    # If M1 routing failed, try deterministic via-escape strategy.
    if path is None:
        print("[VIA-ESCAPE] M1 routing blocked - trying deterministic escape routing...")

        x_tolerance = 0.01
        y_tolerance = 0.01
        ports_vertically_aligned = abs(start_x - stop_x) < x_tolerance
        ports_horizontally_aligned = abs(start_y - stop_y) < y_tolerance

        def _candidate_uses_m2_horiz(name: str) -> bool:
            return name == "direct_m2_horizontal"

        def _count_bends(candidate_path: List[Tuple[float, float]]) -> int:
            return max(0, len(candidate_path) - 2)

        def _candidate_via_points(
            candidate_path: List[Tuple[float, float]],
            use_m2_horiz: bool,
            start_layer: Optional[Tuple[int, int]],
            stop_layer: Optional[Tuple[int, int]],
        ) -> List[Tuple[float, float]]:
            via_points = []
            if len(candidate_path) >= 3 and not use_m2_horiz:
                via_points.extend(candidate_path[1:-1])
            if len(candidate_path) >= 2:
                first_horiz = _is_horizontal(candidate_path[0], candidate_path[1])
                first_layer = LAYER_M2 if use_m2_horiz else (LAYER_M1 if first_horiz else LAYER_M2)
                if start_layer and start_layer != first_layer:
                    via_points.append(candidate_path[0])
                last_horiz = _is_horizontal(candidate_path[-2], candidate_path[-1])
                last_layer = LAYER_M2 if use_m2_horiz else (LAYER_M1 if last_horiz else LAYER_M2)
                if stop_layer and stop_layer != last_layer:
                    via_points.append(candidate_path[-1])
            seen = set()
            unique_points = []
            for x, y in via_points:
                key = (round(x / dbu), round(y / dbu))
                if key not in seen:
                    seen.add(key)
                    unique_points.append((x, y))
            return unique_points

        def _candidate_blocking_boxes(
            candidate_path: List[Tuple[float, float]],
            use_m2_horiz: bool,
            m1_bboxes: List[Tuple[float, float, float, float]],
            m2_bboxes: List[Tuple[float, float, float, float]],
            via_pad_w: float,
            via_pad_h: float,
            start_layer: Optional[Tuple[int, int]],
            stop_layer: Optional[Tuple[int, int]],
        ) -> List[Tuple[float, float, float, float]]:
            blocking = []
            for i in range(len(candidate_path) - 1):
                p0 = candidate_path[i]
                p1 = candidate_path[i + 1]
                is_h = _is_horizontal(p0, p1)
                seg_layer = LAYER_M2 if use_m2_horiz else (LAYER_M1 if is_h else LAYER_M2)
                seg_box = _segment_envelope_um(p0, p1, width)
                target_bboxes = m1_bboxes if seg_layer == LAYER_M1 else m2_bboxes
                for obox in target_bboxes:
                    if _bbox_overlap(seg_box, obox):
                        blocking.append(obox)
            via_points = _candidate_via_points(candidate_path, use_m2_horiz, start_layer, stop_layer)
            for vpt in via_points:
                if not _is_via_legal_on_both_layers(vpt, max(via_pad_w, via_pad_h), m1_bboxes, m2_bboxes):
                    # Keep deterministic blocker bookkeeping shape.
                    blocking.append((vpt[0], vpt[1], vpt[0], vpt[1]))
            return blocking

        clearance_attempts = (
            _deterministic_clearance_attempts(clearance, clearance_ladder)
            if deterministic
            else [max(0.0, float(clearance))]
        )
        if not clearance_attempts:
            clearance_attempts = [0.0]

        use_m2_horiz = False
        start_layer = _get_layer_tuple_local(start, c)
        stop_layer = _get_layer_tuple_local(stop, c)

        for attempt_idx, clearance_try in enumerate(clearance_attempts, start=1):
            buffer_dbu = int(round(max(0.0, clearance_try) / dbu))
            m1_polys = (
                _extract_polys_for_layers(kc, [LAYER_M1], dbu, port_points_dbu, buffer_dbu=buffer_dbu)
                if LAYER_M1 in _layers else []
            )
            m2_polys = (
                _extract_polys_for_layers(kc, [LAYER_M2], dbu, port_points_dbu, buffer_dbu=buffer_dbu)
                if LAYER_M2 in _layers else []
            )
            m1_bboxes = [b for b in _poly_bboxes_um(m1_polys) if not _bbox_contains_any_point(b, port_points_um)]
            m2_bboxes = [b for b in _poly_bboxes_um(m2_polys) if not _bbox_contains_any_point(b, port_points_um)]
            print(
                f"[VIA-ESCAPE] attempt {attempt_idx}/{len(clearance_attempts)} "
                f"clearance={clearance_try:.3f}um m1_obs={len(m1_bboxes)} m2_obs={len(m2_bboxes)}"
            )

            direct_candidates = [
                ("direct_h_first", [(start_x, start_y), (stop_x, start_y), (stop_x, stop_y)]),
                ("direct_v_first", [(start_x, start_y), (start_x, stop_y), (stop_x, stop_y)]),
            ]
            if ports_vertically_aligned:
                direct_candidates.append(("direct_vertical", [(start_x, start_y), (stop_x, stop_y)]))
            if ports_horizontally_aligned:
                direct_candidates.append(("direct_horizontal", [(start_x, start_y), (stop_x, stop_y)]))
                direct_candidates.append(("direct_m2_horizontal", [(start_x, start_y), (stop_x, stop_y)]))

            direct_blockers = []
            for name, candidate in direct_candidates:
                simp = _simplify_path(candidate)
                if not _is_valid_manhattan_path(simp):
                    continue
                direct_blockers.extend(
                    _candidate_blocking_boxes(
                        simp,
                        _candidate_uses_m2_horiz(name),
                        m1_bboxes,
                        m2_bboxes,
                        _via_pad_size_um(width),
                        _via_pad_size_um(width),
                        start_layer,
                        stop_layer,
                    )
                )

            if direct_blockers:
                blocker_x_min = min(b[0] for b in direct_blockers)
                blocker_y_min = min(b[1] for b in direct_blockers)
                blocker_x_max = max(b[2] for b in direct_blockers)
                blocker_y_max = max(b[3] for b in direct_blockers)
            else:
                blocker_x_min = min(start_x, stop_x) - clearance_try
                blocker_y_min = min(start_y, stop_y) - clearance_try
                blocker_x_max = max(start_x, stop_x) + clearance_try
                blocker_y_max = max(start_y, stop_y) + clearance_try

            min_escape = max(1.0, width + clearance_try)
            blocker_x_min = min(blocker_x_min, min(start_x, stop_x) - min_escape)
            blocker_y_min = min(blocker_y_min, min(start_y, stop_y) - min_escape)
            blocker_x_max = max(blocker_x_max, max(start_x, stop_x) + min_escape)
            blocker_y_max = max(blocker_y_max, max(start_y, stop_y) + min_escape)

            escape_x_left = blocker_x_min - clearance_try
            escape_x_right = blocker_x_max + clearance_try
            escape_y_top = blocker_y_max + clearance_try
            escape_y_bottom = blocker_y_min - clearance_try

            candidate_paths = list(direct_candidates)
            candidate_paths.extend(
                [
                    ("escape_left", [(start_x, start_y), (escape_x_left, start_y), (escape_x_left, stop_y), (stop_x, stop_y)]),
                    ("escape_right", [(start_x, start_y), (escape_x_right, start_y), (escape_x_right, stop_y), (stop_x, stop_y)]),
                    ("escape_top", [(start_x, start_y), (start_x, escape_y_top), (stop_x, escape_y_top), (stop_x, stop_y)]),
                    ("escape_bottom", [(start_x, start_y), (start_x, escape_y_bottom), (stop_x, escape_y_bottom), (stop_x, stop_y)]),
                    ("s_up_left", [(start_x, start_y), (start_x, escape_y_top), (escape_x_left, escape_y_top), (escape_x_left, stop_y), (stop_x, stop_y)]),
                    ("s_up_right", [(start_x, start_y), (start_x, escape_y_top), (escape_x_right, escape_y_top), (escape_x_right, stop_y), (stop_x, stop_y)]),
                    ("s_down_left", [(start_x, start_y), (start_x, escape_y_bottom), (escape_x_left, escape_y_bottom), (escape_x_left, stop_y), (stop_x, stop_y)]),
                    ("s_down_right", [(start_x, start_y), (start_x, escape_y_bottom), (escape_x_right, escape_y_bottom), (escape_x_right, stop_y), (stop_x, stop_y)]),
                ]
            )

            best_choice = None
            for name, candidate in candidate_paths:
                simplified = _simplify_path(candidate)
                if not _is_valid_manhattan_path(simplified):
                    print(f"[VIA-ESCAPE] Path '{name}': INVALID")
                    continue

                use_m2_horiz_candidate = _candidate_uses_m2_horiz(name)
                via_points = _candidate_via_points(simplified, use_m2_horiz_candidate, start_layer, stop_layer)
                via_pad_w = _via_pad_size_um(width)
                via_pad_h = via_pad_w
                blocking = _candidate_blocking_boxes(
                    simplified,
                    use_m2_horiz_candidate,
                    m1_bboxes,
                    m2_bboxes,
                    via_pad_w,
                    via_pad_h,
                    start_layer,
                    stop_layer,
                )
                is_blocked = len(blocking) > 0
                length = _calc_path_length(simplified)
                bends = _count_bends(simplified)
                vias = len(via_points)
                lex_key = tuple((int(round(px / dbu)), int(round(py / dbu))) for px, py in simplified)
                rank = (length, vias, bends, lex_key) if deterministic else (length,)
                print(
                    f"[VIA-ESCAPE] Path '{name}': length={length:.3f}um vias={vias} bends={bends} "
                    f"{'BLOCKED' if is_blocked else 'CLEAR'}"
                )
                if is_blocked:
                    continue
                if best_choice is None or rank < best_choice["rank"]:
                    best_choice = {
                        "name": name,
                        "path": simplified,
                        "rank": rank,
                        "length": length,
                        "use_m2_horiz": use_m2_horiz_candidate,
                    }

            if best_choice is not None:
                path = best_choice["path"]
                use_m2_horiz = best_choice["use_m2_horiz"]
                print(
                    f"[VIA-ESCAPE] Selected '{best_choice['name']}' on clearance {clearance_try:.3f}um "
                    f"(length={best_choice['length']:.3f}um)"
                )
                break
            
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

    # Final via legality guard (both layers) just before drawing.
    via_guard_buffer_dbu = int(round(max(0.0, clearance) / dbu))
    via_guard_m1 = _extract_polys_for_layers(kc, [LAYER_M1], dbu, port_points_dbu, buffer_dbu=via_guard_buffer_dbu)
    via_guard_m2 = _extract_polys_for_layers(kc, [LAYER_M2], dbu, port_points_dbu, buffer_dbu=via_guard_buffer_dbu)
    m1_via_bboxes = [b for b in _poly_bboxes_um(via_guard_m1) if not _bbox_contains_any_point(b, port_points_um)]
    m2_via_bboxes = [b for b in _poly_bboxes_um(via_guard_m2) if not _bbox_contains_any_point(b, port_points_um)]

    if dynamic_width:
        start_geom = _get_port_geometry(start, kc, dbu, default_width=width)
        stop_geom = _get_port_geometry(stop, kc, dbu, default_width=width)
        selected_endpoint, selected_axis = _selected_polygon_meta(start_geom, stop_geom)
        body_width = max(
            _DRC["min_width"][LAYER_M1],
            min(
                start_geom.width_x,
                start_geom.width_y,
                stop_geom.width_x,
                stop_geom.width_y,
            ),
        )

        def _layer_idx_from_tuple(layer_tuple: Optional[Tuple[int, int]], default_idx: int) -> int:
            if layer_tuple == LAYER_M2:
                return 1
            if layer_tuple == LAYER_M1:
                return 0
            return default_idx

        def _segment_layer_idx(p0: Tuple[float, float], p1: Tuple[float, float]) -> int:
            is_h = _is_horizontal(p0, p1)
            if is_h:
                return 1 if use_m2_horiz else 0
            return 1

        if len(path) < 2:
            return []

        start_layer_tuple = _get_layer_tuple_local(start, c)
        stop_layer_tuple = _get_layer_tuple_local(stop, c)

        def _build_corners_from_path(path_pts: List[Tuple[float, float]]) -> List[Tuple[int, int, int]]:
            first_seg_layer = _segment_layer_idx(path_pts[0], path_pts[1])
            current_layer = _layer_idx_from_tuple(start_layer_tuple, first_seg_layer)
            x0 = int(round(path_pts[0][0] / dbu))
            y0 = int(round(path_pts[0][1] / dbu))
            out: List[Tuple[int, int, int]] = [(x0, y0, current_layer)]
            if current_layer != first_seg_layer:
                out.append((x0, y0, first_seg_layer))
            for i in range(len(path_pts) - 1):
                sx = int(round(path_pts[i][0] / dbu))
                sy = int(round(path_pts[i][1] / dbu))
                ex = int(round(path_pts[i + 1][0] / dbu))
                ey = int(round(path_pts[i + 1][1] / dbu))
                seg_layer = _segment_layer_idx(path_pts[i], path_pts[i + 1])
                if out[-1][0] != sx or out[-1][1] != sy:
                    out.append((sx, sy, out[-1][2]))
                if out[-1][2] != seg_layer:
                    out.append((sx, sy, seg_layer))
                out.append((ex, ey, seg_layer))
            last_seg_layer = _segment_layer_idx(path_pts[-2], path_pts[-1])
            stop_layer_idx = _layer_idx_from_tuple(stop_layer_tuple, last_seg_layer)
            if out[-1][2] != stop_layer_idx:
                out.append((out[-1][0], out[-1][1], stop_layer_idx))
            return out

        for axis_mode in ("hard", "prefer", "off"):
            path_trial = list(path)
            if axis_mode != "off":
                _enforce_axis_on_path_endpoint(
                    path_trial,
                    endpoint=selected_endpoint,
                    axis=selected_axis,
                    mode=axis_mode,
                )
            path_trial = _make_manhattan(path_trial)
            path_trial = _simplify_path(path_trial)
            if len(path_trial) < 2:
                continue
            corners_3d = _build_corners_from_path(path_trial)
            dyn_ports = _draw_dynamic_geometry_for_corners(
                c=c,
                corners_3d=corners_3d,
                start_geom=start_geom,
                stop_geom=stop_geom,
                body_width=body_width,
                width=width,
                dynamic_width=True,
                m1_polys=via_guard_m1,
                m2_polys=via_guard_m2,
                start_xy_dbu=(int(round(start_x / dbu)), int(round(start_y / dbu))),
                stop_xy_dbu=(int(round(stop_x / dbu)), int(round(stop_y / dbu))),
                dbu=dbu,
                clearance=clearance,
                add_segment_ports=add_segment_ports,
                port_name_prefix=port_name_prefix,
            )
            if dyn_ports is not None:
                if axis_mode == "prefer":
                    print("[ROUTE] Axis policy downgraded to prefer for legal fallback geometry.")
                elif axis_mode == "off":
                    print("[ROUTE] Axis policy downgraded to off for legal fallback geometry.")
                return dyn_ports
        print("[ROUTE] Dynamic fallback geometry blocked; aborting route.")
        return []

    # Final segment and corner legality guard before any drawing.
    for i in range(len(path) - 1):
        p0 = path[i]
        p1 = path[i + 1]
        seg_layer = horiz_layer if _is_horizontal(p0, p1) else vert_layer
        seg_box = _segment_envelope_um(p0, p1, width)
        seg_obs = m1_via_bboxes if seg_layer == LAYER_M1 else m2_via_bboxes
        if any(_bbox_overlap(seg_box, obox) for obox in seg_obs):
            print(
                "[ROUTE] Final planned segment blocked on "
                f"{'M1' if seg_layer == LAYER_M1 else 'M2'}; aborting route."
            )
            return []

    # Same-layer bends materialize as square corner patches in _draw_route_segments.
    if horiz_layer == vert_layer and len(path) >= 3:
        patch_obs = m1_via_bboxes if horiz_layer == LAYER_M1 else m2_via_bboxes
        for corner in path[1:-1]:
            patch_box = _via_envelope_um(corner, width, width)
            if any(_bbox_overlap(patch_box, obox) for obox in patch_obs):
                print(
                    "[ROUTE] Final planned corner patch blocked on "
                    f"{'M1' if horiz_layer == LAYER_M1 else 'M2'} at "
                    f"({corner[0]:.3f}, {corner[1]:.3f}); aborting route."
                )
                return []

    if add_vias:
        via_pad = _via_pad_size_um(width)
        for via_pt in path[1:-1]:
            if not _is_via_legal_on_both_layers(via_pt, via_pad, m1_via_bboxes, m2_via_bboxes):
                print(
                    "[ROUTE] Intermediate via blocked on M1/M2 at "
                    f"({via_pt[0]:.3f}, {via_pt[1]:.3f}); aborting route."
                )
                return []

    # Pre-check start/end transition vias before any geometry is drawn.
    start_transition_via = None
    stop_transition_via = None
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
            start_transition_via = path[0]
            via_w = _via_pad_size_um(width)
            if not _is_via_legal_on_both_layers(start_transition_via, via_w, m1_via_bboxes, m2_via_bboxes):
                print(
                    "[ROUTE] Start transition via blocked on M1/M2 at "
                    f"({start_transition_via[0]:.3f}, {start_transition_via[1]:.3f}); aborting route."
                )
                return []

        last_horiz = _is_horizontal(path[-2], path[-1])
        last_layer = horiz_layer if last_horiz else vert_layer
        stop_layer = _get_layer_tuple(stop, c)
        if stop_layer and stop_layer != last_layer:
            stop_transition_via = path[-1]
            via_w = _via_pad_size_um(width)
            if not _is_via_legal_on_both_layers(stop_transition_via, via_w, m1_via_bboxes, m2_via_bboxes):
                print(
                    "[ROUTE] Stop transition via blocked on M1/M2 at "
                    f"({stop_transition_via[0]:.3f}, {stop_transition_via[1]:.3f}); aborting route."
                )
                return []
    
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
    if start_transition_via is not None:
        via_w = _via_pad_size_um(width)
        via = c.add_ref(via_m1_m2(width=via_w, length=via_w))
        via.dcenter = start_transition_via

    if stop_transition_via is not None:
        via_w = _via_pad_size_um(width)
        via = c.add_ref(via_m1_m2(width=via_w, length=via_w))
        via.dcenter = stop_transition_via
    
    return segment_ports


def route_multilayer_3d(
    c: Component,
    start: Port,
    stop: Port,
    grid_unit: float = 1.0,
    width: float = 0.25,
    dynamic_width: bool = True,
    layers_to_avoid: Iterable[LayerSpec] = None,
    add_segment_ports: bool = False,
    port_name_prefix: str = "seg",
    via_cost: float = 10.0,
    wrong_way_penalty: float = 8.0,
    clearance: float = 0.14,
    clearance_ladder: Tuple[float, ...] = (0.14, 0.10, 0.07),
    deterministic: bool = True,
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
        width: Wire width in um (fallback/base width).
        dynamic_width: If True, derive endpoint/body widths from port geometry.
            If False, route with fixed `width` everywhere.
        layers_to_avoid: Layers containing obstructions (per-layer).
        add_segment_ports: If True, add a port to each straight segment.
        port_name_prefix: Prefix for port names.
        via_cost: Cost weight for via transitions.
        wrong_way_penalty: Penalty for routing against preferred direction.
        clearance: Preferred minimum obstruction offset in um.
        clearance_ladder: Deterministic fallback offsets in um.
        deterministic: Enable deterministic routing retry behavior.
    
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

    # Geometry-aware widths for dynamic mode.
    start_geom = _get_port_geometry(start, kc, dbu, default_width=width)
    stop_geom = _get_port_geometry(stop, kc, dbu, default_width=width)
    selected_poly, selected_axis = _selected_polygon_meta(start_geom, stop_geom)
    selected_straight_width = _selected_straight_width(start_geom, stop_geom, width)
    if dynamic_width:
        start_width = max(width, start_geom.width_x, start_geom.width_y)
        stop_width = max(width, stop_geom.width_x, stop_geom.width_y)
        body_width = max(
            _DRC["min_width"][LAYER_M1],
            min(
                start_geom.width_x,
                start_geom.width_y,
                stop_geom.width_x,
                stop_geom.width_y,
            ),
        )
    else:
        start_width = width
        stop_width = width
        body_width = width
    
    # Invert stop orientation (port faces inward, we approach from opposite direction)
    stop_dir_map = {"n": "s", "s": "n", "e": "w", "w": "e", "o": "o"}
    stop_pos = (stop_pos[0], stop_pos[1], stop_dir_map[stop_pos[2]])
    
    # Port points for polygon exclusion
    port_points = [
        (start_pos[0], start_pos[1]),
        (stop_pos[0], stop_pos[1]),
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
    print(f"[3D ROUTE] Grid: {grid_w}x{grid_h} x 2 layers = {grid_w*grid_h*2} cells")
    print(f"[3D ROUTE] from ({start_x*dbu:.3f}, {start_y*dbu:.3f}, L{start_layer_idx}) "
          f"to ({stop_x*dbu:.3f}, {stop_y*dbu:.3f}, L{stop_layer_idx})")
    print(f"[3D ROUTE] BBox: ({min_x*dbu:.1f}, {min_y*dbu:.1f}) -> ({max_x*dbu:.1f}, {max_y*dbu:.1f})")
    print(
        f"[3D ROUTE] widths dynamic={dynamic_width} "
        f"start={start_width:.3f}um body={body_width:.3f}um stop={stop_width:.3f}um "
        f"selected={selected_poly} selected_straight={selected_straight_width:.3f}um "
        f"selected_axis={selected_axis}"
    )

    # Wider search clearance in dynamic mode to honor endpoint/body widths.
    max_wire_width = max(start_width, stop_width, body_width, _DRC["min_width"][LAYER_M1])
    wire_half_width_dbu = int(max_wire_width / 2 / dbu) if dynamic_width else 0

    def _show_3d_with_width(bbox_value, grid_unit_value, polys_per_layer):
        kwargs = dict(
            polys_per_layer=polys_per_layer,
            start=start_3d,
            stop=stop_3d,
            bbox=bbox_value,
            grid_unit=grid_unit_value,
            layer_directions=["h", "v"],
            via_cost=via_cost,
            wrong_way_penalty=wrong_way_penalty,
        )
        if dynamic_width and wire_half_width_dbu > 0:
            try:
                return _doroutes.show_3d(wire_half_width=wire_half_width_dbu, **kwargs)
            except TypeError:
                pass
        return _doroutes.show_3d(**kwargs)

    clearance_attempts = (
        _deterministic_clearance_attempts(clearance, clearance_ladder)
        if deterministic
        else [max(0.0, clearance)]
    )

    corners_3d = None
    num_vias = 0
    last_error: Optional[Exception] = None

    for clearance_um in clearance_attempts:
        buffer_dbu = int(round(clearance_um / dbu))
        m1_polys = _extract_polys_for_layers(
            kc, [LAYER_M1], dbu, port_points, buffer_dbu=buffer_dbu
        ) if LAYER_M1 in _layers else []
        m2_polys = _extract_polys_for_layers(
            kc, [LAYER_M2], dbu, port_points, buffer_dbu=buffer_dbu
        ) if LAYER_M2 in _layers else []
        polys_per_layer = [m1_polys, m2_polys]
        print(f"[3D ROUTE] Obstructions@{clearance_um:.3f}um: M1={len(m1_polys)}, M2={len(m2_polys)}")

        try:
            corners_3d, num_vias = _show_3d_with_width(bbox_tuple, grid_unit_dbu, polys_per_layer)
            print(f"[3D ROUTE] clearance={clearance_um:.3f}um succeeded")
            break
        except Exception as e:
            last_error = e
            print(f"[3D ROUTE] clearance={clearance_um:.3f}um failed: {e}")
            print("[3D ROUTE] Retrying this clearance with expanded bbox and finer grid...")
            try:
                retry_padding = int(padding * 2.0)
                retry_min_x = min_x - padding
                retry_max_x = max_x + padding
                retry_min_y = min_y - padding
                retry_max_y = max_y + padding
                retry_bbox = (retry_max_y, retry_max_x, retry_min_y, retry_min_x)

                retry_grid_unit = grid_unit * 0.5
                retry_grid_unit_dbu = int(retry_grid_unit / dbu)
                r_grid_w = (retry_max_x - retry_min_x) // retry_grid_unit_dbu
                r_grid_h = (retry_max_y - retry_min_y) // retry_grid_unit_dbu
                print(f"[3D ROUTE RETRY] Grid: {r_grid_w}x{r_grid_h} x 2 layers")

                corners_3d, num_vias = _show_3d_with_width(retry_bbox, retry_grid_unit_dbu, polys_per_layer)
                print(f"[3D ROUTE] clearance={clearance_um:.3f}um succeeded on retry")
                break
            except Exception as e2:
                last_error = e2
                print(f"[3D ROUTE] clearance={clearance_um:.3f}um retry failed: {e2}")

    if corners_3d is None:
        print(f"[3D ROUTE] All clearance attempts failed: {clearance_attempts}")
        if last_error is not None:
            print(f"[3D ROUTE] Last error: {last_error}")
        print("[3D ROUTE] Falling back to hierarchical router...")
        return route_hierarchical(
            c, start, stop,
            global_grid_unit=grid_unit * 2,
            detail_grid_unit=grid_unit,
            width=width,
            dynamic_width=dynamic_width,
            layers_to_avoid=layers_to_avoid,
            clearance=clearance,
            clearance_ladder=clearance_ladder,
            deterministic=deterministic,
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

    if dynamic_width:
        base_corners = [tuple(c) for c in corners_3d]
        for axis_mode in ("hard", "prefer", "off"):
            trial_corners = [tuple(c) for c in base_corners]
            if axis_mode != "off":
                _enforce_axis_on_corners_endpoint(
                    trial_corners,
                    endpoint=selected_poly,
                    axis=selected_axis,
                    jog_dbu=max(1, grid_unit_dbu),
                    mode=axis_mode,
                )
            dyn_ports = _draw_dynamic_geometry_for_corners(
                c=c,
                corners_3d=trial_corners,
                start_geom=start_geom,
                stop_geom=stop_geom,
                body_width=body_width,
                width=width,
                dynamic_width=True,
                m1_polys=m1_polys,
                m2_polys=m2_polys,
                start_xy_dbu=(start_x, start_y),
                stop_xy_dbu=(stop_x, stop_y),
                dbu=dbu,
                clearance=clearance,
                add_segment_ports=add_segment_ports,
                port_name_prefix=port_name_prefix,
            )
            if dyn_ports is not None:
                if axis_mode == "prefer":
                    print("[3D ROUTE] Axis policy downgraded to prefer for legal geometry.")
                elif axis_mode == "off":
                    print("[3D ROUTE] Axis policy downgraded to off for legal geometry.")
                return dyn_ports
        print("[3D ROUTE] Planned geometry violates obstruction clearance; falling back to hierarchical router...")
        return route_hierarchical(
            c, start, stop,
            global_grid_unit=grid_unit * 2,
            detail_grid_unit=grid_unit,
            width=width,
            dynamic_width=dynamic_width,
            layers_to_avoid=layers_to_avoid,
            clearance=clearance,
            clearance_ladder=clearance_ladder,
            deterministic=deterministic,
            add_segment_ports=add_segment_ports,
            port_name_prefix=port_name_prefix,
        )
    
    # Convert corners to um with layer information
    segment_ports = []
    
    # Build per-segment widths using endpoint side snap + cut-density fanout.
    seg_widths = _build_segment_widths_dynamic(
        corners_3d=corners_3d,
        start_geom=start_geom,
        stop_geom=stop_geom,
        body_width=body_width,
        fallback_width=width,
        dynamic_width=dynamic_width,
    )

    # Build obstruction bboxes.
    port_points_um = [(start_x * dbu, start_y * dbu), (stop_x * dbu, stop_y * dbu)]
    m1_bboxes = []
    m2_bboxes = []
    for poly in m1_polys:
        if len(poly) >= 3:
            box = (
                float(poly[:, 0].min()) * dbu,
                float(poly[:, 1].min()) * dbu,
                float(poly[:, 0].max()) * dbu,
                float(poly[:, 1].max()) * dbu,
            )
            if not any(box[0] <= px <= box[2] and box[1] <= py <= box[3] for px, py in port_points_um):
                m1_bboxes.append(box)
    for poly in m2_polys:
        if len(poly) >= 3:
            box = (
                float(poly[:, 0].min()) * dbu,
                float(poly[:, 1].min()) * dbu,
                float(poly[:, 0].max()) * dbu,
                float(poly[:, 1].max()) * dbu,
            )
            if not any(box[0] <= px <= box[2] and box[1] <= py <= box[3] for px, py in port_points_um):
                m2_bboxes.append(box)

    geom_blocked = False
    via_pad_by_transition: Dict[int, float] = {}
    for i in range(len(corners_3d) - 1):
        x0, y0, z0 = corners_3d[i]
        _, _, z1 = corners_3d[i + 1]
        if z0 == z1:
            continue
        target_w = _transition_target_via_width(corners_3d, seg_widths, i, width)
        target_pad = _via_pad_size_um(target_w)
        base_center = (x0 * dbu, y0 * dbu)
        allow_relocate = i > 0 and (i + 1) < (len(corners_3d) - 1)
        resolved = None
        chosen_pad = None
        for via_pad in _via_pad_candidates(target_pad):
            candidate = _resolve_legal_via_center(
                base_center_um=base_center,
                via_pad_um=via_pad,
                m1_bboxes=m1_bboxes,
                m2_bboxes=m2_bboxes,
                dbu=dbu,
                relocate_step_um=max(clearance, 0.14),
                relocate_radius_um=max(1.0, 2.0 * clearance),
                max_candidates=64,
                allow_relocate=allow_relocate,
            )
            if candidate is None:
                continue
            resolved = candidate
            chosen_pad = via_pad
            break
        if resolved is None or chosen_pad is None:
            geom_blocked = True
            print(f"[3D ROUTE] Via blocked at ({base_center[0]:.3f}, {base_center[1]:.3f})")
            break
        via_pad_by_transition[i] = chosen_pad
        if chosen_pad + 1e-6 < target_pad:
            print(
                f"[3D ROUTE] Via pad stepped down at index {i} "
                f"from {target_pad:.3f}um to {chosen_pad:.3f}um"
            )
        if resolved != base_center:
            rx = int(round(resolved[0] / dbu))
            ry = int(round(resolved[1] / dbu))
            corners_3d[i] = (rx, ry, z0)
            corners_3d[i + 1] = (rx, ry, z1)
            print(
                f"[3D ROUTE] Relocated via at index {i} "
                f"from ({base_center[0]:.3f}, {base_center[1]:.3f}) "
                f"to ({resolved[0]:.3f}, {resolved[1]:.3f})"
            )

    # Build canonical primitives so every drawn shape is validated.
    plan_segments: List[Tuple[Tuple[float, float], Tuple[float, float], Tuple[int, int], float]] = []
    plan_vias: List[Tuple[Tuple[float, float], float]] = []

    def _plan_add_segment(p0: Tuple[float, float], p1: Tuple[float, float], layer: Tuple[int, int], seg_w: float) -> None:
        dx = abs(p1[0] - p0[0])
        dy = abs(p1[1] - p0[1])
        if dx < MIN_SEGMENT_LENGTH and dy < MIN_SEGMENT_LENGTH:
            return
        if dx > 0.001 and dy > 0.001:
            mid = (p1[0], p0[1]) if layer == LAYER_M1 else (p0[0], p1[1])
            _plan_add_segment(p0, mid, layer, seg_w)
            _plan_add_segment(mid, p1, layer, seg_w)
            return
        plan_segments.append((p0, p1, layer, seg_w))

    if len(corners_3d) >= 2:
        for i in range(len(corners_3d) - 1):
            x0, y0, z0 = corners_3d[i]
            x1, y1, z1 = corners_3d[i + 1]
            seg_w = seg_widths[i] if i < len(seg_widths) else width
            p0 = (x0 * dbu, y0 * dbu)
            p1 = (x1 * dbu, y1 * dbu)
            if z0 != z1:
                via_pad = via_pad_by_transition.get(
                    i,
                    _via_pad_size_um(_transition_target_via_width(corners_3d, seg_widths, i, width)),
                )
                plan_vias.append((p0, via_pad))
                _plan_add_segment(p0, p1, LAYER_M1 if z1 == 0 else LAYER_M2, seg_w)
            else:
                _plan_add_segment(p0, p1, LAYER_M1 if z0 == 0 else LAYER_M2, seg_w)

    plan_patches = _build_corner_patches_from_segments(plan_segments)

    if not geom_blocked:
        for p0, p1, layer, seg_w in plan_segments:
            seg_box = _segment_envelope_um(p0, p1, seg_w)
            target = m1_bboxes if layer == LAYER_M1 else m2_bboxes
            if any(_bbox_overlap(seg_box, obox) for obox in target):
                geom_blocked = True
                print(f"[3D ROUTE] Planned segment blocked on {'M1' if layer == LAYER_M1 else 'M2'}")
                break

    if not geom_blocked:
        for center, layer, patch_w, patch_h in plan_patches:
            patch_box = _rect_envelope_um(center, patch_w, patch_h)
            target = m1_bboxes if layer == LAYER_M1 else m2_bboxes
            if any(_bbox_overlap(patch_box, obox) for obox in target):
                geom_blocked = True
                print(f"[3D ROUTE] Planned patch blocked on {'M1' if layer == LAYER_M1 else 'M2'}")
                break

    if not geom_blocked:
        for center, via_w in plan_vias:
            if not _is_via_legal_on_both_layers(center, via_w, m1_bboxes, m2_bboxes):
                geom_blocked = True
                print(f"[3D ROUTE] Planned via blocked at ({center[0]:.3f}, {center[1]:.3f})")
                break

    if geom_blocked:
        print("[3D ROUTE] Planned geometry violates obstruction clearance; falling back to hierarchical router...")
        return route_hierarchical(
            c, start, stop,
            global_grid_unit=grid_unit * 2,
            detail_grid_unit=grid_unit,
            width=width,
            dynamic_width=dynamic_width,
            layers_to_avoid=layers_to_avoid,
            clearance=clearance,
            clearance_ladder=clearance_ladder,
            deterministic=deterministic,
            add_segment_ports=add_segment_ports,
            port_name_prefix=port_name_prefix,
        )

    segment_ports = []
    for center, layer, patch_w, patch_h in plan_patches:
        patch = c.add_ref(gf.components.rectangle(size=(patch_w, patch_h), layer=layer))
        patch.dcenter = center

    for center, via_w in plan_vias:
        via = c.add_ref(via_m1_m2(width=via_w, length=via_w))
        via.dcenter = center

    for p0, p1, layer, seg_w in plan_segments:
        is_horiz = abs(p1[1] - p0[1]) < 0.001
        if is_horiz:
            x_min = min(p0[0], p1[0])
            x_max = max(p0[0], p1[0])
            seg_len = x_max - x_min
            if seg_len >= 0.001:
                rect = c.add_ref(gf.components.rectangle(size=(seg_len, seg_w), layer=layer))
                rect.dmove((x_min, p0[1] - seg_w / 2))
                if add_segment_ports:
                    port = c.add_port(
                        name=f"{port_name_prefix}",
                        center=(x_min + seg_len / 2, p0[1]),
                        width=0.01,
                        orientation=0,
                        layer=(layer[0], 16),
                        port_type="electrical",
                    )
                    segment_ports.append(port)
                    c.draw_ports()
        else:
            y_min = min(p0[1], p1[1])
            y_max = max(p0[1], p1[1])
            seg_len = y_max - y_min
            if seg_len >= 0.001:
                rect = c.add_ref(gf.components.rectangle(size=(seg_w, seg_len), layer=layer))
                rect.dmove((p0[0] - seg_w / 2, y_min))
                if add_segment_ports:
                    port = c.add_port(
                        name=f"{port_name_prefix}",
                        center=(p0[0], y_min + seg_len / 2),
                        width=0.01,
                        orientation=90,
                        layer=(layer[0], 16),
                        port_type="electrical",
                    )
                    segment_ports.append(port)
                    c.draw_ports()

    return segment_ports


def _clear_component_routes_from_baseline(
    c: Component,
    baseline_instances: set,
    baseline_port_count: int,
) -> None:
    """Rollback route-created instances/ports to a known baseline."""
    for inst in list(c.insts):
        if inst.instance not in baseline_instances:
            inst.instance.delete()
    if len(c.ports.bases) > baseline_port_count:
        del c.ports.bases[baseline_port_count:]


def _build_deterministic_net_orders(
    nets: Sequence[RouteNetSpec],
) -> List[Tuple[RouteNetSpec, ...]]:
    """Build deterministic net ordering candidates.

    Always includes user order first, then heuristic reorderings. For small netlists,
    includes all permutations in lexicographic order of indices.
    """
    if not nets:
        return []

    idxs = list(range(len(nets)))

    def _manhattan(i: int) -> float:
        s = nets[i].start.dcenter
        t = nets[i].stop.dcenter
        return abs(float(s[0]) - float(t[0])) + abs(float(s[1]) - float(t[1]))

    seed_orders: List[Tuple[int, ...]] = [tuple(idxs)]
    seed_orders.append(tuple(sorted(idxs, key=lambda i: (-_manhattan(i), i))))
    seed_orders.append(tuple(sorted(idxs, key=lambda i: (_manhattan(i), i))))
    seed_orders.append(tuple(reversed(idxs)))

    if len(nets) <= 6:
        seed_orders.extend(permutations(idxs))

    dedup: List[Tuple[int, ...]] = []
    seen = set()
    for ord_idxs in seed_orders:
        if ord_idxs in seen:
            continue
        seen.add(ord_idxs)
        dedup.append(ord_idxs)

    return [tuple(nets[i] for i in ord_idxs) for ord_idxs in dedup]


def route_nets_deterministic(
    c: Component,
    nets: Sequence[RouteNetSpec],
    grid_unit: float = 1.0,
    width: float = 0.25,
    dynamic_width: bool = True,
    layers_to_avoid: Iterable[LayerSpec] = None,
    via_cost: float = 10.0,
    wrong_way_penalty: float = 8.0,
    clearance: float = 0.14,
    clearance_ladder: Tuple[float, ...] = (0.14, 0.10, 0.07),
    deterministic: bool = True,
    add_segment_ports: bool = True,
    require_all: bool = True,
) -> Dict[str, List[Port]]:
    """Deterministically route multiple nets with whole-attempt rollback/retry.

    This guarantees no partial geometry is left behind from failed attempts.
    """
    if layers_to_avoid is None:
        layers_to_avoid = []
    if not nets:
        return {}

    baseline_instances = {inst.instance for inst in c.insts}
    baseline_port_count = len(c.ports.bases)
    net_orders = _build_deterministic_net_orders(nets)

    best_partial: Dict[str, List[Port]] = {}

    for attempt_idx, ordered_nets in enumerate(net_orders, start=1):
        if attempt_idx > 1:
            _clear_component_routes_from_baseline(c, baseline_instances, baseline_port_count)
        print(
            f"[MULTINET] Attempt {attempt_idx}/{len(net_orders)} order="
            f"{','.join(net.name for net in ordered_nets)}"
        )

        routed: Dict[str, List[Port]] = {}
        failed_name: Optional[str] = None

        for net in ordered_nets:
            before_inst = len(c.insts)
            before_ports = len(c.ports.bases)
            seg_ports = route_multilayer_3d(
                c,
                start=net.start,
                stop=net.stop,
                grid_unit=grid_unit,
                width=width,
                dynamic_width=dynamic_width,
                layers_to_avoid=layers_to_avoid,
                add_segment_ports=add_segment_ports,
                port_name_prefix=net.port_name_prefix,
                via_cost=via_cost,
                wrong_way_penalty=wrong_way_penalty,
                clearance=clearance,
                clearance_ladder=clearance_ladder,
                deterministic=deterministic,
            )
            after_inst = len(c.insts)
            after_ports = len(c.ports.bases)
            success = after_inst > before_inst
            if not success:
                if after_ports > before_ports:
                    del c.ports.bases[before_ports:]
                failed_name = net.name
                print(f"[MULTINET] net '{net.name}' failed in attempt {attempt_idx}")
                break
            routed[net.name] = seg_ports

        if failed_name is None and len(routed) == len(nets):
            print(f"[MULTINET] Success on attempt {attempt_idx}")
            return routed

        if len(routed) > len(best_partial):
            best_partial = routed

    if require_all:
        raise RuntimeError(
            "[MULTINET] Unable to complete all requested nets without obstruction conflicts."
        )
    return best_partial


def route_nets_deterministic_copy(
    c: Component,
    nets: Sequence[RouteNetSpec],
    grid_unit: float = 1.0,
    width: float = 0.25,
    dynamic_width: bool = True,
    layers_to_avoid: Iterable[LayerSpec] = None,
    via_cost: float = 10.0,
    wrong_way_penalty: float = 8.0,
    clearance: float = 0.14,
    clearance_ladder: Tuple[float, ...] = (0.14, 0.10, 0.07),
    deterministic: bool = True,
    add_segment_ports: bool = True,
    require_all: bool = True,
) -> Tuple[Component, Dict[str, List[Port]]]:
    """Deterministically route multiple nets on copy-attempts.

    Avoids in-place rip-up side effects by evaluating each net-order attempt on
    a fresh `Component.copy()`.
    """
    if layers_to_avoid is None:
        layers_to_avoid = []
    if not nets:
        return c.copy(), {}

    net_orders = _build_deterministic_net_orders(nets)
    best_trial: Optional[Component] = None
    best_partial: Dict[str, List[Port]] = {}

    for attempt_idx, ordered_nets in enumerate(net_orders, start=1):
        trial = c.copy()
        print(
            f"[MULTINET-COPY] Attempt {attempt_idx}/{len(net_orders)} order="
            f"{','.join(net.name for net in ordered_nets)}"
        )

        routed: Dict[str, List[Port]] = {}
        failed_name: Optional[str] = None

        for net in ordered_nets:
            before_inst = len(trial.insts)
            seg_ports = route_multilayer_3d(
                trial,
                start=net.start,
                stop=net.stop,
                grid_unit=grid_unit,
                width=width,
                dynamic_width=dynamic_width,
                layers_to_avoid=layers_to_avoid,
                add_segment_ports=add_segment_ports,
                port_name_prefix=net.port_name_prefix,
                via_cost=via_cost,
                wrong_way_penalty=wrong_way_penalty,
                clearance=clearance,
                clearance_ladder=clearance_ladder,
                deterministic=deterministic,
            )
            success = len(trial.insts) > before_inst
            if not success:
                failed_name = net.name
                print(f"[MULTINET-COPY] net '{net.name}' failed in attempt {attempt_idx}")
                break
            routed[net.name] = seg_ports

        if failed_name is None and len(routed) == len(nets):
            print(f"[MULTINET-COPY] Success on attempt {attempt_idx}")
            return trial, routed

        if len(routed) > len(best_partial):
            best_partial = routed
            best_trial = trial

    if require_all:
        raise RuntimeError(
            "[MULTINET-COPY] Unable to complete all requested nets without obstruction conflicts."
        )
    return (best_trial if best_trial is not None else c.copy()), best_partial
