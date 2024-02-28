import numpy as np
from qiskit.circuit import QuantumCircuit, Parameter

class SquareLatticeMatrix:
    """
    Represents a square lattice using a matrix to define adjacency relationships between sites.

    The adjacency matrix is a binary matrix where each element (i, j) indicates whether
    sites i and j are neighbors (1 if they are neighbors, 0 otherwise).

    Attributes:
        rows (int): Number of rows in the lattice.
        cols (int): Number of columns in the lattice.
        adjacency_matrix (np.ndarray): Matrix representing adjacency between sites.
    """    

    def __init__(self, rows, cols):
        """
        Initializes the square lattice with the given number of rows and columns.

        Args:
            rows (int): The number of rows in the lattice.
            cols (int): The number of columns in the lattice.
        """        
        self.rows = rows
        self.cols = cols
        self.adjacency_matrix = self._create_adjacency_matrix()

    def _create_adjacency_matrix(self):
        """
        Generates the adjacency matrix for the lattice.

        Returns:
            np.ndarray: A binary matrix indicating adjacent sites.
        """        
        size = self.rows * self.cols
        adjacency_matrix = np.zeros((size, size), dtype=int)
        for row in range(self.rows):
            for col in range(self.cols):
                index = row * self.cols + col
                if row > 0:
                    adjacency_matrix[index, ((row - 1) * self.cols) + col] = 1
                if row < self.rows - 1:
                    adjacency_matrix[index, ((row + 1) * self.cols) + col] = 1
                if col > 0:
                    adjacency_matrix[index, (row * self.cols) + (col - 1)] = 1
                if col < self.cols - 1:
                    adjacency_matrix[index, (row * self.cols) + (col + 1)] = 1
        return adjacency_matrix

    def are_neighbors(self, site1, site2):
        """
        Determines if two sites are neighbors based on the adjacency matrix.

        Args:
            site1 (int): The index of the first site.
            site2 (int): The index of the second site.

        Returns:
            bool: True if the sites are neighbors, False otherwise.
        """        
        return self.adjacency_matrix[site1, site2] == 1

def create_heisenberg_square_lattice_matrix_circuit(lattice_matrix, t):
    """
    Creates a quantum circuit for the Heisenberg model on a square lattice.

    Args:
        lattice_matrix (SquareLatticeMatrix): The lattice matrix defining adjacency.
        t (Parameter): A Qiskit Parameter object representing time evolution.

    Returns:
        QuantumCircuit: The quantum circuit modeling the Heisenberg interactions.
    """    
    N = lattice_matrix.rows * lattice_matrix.cols
    qc = QuantumCircuit(N)
    # Iterate over all pairs of sites and apply interaction gates if they are neighbors    
    for i in range(N):
        for j in range(i + 1, N):
            if lattice_matrix.are_neighbors(i, j):
                qc.rxx(2 * t, i, j)
                qc.ryy(2 * t, i, j)
                qc.rzz(2 * t, i, j)
    return qc

# Example usage
# lattice_matrix = SquareLatticeMatrix(rows=2, cols=2)
# t = Parameter('t')
# qc = create_heisenberg_square_lattice_matrix_circuit(lattice_matrix, t)
# print(qc)