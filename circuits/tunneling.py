import argparse
import numpy as np

from typing import Dict

from circuits.circuit_layout import CircuitLayout
from circuits.run_circuit import simulate

def tunneling_circuit(
        velocity: float,
        api_key: str,
        barrier_strength: float = 1.0,
        used_backend: str = 'aer_simulator',
        shots: int = 100
    ) -> Dict[str, int]:
    """
    Generates a circuit for a 1D particle through a barrier.
    
    Args:
        velocity: Float of the particle's velocity, where velocity=1 is the maximum.
        api_key: User's API Key from their IBM account.
        barrier_strength: Float representing barrier thickness/strength.
        used_backend: String with the backend to be used.
        shots: Number of shots for measurement statistics.

    Returns:
        counts: Dictionary with the number of measurements for each result.
    """
    circuit = CircuitLayout(1, 1)

    # Probability of tunneling decreases exponentially with barrier strength
    angle = velocity**2 * np.exp(-barrier_strength) * (np.pi / 2)
    circuit.qc.u(2*angle, 0, 0, 0)

    circuit.qc.measure_all()

    counts = simulate(circuit, api_key=api_key, used_backend=used_backend, shots=shots)
    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Running quick test for tunneling effect on a quantum computer.')

    parser.add_argument('--api_key', type=str, help='API key for IBM quantum computers.', default=None)
    args = parser.parse_args()

    if args.api_key is None:
        raise ValueError("API key is missing. Login into your IBM Qiskit account if you still don't have one.")
    
    counts = tunneling_circuit(
        velocity=1.0,  # example velocity, for this test's purpose
        api_key=args.api_key,
        barrier_strength=1.0,
        used_backend='aer_simulator',
        shots=100
    )
    print(counts)