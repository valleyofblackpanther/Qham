import torch
import matplotlib.pyplot as plt

class HeisenbergModel:
    """
    A class to simulate the 1D Heisenberg model, which is a quantum spin chain model used to understand magnetism.

    Attributes:
        N (int): The number of spins in the chain.
        J (float): The exchange interaction strength between adjacent spins.
        Sx (torch.Tensor): The Pauli X matrix for spin interactions.
        Sy (torch.Tensor): The Pauli Y matrix for spin interactions.
        Sz (torch.Tensor): The Pauli Z matrix for spin interactions.
        I (torch.Tensor): The identity matrix representing no spin interaction.
        H (torch.Tensor): The Hamiltonian matrix of the system.
    """    
    def __init__(self, N, J):
        """
        Initializes the HeisenbergModel with a given number of spins and interaction strength.

        Args:
            N (int): The number of spins in the chain.
            J (float): The exchange interaction strength between adjacent spins.
        """        
        self.N = N
        self.J = J
        self.Sx = torch.tensor([[0, 1], [1, 0]], dtype=torch.complex64)
        self.Sy = torch.tensor([[0, -1j], [1j, 0]], dtype=torch.complex64)
        self.Sz = torch.tensor([[1, 0], [0, -1]], dtype=torch.complex64)
        self.I = torch.eye(2, dtype=torch.complex64)
        self.H = self.build_hamiltonian()

    def build_hamiltonian(self):
        """
        Constructs the Hamiltonian matrix for the Heisenberg model using the tensor product of Pauli matrices.

        Returns:
            torch.Tensor: The Hamiltonian matrix as a PyTorch tensor.
        """        
        H = torch.zeros((2**self.N, 2**self.N), dtype=torch.complex64)
        for i in range(self.N):
            next_i = (i + 1) % self.N
            for op1, op2 in [(self.Sx, self.Sx), (self.Sy, self.Sy), (self.Sz, self.Sz)]:
                term = torch.eye(1, dtype=torch.complex64)
                for j in range(self.N):
                    if j == i:
                        term = torch.kron(term, op1)
                    elif j == next_i:
                        term = torch.kron(term, op2)
                    else:
                        term = torch.kron(term, self.I)
                H -= self.J * term
        return H

    def solve_eigenvalues(self):
        """
        Diagonalizes the Hamiltonian to find the eigenvalues and eigenvectors.

        Returns:
            tuple: A tuple containing a tensor of eigenvalues and a tensor of eigenvectors.
        """        
        eigenvalues, eigenvectors = torch.linalg.eigh(self.H)
        return eigenvalues, eigenvectors

    def plot_energy_levels(self, eigenvalues):
        """
        Plots the energy levels of the Heisenberg model as a scatter plot.

        Args:
            eigenvalues (torch.Tensor): A tensor containing the energy levels to plot.
        """        
        plt.figure(figsize=(10, 6))
        plt.plot(eigenvalues.numpy(), 'o')
        plt.title('Energy levels of the 1D Heisenberg model')
        plt.xlabel('State index')
        plt.ylabel('Energy')
        plt.grid(True)
        plt.show()

# # Example usage
# if __name__ == "__main__":
#     model = HeisenbergModel(N=4, J=1)
#     eigenvalues, eigenvectors = model.solve_eigenvalues()
#     model.plot_energy_levels(eigenvalues)