"""RC Filter SPICE Simulation Example

This example demonstrates how to simulate an RC low-pass filter using PySpice.
It includes both transient analysis (step response) and AC analysis (frequency response).

Requirements:
- PySpice
- ngspice (system dependency)
- matplotlib
- numpy

Installation on macOS:
    brew install ngspice

Installation on Ubuntu/Debian:
    sudo apt-get install ngspice

Installation on Windows:
    Download ngspice from http://ngspice.sourceforge.net/download.html
"""

import matplotlib.pyplot as plt
import numpy as np
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import (
    u_Hz,
    u_kHz,
    u_kOhm,
    u_ms,
    u_nF,
    u_us,
    u_V,
)


def create_rc_filter_circuit():
    """Create an RC low-pass filter circuit.

    Circuit topology:
    VIN ---[R]---+--- VOUT
                 |
                [C]
                 |
                GND
    """
    circuit = Circuit("RC Low-Pass Filter")

    # Circuit parameters
    R = 1 @ u_kOhm  # 1 kΩ resistor
    C = 100 @ u_nF  # 100 nF capacitor

    # Calculate cutoff frequency: fc = 1/(2πRC)
    R_value = float(R)  # R is in Ohms (1000)
    C_value = float(C)  # C is in Farads (100e-9)
    cutoff_freq = 1 / (2 * np.pi * R_value * C_value)  # Hz
    print(f"Theoretical cutoff frequency: {cutoff_freq:.1f} Hz")

    # Circuit elements
    circuit.R("1", "vin", "vout", R)
    circuit.C("1", "vout", circuit.gnd, C)

    return circuit, cutoff_freq


def run_transient_analysis():
    """Run transient analysis with step input to see RC charging."""
    print("\n=== Transient Analysis (Step Response) ===")

    circuit, _ = create_rc_filter_circuit()

    # Step voltage source: 0V to 1V step at t=0
    circuit.V("in", "vin", circuit.gnd, 1 @ u_V)

    # Note: Capacitor starts uncharged by default in transient analysis

    # Simulation
    try:
        simulator = circuit.simulator()
        analysis = simulator.transient(
            step_time=10 @ u_us,  # 10 μs time steps
            end_time=1 @ u_ms,  # Simulate for 1 ms
        )
    except Exception as e:
        print(f"Error during simulation: {e}")
        print("Make sure ngspice is installed on your system.")
        print("See the installation instructions in the file header.")
        return None

    # Plot results
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.title("RC Filter Step Response")
    plt.plot(
        analysis.time * 1e3, analysis["vin"], "b-", label="Input (VIN)", linewidth=2
    )
    plt.plot(
        analysis.time * 1e3, analysis["vout"], "r-", label="Output (VOUT)", linewidth=2
    )
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (V)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Calculate and show time constant
    # τ = RC, voltage reaches ~63.2% of final value at t = τ
    time_constant = 1e3 * 100e-9  # R (1kΩ) * C (100nF) in seconds
    final_voltage = 1.0  # Step input voltage
    tau_voltage = final_voltage * (1 - np.exp(-1))  # ~0.632V

    plt.axhline(
        y=tau_voltage,
        color="g",
        linestyle="--",
        alpha=0.7,
        label=f"τ = {time_constant * 1e3:.2f} ms (63.2%)",
    )
    plt.axvline(x=time_constant * 1e3, color="g", linestyle="--", alpha=0.7)

    return analysis


def run_ac_analysis():
    """Run AC analysis to get frequency response."""
    print("\n=== AC Analysis (Frequency Response) ===")

    circuit, cutoff_freq = create_rc_filter_circuit()

    # AC voltage source
    circuit.V("in", "vin", circuit.gnd, "AC 1")  # 1V AC source

    # Simulation
    try:
        simulator = circuit.simulator()
        analysis = simulator.ac(
            start_frequency=10 @ u_Hz,  # Start from 10 Hz
            stop_frequency=100 @ u_kHz,  # Go up to 100 kHz
            number_of_points=50,  # 50 points per decade
            variation="dec",  # Decade (logarithmic) sweep
        )
    except Exception as e:
        print(f"Error during simulation: {e}")
        print("Make sure ngspice is installed on your system.")
        return None

    # Calculate magnitude and phase
    frequency = analysis.frequency
    vout_complex = analysis["vout"]
    magnitude_db = 20 * np.log10(np.abs(vout_complex))
    phase_deg = np.angle(vout_complex) * 180 / np.pi

    # Plot frequency response
    plt.subplot(2, 1, 2)

    # Magnitude plot
    plt.semilogx(frequency, magnitude_db, "b-", linewidth=2, label="Magnitude")
    plt.axvline(
        x=cutoff_freq,
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"fc = {cutoff_freq:.1f} Hz (-3dB)",
    )
    plt.axhline(y=-3, color="r", linestyle="--", alpha=0.7)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title("RC Filter Frequency Response")
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Add phase plot as inset
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes

    ax_phase = inset_axes(plt.gca(), width="40%", height="40%", loc="lower left")
    ax_phase.semilogx(frequency, phase_deg, "g-", linewidth=2)
    ax_phase.axvline(x=cutoff_freq, color="r", linestyle="--", alpha=0.7)
    ax_phase.axhline(y=-45, color="r", linestyle="--", alpha=0.7)
    ax_phase.set_xlabel("Frequency (Hz)", fontsize=8)
    ax_phase.set_ylabel("Phase (°)", fontsize=8)
    ax_phase.grid(True, alpha=0.3)
    ax_phase.tick_params(labelsize=7)

    return analysis


def run_pulse_response():
    """Run transient analysis with pulse input to see filtering effect."""
    print("\n=== Pulse Response Analysis ===")

    circuit, cutoff_freq = create_rc_filter_circuit()

    # Pulse voltage source: square wave
    circuit.PulseVoltageSource(
        "in",
        "vin",
        circuit.gnd,
        initial_value=0 @ u_V,
        pulsed_value=1 @ u_V,
        rise_time=1 @ u_us,  # Fast rise time
        fall_time=1 @ u_us,  # Fast fall time
        pulse_width=100 @ u_us,  # 100 μs pulse width
        period=200 @ u_us,  # 200 μs period (5 kHz)
        delay_time=50 @ u_us,  # Start after 50 μs
    )

    # Simulation
    try:
        simulator = circuit.simulator()
        analysis = simulator.transient(
            step_time=1 @ u_us,  # 1 μs time steps
            end_time=500 @ u_us,  # Simulate for 500 μs
        )
    except Exception as e:
        print(f"Error during simulation: {e}")
        print("Make sure ngspice is installed on your system.")
        return None

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.plot(
        analysis.time * 1e6, analysis["vin"], "b-", label="Input (VIN)", linewidth=2
    )
    plt.plot(
        analysis.time * 1e6, analysis["vout"], "r-", label="Output (VOUT)", linewidth=2
    )
    plt.xlabel("Time (μs)")
    plt.ylabel("Voltage (V)")
    plt.title("RC Filter Pulse Response (Square Wave Input)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    return analysis


def main():
    """Run all RC filter simulations."""
    print("RC Filter SPICE Simulation Example")
    print("=" * 40)

    # Check if simulations can run
    errors = 0

    # Run transient analysis
    transient_analysis = run_transient_analysis()
    if transient_analysis is None:
        errors += 1

    # Run AC analysis
    ac_analysis = run_ac_analysis()
    if ac_analysis is None:
        errors += 1

    if errors == 0:
        plt.tight_layout()
        plt.show()

        # Run pulse response
        pulse_analysis = run_pulse_response()
        if pulse_analysis is not None:
            plt.show()

        print("\nSimulation completed!")
        print("\nKey observations:")
        print("1. Step response shows exponential charging with time constant τ = RC")
        print(
            "2. Frequency response shows -3dB at cutoff frequency and -20dB/decade rolloff"
        )
        print(
            "3. Pulse response demonstrates the filtering (smoothing) effect on square waves"
        )
    else:
        print(f"\n{errors} simulation(s) failed due to missing ngspice library.")
        print("\nTo install ngspice:")
        print("  macOS: brew install ngspice")
        print("  Ubuntu/Debian: sudo apt-get install ngspice")
        print("  Windows: Download from http://ngspice.sourceforge.net/download.html")


if __name__ == "__main__":
    main()
