SquareLattice class
===================

.. class:: SquareLattice(rows, cols)

   A class representing a square lattice that can be used to simulate quantum systems on a two-dimensional grid.

   :param rows: The number of rows in the lattice.
   :type rows: int
   :param cols: The number of columns in the lattice.
   :type cols: int

   .. attribute:: rows

      The number of rows in the lattice.

   .. attribute:: cols

      The number of columns in the lattice.

   .. attribute:: adjacency_list

      A dictionary representing the adjacency list of the lattice, where each key is a site index and the value is a list of neighboring site indices.

   .. method:: get_neighbors(site)

      Retrieves the neighboring sites for a given site on the lattice.

      :param site: The index of the site for which neighbors are to be found.
      :type site: int
      :returns: A list of indices of neighboring sites.
      :rtype: list[int]


create_heisenberg_lattice_circuit function
==========================================

.. function:: create_heisenberg_lattice_circuit(lattice, t)

   Creates a quantum circuit that simulates the Heisenberg model on a square lattice, using the provided lattice to determine qubit interactions.

   :param lattice: An instance of the SquareLattice class representing the lattice structure.
   :type lattice: SquareLattice
   :param t: A Qiskit Parameter representing the time evolution parameter in the simulation.
   :type t: Parameter
   :returns: A QuantumCircuit object representing the Heisenberg interaction on the lattice.
   :rtype: QuantumCircuit

   This function iterates over each site in the square lattice and applies RXX, RYY, and RZZ gates to simulate the Heisenberg interaction between each site and its neighbors as determined by the adjacency list of the lattice.

Example Usage
-------------

Here is how you can use the ``SquareLattice`` class and the ``create_heisenberg_lattice_circuit`` function to create a circuit:

.. code-block:: python

   from qiskit import Aer, transpile

   # Create a square lattice with 2 rows and 2 columns
   lattice = SquareLattice(rows=2, cols=2)

   # Define the time evolution parameter 't'
   t = Parameter('t')

   # Create the Heisenberg model circuit for the lattice
   qc = create_heisenberg_lattice_circuit(lattice, t)

   # Transpile the circuit for a simulator backend
   simulator = Aer.get_backend('aer_simulator')
   transpiled_circuit = transpile(qc, simulator)

   # Print the transpiled circuit
   print(transpiled_circuit)

The output will be a Qiskit QuantumCircuit that simulates the Heisenberg model on a 2x2 square lattice.