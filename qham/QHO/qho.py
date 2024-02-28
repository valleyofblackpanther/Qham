import torch

class QuantumHarmonicOscillator:
    """
    A class representing the quantum harmonic oscillator, a fundamental model in quantum mechanics.

    Attributes:
        n (int): The number of quantum states to consider in the oscillator model.
        omega (float): The angular frequency of the oscillator.
        hamiltonian (torch.Tensor): The Hamiltonian matrix of the oscillator.
    """

    def __init__(self, n, omega):
        """
        Initializes the QuantumHarmonicOscillator with the given number of states and frequency.

        Args:
            n (int): The number of quantum states for the oscillator.
            omega (float): The angular frequency of the oscillator.
        """
        self.n = n
        self.omega = omega
        self.hamiltonian = self.create_hamiltonian()

    def create_annihilation_operator(self):
        """
        Creates the annihilation operator matrix for n quantum states, which is a lower-triangular matrix.

        Returns:
            torch.Tensor: The annihilation operator represented as a PyTorch tensor.
        """
        indices = torch.arange(1, self.n)
        values = torch.sqrt(indices)
        return torch.diag(values, 1)

    def create_hamiltonian(self):
        """
        Constructs the Hamiltonian matrix for the quantum harmonic oscillator using the annihilation and creation operators.

        Returns:
            torch.Tensor: The Hamiltonian matrix as a PyTorch tensor.
        """
        a = self.create_annihilation_operator()
        a_dagger = a.T
        H = self.omega * (a_dagger @ a + 0.5 * torch.eye(self.n))
        return H

    def find_eigenstates(self):
        """
        Diagonalizes the Hamiltonian matrix to find its eigenvalues and eigenvectors, representing the energy levels and state vectors of the oscillator.

        Returns:
            tuple: A tuple containing a tensor of eigenvalues and a matrix of eigenvectors.
        """
        eigenvalues, eigenvectors = torch.linalg.eigh(self.hamiltonian)
        return eigenvalues, eigenvectors

    def print_eigenvalues(self):
        """
        Prints the calculated eigenvalues (energy levels) of the quantum harmonic oscillator.
        """        
        eigenvalues, _ = self.find_eigenstates()
        print("Eigenvalues (Energy Levels):", eigenvalues)

# Example usage
# if __name__ == "__main__":
#     qho = QuantumHarmonicOscillator(n=10, omega=1.0)
#     qho.print_eigenvalues()