# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Layout
#
# ## Layout driven flow
#
# You can import the PDK and layout any of the standard cells

import gdsfactory as gf

import sky130.components as sc
import sky130.tech as st

c = sc.sky130_fd_sc_hd__a2111o_1()
c

scene = c.to_3d()
scene.show()

# TODO: add Parametric cells natively into gdsfactory `sky130` pdk.

c = gf.Component()
g1 = c << sc.sky130_fd_sc_hd__a2111o_1()
g2 = c << sc.sky130_fd_sc_hd__a311oi_4()
g2.move((15, 10))
c

c = gf.Component("demo_connect")
g1 = c << sc.sky130_fd_sc_hd__a2111o_1()
g2 = c << sc.sky130_fd_sc_hd__a311oi_4()
g2.move((15, 10))
route = gf.routing.get_route_electrical(
    g1.ports["VPWR"], g2.ports["VPWR"], cross_section=st.xs_metal1
)
c.add(route.references)
c

scene = c.to_3d()
scene.show()

# ## Netlist driven flow
#
# For netlist driven flow you can define circuits for place and route. You have two options:
#
# 1. in python
# 2. in YAML

# ## Spice simulations
#
# You can use `PySpice` for running simulations.
#
# gdsfactory can extract the netlist and simulate the circuit.
#
# TODO: add some relevant examples.
