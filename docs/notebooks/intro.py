# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Layout
#
# ## Layout driven flow
#
# You can import the PDK and layout any of the standard cells

# %%
import gdsfactory as gf
from gdsfactory.config import rich_output
gf.config.rich_output()

# %%
import sky130
import sky130.components as sc
import sky130.tech as st

# %% [markdown]
# If you want to see what are the cells available:

# %%
# sky130.cells

# %%
# sky130.cross_sections

# %% [markdown]
# Let's explore the available layers:

# %%
# help(gf.pdk)
# help(gf.get_active_pdk().get_layer_stack)
# gf.pdk.get_layer_stack()

# %% [markdown]
# You can also verify this is the active PDK on `gdsfactory`:

# %%
gf.pdk.get_active_pdk().name

# %% [markdown]
# Now, let's explore available symbols for the components:

# %%
# dir(sky130)
sky130

# %% [markdown]
# Let's try exploring an example basic `nfet`:

# %%
c = sc.sky130_fd_pr__rf_nfet_01v8_aM02W1p65L0p15()
c

# %% [markdown]
# Explore it's ports:

# %%
c.ports

# %% [markdown]
# We can also explore the digital cells:

# %%
c = sc.sky130_fd_sc_hd__a2111o_1()
c

# %%
scene = c.to_3d()
scene.show()

# %% [markdown]
# TODO: add Parametric cells natively into gdsfactory `sky130` pdk.

# %%
c = gf.Component()
g1 = c << sc.sky130_fd_sc_hd__a2111o_1()
g2 = c << sc.sky130_fd_sc_hd__a311oi_4()
g2.move((15, 10))
c

# %%
c = gf.Component("demo_connect")
g1 = c << sc.sky130_fd_sc_hd__a2111o_1()
g2 = c << sc.sky130_fd_sc_hd__a311oi_4()
g2.move((15, 10))
route = gf.routing.get_route_electrical(
    g1.ports["VPWR"], g2.ports["VPWR"], cross_section=st.xs_metal1
)
c.add(route.references)
c

# %%
scene = c.to_3d()
scene.show()

# %% [markdown]
# ## Netlist driven flow
#
# For netlist driven flow you can define circuits for place and route. You have two options:
#
# 1. in python
# 2. in YAML

# %% [markdown]
# ## Spice simulations
#
# You can use `PySpice` for running simulations.
#
# gdsfactory can extract the netlist and simulate the circuit.
#
# TODO: add some relevant examples.
