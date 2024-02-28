import numpy as np
from qiskit.circuit import QuantumCircuit, Parameter

class SquareLattice:
    """
    Represents a square lattice in two dimensions and provides functionality to generate an adjacency list for the lattice.

    Attributes:
        rows (int): The number of rows in the lattice.
        cols (int): The number of columns in the lattice.
        adjacency_list (dict): A dictionary where each key is a site index, and the value is a list of neighboring site indices.
    """    
    def __init__(self, rows, cols):
        """
        Initializes the SquareLattice with the specified number of rows and columns.

        Args:
            rows (int): The number of rows in the lattice.
            cols (int): The number of columns in the lattice.
        """
        self.rows = rows
        self.cols = cols
        self.adjacency_list = self._create_adjacency_list()

    def _create_adjacency_list(self):
        """
        Private method to create an adjacency list for the lattice based on its size.

        Returns:
            dict: The adjacency list represented as a dictionary.
        """        
        adjacency_list = {}
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = []
                if row > 0:
                    neighbors.append(((row - 1) * self.cols) + col)  # Up
                if row < self.rows - 1:
                    neighbors.append(((row + 1) * self.cols) + col)  # Down
                if col > 0:
                    neighbors.append((row * self.cols) + (col - 1))  # Left
                if col < self.cols - 1:
                    neighbors.append((row * self.cols) + (col + 1))  # Right
                adjacency_list[row * self.cols + col] = neighbors
        return adjacency_list

    def get_neighbors(self, site):
        """
        Retrieves the neighboring site indices for a given site.

        Args:
            site (int): The index of the site whose neighbors are to be found.

        Returns:
            list: A list of neighboring site indices.
        """        
        return self.adjacency_list[site]

def create_heisenberg_lattice_circuit(lattice, t):
    """
    Constructs a quantum circuit representing the Heisenberg model on a square lattice.

    Args:
        lattice (SquareLattice): The square lattice for which to construct the circuit.
        t (Parameter): A Qiskit Parameter representing the time evolution parameter for the Heisenberg model.

    Returns:
        QuantumCircuit: The constructed quantum circuit with Heisenberg interactions between neighbors.
    """    
    N = lattice.rows * lattice.cols
    qc = QuantumCircuit(N)
    # Apply the Heisenberg interaction using the adjacency list    
    for site, neighbors in lattice.adjacency_list.items():
        for neighbor in neighbors:
            qc.rxx(2 * t, site, neighbor)
            qc.ryy(2 * t, site, neighbor)
            qc.rzz(2 * t, site, neighbor)
    return qc

# Example usage
# lattice = SquareLattice(rows=2, cols=2)
# t = Parameter('t')
# qc = create_heisenberg_lattice_circuit(lattice, t)
# print(qc)