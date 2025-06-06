"""Theoretical RC Filter Analysis

This example demonstrates RC filter theory and calculations without requiring
ngspice simulation. It shows theoretical responses and circuit analysis principles.
"""

import matplotlib.pyplot as plt
import numpy as np


def calculate_rc_parameters(R, C):
    """Calculate RC filter parameters.

    Args:
        R: Resistance in Ohms
        C: Capacitance in Farads

    Returns:
        dict: Dictionary with calculated parameters
    """
    params = {}

    # Time constant
    params["tau"] = R * C  # seconds

    # Cutoff frequency
    params["fc"] = 1 / (2 * np.pi * R * C)  # Hz
    params["wc"] = 2 * np.pi * params["fc"]  # rad/s

    # 3dB frequency (same as cutoff)
    params["f_3db"] = params["fc"]

    return params


def theoretical_step_response(R, C, t_max=None, n_points=1000):
    """Calculate theoretical step response of RC filter.

    Args:
        R: Resistance in Ohms
        C: Capacitance in Farads
        t_max: Maximum time (if None, use 5*tau)
        n_points: Number of time points

    Returns:
        tuple: (time_array, voltage_response)
    """
    tau = R * C

    if t_max is None:
        t_max = 5 * tau  # Go to 5 time constants

    t = np.linspace(0, t_max, n_points)

    # Step response: v_out(t) = V_in * (1 - exp(-t/tau))
    # For unit step input (V_in = 1V)
    v_out = 1 - np.exp(-t / tau)

    return t, v_out


def theoretical_frequency_response(R, C, f_min=1, f_max=1e6, n_points=1000):
    """Calculate theoretical frequency response of RC filter.

    Args:
        R: Resistance in Ohms
        C: Capacitance in Farads
        f_min: Minimum frequency in Hz
        f_max: Maximum frequency in Hz
        n_points: Number of frequency points

    Returns:
        tuple: (frequency, magnitude_db, phase_deg)
    """
    f = np.logspace(np.log10(f_min), np.log10(f_max), n_points)
    omega = 2 * np.pi * f

    # Transfer function: H(jω) = 1 / (1 + jωRC)
    wc = 1 / (R * C)  # Cutoff frequency in rad/s
    H = 1 / (1 + 1j * omega / wc)

    # Magnitude in dB
    magnitude_db = 20 * np.log10(np.abs(H))

    # Phase in degrees
    phase_deg = np.angle(H) * 180 / np.pi

    return f, magnitude_db, phase_deg


def plot_step_response():
    """Plot theoretical step response for different RC values."""
    print("=== Theoretical Step Response Analysis ===")

    # Different RC combinations
    circuits = [
        {"R": 1e3, "C": 100e-9, "label": "R=1kΩ, C=100nF"},
        {"R": 10e3, "C": 10e-9, "label": "R=10kΩ, C=10nF"},
        {"R": 100, "C": 1e-6, "label": "R=100Ω, C=1μF"},
    ]

    plt.figure(figsize=(12, 8))

    for i, circuit in enumerate(circuits):
        R, C = circuit["R"], circuit["C"]
        params = calculate_rc_parameters(R, C)

        # Calculate response
        t, v_out = theoretical_step_response(R, C)

        # Plot
        plt.subplot(2, 2, i + 1)
        plt.plot(t * 1e3, v_out, "b-", linewidth=2, label="Output")
        plt.axhline(y=1, color="r", linestyle="--", alpha=0.7, label="Input (1V step)")
        plt.axhline(y=0.632, color="g", linestyle="--", alpha=0.7, label="63.2% (τ)")
        plt.axvline(x=params["tau"] * 1e3, color="g", linestyle="--", alpha=0.7)

        plt.title(
            f"{circuit['label']}\nτ = {params['tau'] * 1e3:.2f} ms, fc = {params['fc']:.1f} Hz"
        )
        plt.xlabel("Time (ms)")
        plt.ylabel("Voltage (V)")
        plt.grid(True, alpha=0.3)
        plt.legend()

        print(f"Circuit {i + 1}: {circuit['label']}")
        print(f"  Time constant: {params['tau'] * 1e3:.2f} ms")
        print(f"  Cutoff frequency: {params['fc']:.1f} Hz")
        print()

    plt.tight_layout()
    return plt.gcf()


def plot_frequency_response():
    """Plot theoretical frequency response."""
    print("=== Theoretical Frequency Response Analysis ===")

    # Circuit parameters
    R = 1e3  # 1 kΩ
    C = 100e-9  # 100 nF

    params = calculate_rc_parameters(R, C)
    f, magnitude_db, phase_deg = theoretical_frequency_response(R, C)

    plt.figure(figsize=(12, 8))

    # Magnitude plot
    plt.subplot(2, 1, 1)
    plt.semilogx(f, magnitude_db, "b-", linewidth=2)
    plt.axvline(
        x=params["fc"],
        color="r",
        linestyle="--",
        alpha=0.7,
        label=f"fc = {params['fc']:.1f} Hz",
    )
    plt.axhline(y=-3, color="r", linestyle="--", alpha=0.7, label="-3dB")
    plt.title(f"RC Filter Frequency Response (R={R / 1e3:.0f}kΩ, C={C * 1e9:.0f}nF)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(-60, 5)

    # Phase plot
    plt.subplot(2, 1, 2)
    plt.semilogx(f, phase_deg, "g-", linewidth=2)
    plt.axvline(x=params["fc"], color="r", linestyle="--", alpha=0.7)
    plt.axhline(y=-45, color="r", linestyle="--", alpha=0.7, label="-45° at fc")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (degrees)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.ylim(-95, 5)

    plt.tight_layout()

    print(f"Cutoff frequency: {params['fc']:.1f} Hz")
    print(f"Time constant: {params['tau'] * 1e3:.2f} ms")
    print("At fc: Magnitude = -3dB, Phase = -45°")
    print("Rolloff rate: -20 dB/decade above fc")

    return plt.gcf()


def analyze_pulse_response():
    """Analyze theoretical pulse response."""
    print("=== Theoretical Pulse Response Analysis ===")

    R = 1e3  # 1 kΩ
    C = 100e-9  # 100 nF
    params = calculate_rc_parameters(R, C)

    # Pulse parameters
    pulse_width = 200e-6  # 200 μs
    pulse_period = 400e-6  # 400 μs (2.5 kHz)

    # Time array
    t_max = 1e-3  # 1 ms
    t = np.linspace(0, t_max, 10000)

    # Generate square wave input
    v_in = np.zeros_like(t)
    for i, time in enumerate(t):
        cycle_time = time % pulse_period
        if cycle_time < pulse_width:
            v_in[i] = 1.0

    # Calculate response (simplified - assumes linear superposition)
    # For more accurate results, would need to solve differential equation
    v_out = np.zeros_like(t)
    tau = params["tau"]

    # Simple approximation using exponential charging/discharging
    v_out[0] = 0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        if v_in[i] > v_in[i - 1]:  # Rising edge
            v_out[i] = v_out[i - 1] + (v_in[i] - v_out[i - 1]) * (1 - np.exp(-dt / tau))
        elif v_in[i] < v_in[i - 1]:  # Falling edge
            v_out[i] = v_out[i - 1] * np.exp(-dt / tau)
        else:  # Steady state
            v_out[i] = v_out[i - 1] + (v_in[i] - v_out[i - 1]) * (1 - np.exp(-dt / tau))

    plt.figure(figsize=(12, 6))
    plt.plot(t * 1e6, v_in, "b-", linewidth=2, label="Input (Square Wave)")
    plt.plot(t * 1e6, v_out, "r-", linewidth=2, label="Output (Filtered)")
    plt.xlabel("Time (μs)")
    plt.ylabel("Voltage (V)")
    plt.title(
        f"RC Filter Pulse Response\n(R={R / 1e3:.0f}kΩ, C={C * 1e9:.0f}nF, τ={params['tau'] * 1e6:.0f}μs)"
    )
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    print(f"Pulse width: {pulse_width * 1e6:.0f} μs")
    print(f"Time constant: {params['tau'] * 1e6:.0f} μs")
    print(f"Pulse width / τ ratio: {pulse_width / params['tau']:.2f}")

    if pulse_width > 3 * params["tau"]:
        print("Pulse is much longer than τ - output will nearly reach input level")
    elif pulse_width > params["tau"]:
        print("Pulse is longer than τ - partial charging/discharging")
    else:
        print("Pulse is shorter than τ - significant filtering effect")

    return plt.gcf()


def main():
    """Run all theoretical analyses."""
    print("RC Filter Theoretical Analysis")
    print("=" * 40)
    print("This example shows RC filter behavior using theoretical calculations.")
    print("No SPICE simulation required!\n")

    # Step response analysis
    plot_step_response()
    plt.show()

    # Frequency response analysis
    plot_frequency_response()
    plt.show()

    # Pulse response analysis
    analyze_pulse_response()
    plt.show()

    print("\nAnalysis completed!")
    print("\nKey RC Filter Principles:")
    print("1. Time constant τ = RC determines charging/discharging speed")
    print("2. Cutoff frequency fc = 1/(2πRC) defines -3dB point")
    print("3. Step response reaches 63.2% of final value at t = τ")
    print("4. Frequency response rolls off at -20dB/decade above fc")
    print("5. Phase shifts from 0° to -90° with -45° at fc")


if __name__ == "__main__":
    main()
