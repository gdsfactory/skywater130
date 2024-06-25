import os

# Define the PDK directories
pdk_directories = ["src/sky130_fd_pr", "src/sky130_fd_sc_hd"]


# List to store gds file paths


def compile_components(pdk_directories=pdk_directories):
    """Compile the components from the PDK directories into a Python file."""
    gds_files = []

    # Walk through the PDK directories and collect GDS files
    for pdk_dir in pdk_directories:
        for subdir, _, files in os.walk(pdk_dir):
            for file in files:
                if file.endswith(".gds"):
                    gds_files.append(os.path.join(subdir, file))

    # Function to create Python code for each gds file
    def create_code(file_path):
        file_name = os.path.basename(file_path)
        raw_cell_name = os.path.splitext(file_name)[0]

        for pdk_dir in pdk_directories:
            prefix = pdk_dir.split("/")[-1] + "__"
            if raw_cell_name.startswith(prefix):
                cell_name = raw_cell_name[len(prefix) :]
                break

        # For old compatibility:
        cell_name = raw_cell_name

        code = f"""
@cell
def {cell_name}() -> gf.Component:
    \"\"\"Returns {cell_name} fixed cell.

    .. plot::
      :include-source:

      import sky130

      c = sky130.components.{cell_name}()
      c.plot()
    \"\"\"
    return import_gds(gdsdir / "{file_path}", cellname="{raw_cell_name}")
"""
        return code

    # Prelude to add at the top of the file
    prelude = """from functools import partial
import gdsfactory as gf
from gdsfactory import cell

from sky130.config import PATH
from sky130.layers import LAYER

add_ports_m1 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met1drawing,
    layer_label=LAYER.met1label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=True,
)
add_ports_m2 = gf.partial(
    gf.add_ports.add_ports_from_labels,
    port_layer=LAYER.met2drawing,
    layer_label=LAYER.met2label,
    port_type="electrical",
    port_width=0.2,
    get_name_from_label=True,
    guess_port_orientation=True,
)
add_ports = gf.compose(add_ports_m1, add_ports_m2)

gdsdir = PATH.module
import_gds = partial(gf.import_gds, post_process=add_ports)
"""

    # TODO delete old file automatically
    # Write the code to a Python file
    with open("components.py", "w") as f:
        f.write(prelude)
        for gds_file in gds_files:
            print(gds_file)
            # gds_file = os.path.dirname(str(pathlib.Path(gds_file)))
            code = create_code(gds_file)
            f.write(code)

    print("Python file 'components.py' has been created.")


if __name__ == "__main__":
    compile_components()
#     # gf.write_cells.write_cells(gdspath=PATH.gdshd, dirpath="gds")
#     # gf.write_cells.write_cells(gdspath=PATH.gdshs, dirpath="gds")
#     # gf.write_cells.write_cells(gdspath=PATH.gdshvl, dirpath="gds")
#     # print(gf.write_cells.get_import_gds_script(PATH.gds))
#     # c = sky130_fd_sc_hvl__xor2_1()
#     # c = sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2()
#     c = sky130_fd_sc_hd__conb_1()
#     # c.show()
#     c.show()
