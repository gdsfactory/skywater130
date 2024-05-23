
from hdl21.pdk import register

# Grab our primary PDK-definition module
from . import pdk_logic
from .pdk_logic import *

# The optional external-data installation.
# Set by an instantiator of `Install`, if available.
install: Install | None = None

# And register as a PDK module
register(pdk_logic)
