from typing import Dict

from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService

def simulate(
        circuit,
        api_key: str,
        used_backend: str = 'aer_simulator',
        shots: int = 100,
    ) -> Dict[str, int]:
    """
    Run a circuit in the given backend and count the results.

    Args:
        circuit: A quantum circuit to be run.
        api_key: User's API Key from their IBM account.
        used_backend: String with the backend to be used. If we want to run on a quantum computer, we just need
            to change this into the appropriate backend, and not a simulation one (default: 'aer_simulator').
        shots: Integer of the number of tests will be done.
    
    Returns:
        counts: Dictionary with the number of measurements for each possible result.
    """
    QiskitRuntimeService.save_account(
        channel='ibm_quantum',
        token=api_key,  # API Key from a person's IBM account
        overwrite=True
    )
    provider = QiskitRuntimeService()

    backend = provider.get_backend(used_backend)
    job = transpile(circuit.qc, backend)

    results = backend.run(job, shots=shots).result()
    counts = results.get_counts()
    return counts