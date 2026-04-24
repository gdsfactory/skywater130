"""Tests for sky130/pcells/contact.py — shared contact/via array generator."""

from sky130.layers import LAYER
from sky130.pcells.contact import contact_array, licon_array, mcon_array


def test_contact_array_single():
    """Minimum area should produce exactly 1 contact."""
    # Minimum: width = 2*enc + size = 2*0.06 + 0.17 = 0.29
    # Use slightly larger (0.30) to avoid floating point edge case
    c = contact_array(width=0.30, height=0.30)
    polys = c.get_polygons()
    contacts = polys[LAYER.licon1drawing]
    assert len(contacts) == 1


def test_contact_array_2x2():
    """Sufficient space should produce a 2x2 grid (4 contacts)."""
    # For nc=2: avail_w >= 2*size + spacing = 2*0.17 + 0.17 = 0.51
    # Use avail=0.52 → width = 0.52 + 2*0.06 = 0.64 to avoid FP edge case
    c = contact_array(width=0.64, height=0.64)
    polys = c.get_polygons()
    contacts = polys[LAYER.licon1drawing]
    assert len(contacts) == 4


def test_contact_array_floor_rounding():
    """Area barely too small for 3 cols should give 2 cols (proves floor, not ceil)."""
    # For 3 cols: avail_w needs 3*0.17 + 2*0.17 = 0.85
    # Use avail_w = 0.84 → width = 0.84 + 2*0.06 = 0.96 → floor gives nc=2
    # The old ceil formula (ceil(width/(size+spacing)) = ceil(0.96/0.34) = 3) would give 3
    c = contact_array(width=0.96, height=0.30)
    polys = c.get_polygons()
    contacts = polys[LAYER.licon1drawing]
    # Floor rounding: 2 columns x 1 row = 2 contacts
    assert len(contacts) == 2


def test_contact_array_centering():
    """Contacts should be centered within the enclosing area."""
    # Use 0.50 x 0.50 area, which fits 1 contact (0.17x0.17)
    # enc=0.06 on each side → ox = oy = (0.50 - 0.17) / 2 = 0.165
    width = 0.50
    height = 0.50
    c = contact_array(width=width, height=height)
    polys = c.get_polygons()
    contacts = polys[LAYER.licon1drawing]
    assert len(contacts) == 1

    # Extract bounding box of the single contact polygon (in nm)
    poly = contacts[0]
    pts = [(pt.x, pt.y) for pt in poly.each_point_hull()]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x_min = min(xs)
    y_min = min(ys)

    # Contact width/height in database units (1nm = 1 DBU)
    contact_w_nm = 0.17 * 1000
    contact_h_nm = 0.17 * 1000
    area_w_nm = width * 1000
    area_h_nm = height * 1000

    expected_ox = (area_w_nm - contact_w_nm) / 2
    expected_oy = (area_h_nm - contact_h_nm) / 2

    assert abs(x_min - expected_ox) < 1, f"x offset {x_min} != expected {expected_ox}"
    assert abs(y_min - expected_oy) < 1, f"y offset {y_min} != expected {expected_oy}"


def test_licon_defaults():
    """licon_array should place contacts on LAYER.licon1drawing."""
    c = licon_array(width=0.30, height=0.30)
    polys = c.get_polygons()
    assert LAYER.licon1drawing in polys
    assert len(polys[LAYER.licon1drawing]) >= 1


def test_mcon_defaults():
    """mcon_array should place contacts on LAYER.mcondrawing."""
    c = mcon_array(width=0.30, height=0.30)
    polys = c.get_polygons()
    assert LAYER.mcondrawing in polys
    assert len(polys[LAYER.mcondrawing]) >= 1
