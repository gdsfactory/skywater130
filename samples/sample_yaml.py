sample_yaml = """
instances:
  a2:
    component: sky130_fd_sc_hd__a2111oi_0

  a3:
    component: sky130_fd_sc_hd__a311o_2

placements:
  a2:
    xmin: 30
  a3:
    xmin: a2,east
    dx: 10
    dy: 20

routes:
  bundle:
    links:
      a2,VGND: a3,VGND
    routing_strategy: route_bundle
    settings:
      cross_section: metal1
"""


if __name__ == "__main__":
    import gdsfactory as gf

    from sky130 import PDK

    PDK.activate()
    c = gf.read.from_yaml(sample_yaml)
    c.show()
