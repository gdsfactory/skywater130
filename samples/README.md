# Samples

This directory contains example SPICE simulations demonstrating various circuit analysis techniques using the Sky130 PDK and PySpice.

## Examples

### RC Filter (`rc_filter.py`)

A comprehensive example demonstrating RC low-pass filter simulation with:

- **Transient Analysis**: Step response showing exponential charging behavior
- **AC Analysis**: Frequency response showing magnitude and phase characteristics
- **Pulse Response**: Square wave filtering to demonstrate smoothing effect

#### Key Features:
- Circuit parameters: R = 1kΩ, C = 100nF (cutoff frequency ≈ 1.59 kHz)
- Multiple analysis types in a single script
- Professional plotting with time constants and cutoff frequency annotations
- Educational comments explaining RC filter theory
- **Requires ngspice** for actual simulation

#### Running the Example:

```bash
# From the project root directory
python samples/rc_filter.py
```

#### Expected Output:
- If ngspice is installed: Two matplotlib windows with simulation results
- If ngspice is missing: Error messages with installation instructions
- Console output showing theoretical calculations and analysis progress

### RC Filter Theoretical (`rc_filter_theoretical.py`)

A theoretical analysis of RC filter behavior **without requiring ngspice simulation**:

- **Step Response**: Theoretical exponential charging curves for different RC values
- **Frequency Response**: Calculated magnitude and phase plots
- **Pulse Response**: Theoretical square wave filtering analysis

#### Key Features:
- No ngspice dependency - works with just Python, matplotlib, and numpy
- Multiple RC combinations showing different time constants
- Educational analysis of RC filter principles
- Perfect for learning filter theory without simulation setup

#### Running the Example:

```bash
# From the project root directory
python samples/rc_filter_theoretical.py
```

#### Expected Output:
- Three matplotlib windows showing theoretical analyses
- Console output explaining RC filter principles and calculations

### RC Filter Analysis Notebook (`rc_filter_analysis.ipynb`)

A comprehensive **Jupyter notebook** combining theoretical analysis and SPICE simulation:

- **Interactive Learning**: Step-by-step explanation with live code
- **Theory + Practice**: Combines mathematical analysis with simulation
- **Graceful Degradation**: Works with or without ngspice installed
- **Rich Visualization**: Professional plots with detailed explanations

#### Key Features:
- Interactive parameter exploration
- Comparison between theory and SPICE simulation
- HTML tables summarizing key formulas
- Educational markdown explanations
- Error handling for missing dependencies

#### Running the Notebook:

```bash
# From the project root directory
jupyter notebook samples/rc_filter_analysis.ipynb
# or
jupyter lab samples/rc_filter_analysis.ipynb
```

#### Requirements:
- Jupyter notebook or JupyterLab
- All the same dependencies as other examples
- Optional: ngspice for SPICE simulation cells

#### Circuit Topology:
```
VIN ---[R]---+--- VOUT
             |
            [C]
             |
            GND
```

## Requirements

All examples require:
- PySpice
- matplotlib
- numpy
- **ngspice** (system dependency - not a Python package)

The Python dependencies are included in the main project's requirements, but ngspice must be installed separately on your system.

### Installing ngspice

**macOS:**
```bash
brew install ngspice
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ngspice
```

**Windows:**
Download and install from: http://ngspice.sourceforge.net/download.html

**Note:** Without ngspice, the examples will show circuit creation and theoretical calculations but cannot run actual SPICE simulations.

## Adding New Examples

When adding new examples:
1. Create a descriptive filename (e.g., `amplifier_analysis.py`)
2. Include comprehensive docstrings explaining the circuit and analysis
3. Add educational comments throughout the code
4. Update this README with a description of the new example
5. Follow the existing code style and structure
