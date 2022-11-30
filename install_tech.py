"""Symlink tech to klayout."""

import shutil
import sys
import os
import subprocess
import pathlib


def remove_path_or_dir(dest: pathlib.Path):
    if dest.is_dir():
        if dest.is_symlink():
            os.unlink(dest)
        else:
            shutil.rmtree(dest)
    else:
        os.remove(dest)


def make_link(src, dest, overwrite: bool = True) -> None:
    dest = pathlib.Path(dest)
    if dest.exists() and not overwrite:
        print(f"{dest} already exists")
        return
    if dest.exists() or dest.is_symlink():
        print(f"removing {dest} already installed")
        remove_path_or_dir(dest)
    try:
        os.symlink(src, dest, target_is_directory=True)
    except OSError as err:
        print("Could not create symlink!")
        print("     Error: ", err)
        if sys.platform == "win32":
            # https://stackoverflow.com/questions/32877260/privlege-error-trying-to-create-symlink-using-python-on-windows-10
            print("Trying to create a junction instead of a symlink...")
            proc = subprocess.check_call(f"mklink /J {dest} {src}", shell=True)
            if proc != 0:
                print("Could not create link!")
    print("Symlink made:")
    print(f"From: {src}")
    print(f"To:   {dest}")


if __name__ == "__main__":
    klayout_folder = "KLayout" if sys.platform == "win32" else ".klayout"
    cwd = pathlib.Path(__file__).resolve().parent
    home = pathlib.Path.home()
    src = cwd / "sky130" / "klayout" / "sky130"
    dest_folder = home / klayout_folder / "tech"
    dest_folder.mkdir(exist_ok=True, parents=True)
    dest = dest_folder / "sky130"
    make_link(src=src, dest=dest)
