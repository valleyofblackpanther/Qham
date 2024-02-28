from qiskit import QuantumCircuit

def create_tfim_circuit(n_qubits, theta_z, theta_x, periodic_boundary=False):
    """
    Create a quantum circuit representing the Transverse Field Ising Model (TFIM).

    Args:
        n_qubits (int): Number of qubits (spins) in the chain.
        theta_z (float): Parameter for ZZ interaction strength.
        theta_x (float): Parameter for transverse field strength.
        periodic_boundary (bool): If True, applies periodic boundary conditions.

    Returns:
        QuantumCircuit: The constructed quantum circuit representing the TFIM.
    """
    qc = QuantumCircuit(n_qubits)
    
    # Add ZZ interactions
    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)
        qc.rz(theta_z, i + 1)
        qc.cx(i, i + 1)
    
    # Apply periodic boundary conditions if specified
    if periodic_boundary and n_qubits > 2:
        qc.cx(n_qubits - 1, 0)
        qc.rz(theta_z, 0)
        qc.cx(n_qubits - 1, 0)
    
    # Add transverse field interactions
    for i in range(n_qubits):
        qc.rx(theta_x, i)
    
    return qc

# Enhanced usage example with periodic boundary conditions
# n_qubits = 4
# theta_z = 1.0
# theta_x = 1.5
# qc = create_tfim_circuit(n_qubits, theta_z, theta_x, periodic_boundary=True)
# print(qc)