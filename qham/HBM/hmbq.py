from qiskit.circuit import QuantumCircuit, Parameter

def create_heisenberg_circuit(N, trotter_steps=1):
    """
    Create a quantum circuit simulating the Heisenberg model with optional periodic boundary conditions.

    This function constructs a quantum circuit based on the Heisenberg model using the Trotter-Suzuki decomposition. 
    The Heisenberg model is a fundamental model in quantum mechanics that describes how quantum spins interact with each other.

    Parameters:
    N (int): Number of qubits representing spins in the chain.
    trotter_steps (int): Number of Trotter steps to use for time evolution approximation. Defaults to 1.
    
    Returns:
    QuantumCircuit: The quantum circuit representing the Heisenberg interaction between spins.

    The constructed circuit will include RXX, RYY, and RZZ gates between adjacent qubits to simulate the Heisenberg interaction. 
    If periodic boundary conditions are required, additional gates are added between the first and last qubits to simulate a closed chain.
    """
    # Initialize the quantum circuit for N qubits    
    qc = QuantumCircuit(N)
    # Define the time evolution parameter 't'
    t = Parameter('t')  
    
    # Apply the Heisenberg interaction using Trotter-Suzuki decomposition/Loop over the specified number of Trotter steps
    for _ in range(trotter_steps):
        for i in range(N - 1):
            qc.rxx(2 * t, i, i + 1)
            qc.ryy(2 * t, i, i + 1)
            qc.rzz(2 * t, i, i + 1)
        # Apply periodic boundary conditions to connect the last and first qubits
        qc.rxx(2 * t, N - 1, 0)
        qc.ryy(2 * t, N - 1, 0)
        qc.rzz(2 * t, N - 1, 0)
    # Return the constructed circuit    
    return qc

# Example usage
# N = 4
# trotter_steps = 1
# qc = create_heisenberg_circuit(N, trotter_steps)
# print(qc)