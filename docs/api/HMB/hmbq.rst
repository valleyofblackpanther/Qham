create_heisenberg_circuit function
==================================

.. function:: create_heisenberg_circuit(N, trotter_steps=1)

   Generates a quantum circuit that simulates the Heisenberg model. The simulation uses the Trotter-Suzuki decomposition to approximate the time evolution of the system under the Heisenberg Hamiltonian with periodic boundary conditions.

   :param N: The number of qubits representing spins in the chain.
   :type N: int
   :param trotter_steps: The number of Trotter steps to use in the decomposition, which determines the approximation accuracy.
   :type trotter_steps: int, optional
   :returns: A Qiskit QuantumCircuit object that represents the simulation circuit.
   :rtype: QuantumCircuit

   The function creates a QuantumCircuit object and applies a series of RXX, RYY, and RZZ gates to simulate the interactions between adjacent spins in a 1D Heisenberg chain. The periodic boundary conditions are implemented by connecting the last qubit with the first one.

Example Usage
-------------

The following example demonstrates how to create a Heisenberg model circuit for a chain of 4 qubits with a single Trotter step:

.. code-block:: python

   from qiskit import Aer, transpile

   # Create a quantum circuit for the Heisenberg model with 4 qubits and 1 Trotter step
   N = 4
   trotter_steps = 1
   qc = create_heisenberg_circuit(N, trotter_steps)
   
   # Transpile the circuit for a simulator backend
   simulator = Aer.get_backend('aer_simulator')
   transpiled_circuit = transpile(qc, simulator)
   
   # Print the transpiled circuit
   print(transpiled_circuit)