from qiskit import QuantumCircuit

class CircuitLayout:
    def __init__(
            self,
            number_of_bits: int,
            number_of_bits_to_measure: int,
            initial_states = None,
    ):
        """
        Create basic quantum circuit with defined number of qubits.

        Args:
            number_of_bits: Integer of the number of qubits of the system.
            number_of_bits_to_measure: Integer of the number of qubits to measure at the end of the system,
                which creates classical bits to store the quantum data after it is projected.
            initial_states: Optional dictionary of the form {qubit, '[x, y]'}, where we can define the initial
                state of a qubit as x|0>+y|1>.
        
        Note that Qiskit assumes qubit 0 as the least sig bit and the qubit n-1 as the most.
        Therefore, choosing number_of_bits=4 and number_of_bits_to_measure=2, it measures q2 and q3, not q0 and q1.
        """
        if number_of_bits_to_measure > number_of_bits:
            raise ValueError("Number of bits to measure can't be bigger than the total number of bits")
        
        self.qc = QuantumCircuit(number_of_bits, number_of_bits_to_measure)  # instead of integers, it can also take QuantumRegister and ClassicalRegister objects

        if initial_states:
            for qubit, state in initial_states.items():
                self.qc.initialize(list(state), int(qubit))  # initialize the qubits we want in a given state

    def add_not_gate(
            self,
            locations: list,
    ):
        """
        Add X Gate (Pauli Matrix), quivalent to the classical NOT gate.

        Args:
            locations: List of the qubits to be affected.
        """
        self.qc.x(locations)
    
    def add_cnot_gate(
            self,
            location: int,
            controller_qubit: int,
            second_controller_qubit = None,
    ):
        """
        Add Controlled-NOT Gate, quivalent to the classical XOR gate.

        Args:
            location: Integer with the qubit to be affected.
            controller_qubit: Integer with the controller qubit (only if it's =1 will this gate act).
            second_controller_qubit: Optional integer with a second controller qubit, making an AND with the first one.
        """
        if type(second_controller_qubit) is int:
            self.qc.ccx(controller_qubit, second_controller_qubit, location)  # also called a "Toffoli" gate
        else:
            self.qc.cx(controller_qubit, location)
    
    def add_hadamard_gate(
            self,
            locations: list,
    ):
        """
        Add Hadamard Gate, which introduces superposition.

        Args:
            locations: List of the qubits to be affected.

        Note that it does NOT create entanglement. To those objects we call e-bits.
        """
        self.qc.h(locations)