import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

class HubbardModel:
    """
    A class representing the Hubbard model, a fundamental model in condensed matter physics that describes interacting particles on a lattice.

    Attributes:
        num_sites (int): The number of lattice sites in the model.
        t (float): The hopping parameter representing the probability amplitude for a particle to move to an adjacent site.
        U (float): The on-site interaction energy representing the energy penalty for double occupancy.
        H (numpy.ndarray): The Hamiltonian matrix of the system.
    """    

    def __init__(self, num_sites, t, U):
        """
        Initializes the HubbardModel with the given number of sites, hopping parameter, and on-site interaction energy.

        Args:
            num_sites (int): The number of lattice sites.
            t (float): The hopping parameter for the model.
            U (float): The on-site interaction energy.
        """        
        self.num_sites = num_sites
        self.t = t
        self.U = U
        self.H = self.create_hamiltonian()
    
    def create_hamiltonian(self):
        """
        Constructs the Hamiltonian matrix for the Hubbard model.

        Returns:
            numpy.ndarray: The Hamiltonian matrix representing the Hubbard model.
        """        
        dim = 4**self.num_sites   # Dimension of the Hilbert space
        H = np.zeros((dim, dim))  # Initialize Hamiltonian matrix
        
        # Convert basis index to occupation numbers        
        def idx_to_occ(idx):
            return tuple((idx >> bit) & 1 for bit in reversed(range(self.num_sites * 2)))
        
        # Convert occupation numbers to basis index        
        def occ_to_idx(occ):
            idx = 0
            for n in occ:
                idx = (idx << 1) | n
            return idx
        
        # Construct the kinetic (hopping) term        
        for i in range(self.num_sites - 1):
            for idx in range(dim):
                occ = idx_to_occ(idx)
                for spin in [0, 1]:  # 0 for up, 1 for down
                    if occ[2*i+spin] > occ[2*(i+1)+spin]:
                        new_occ = list(occ)
                        new_occ[2*i+spin], new_occ[2*(i+1)+spin] = new_occ[2*(i+1)+spin], new_occ[2*i+spin]
                        new_idx = occ_to_idx(new_occ)
                        H[idx, new_idx] -= self.t
                        H[new_idx, idx] -= self.t

        # Construct the interaction term        
        for idx in range(dim):
            occ = idx_to_occ(idx)
            for i in range(self.num_sites):
                H[idx, idx] += self.U * occ[2*i] * occ[2*i+1]
        
        return H
    
    def diagonalize(self):
        """
        Diagonalizes the Hamiltonian to find the energy levels of the system.

        Returns:
            tuple: A tuple containing an array of energy levels and a matrix of eigenvectors.
        """        
        return eigh(self.H)
    
    def plot_energy_levels(self, energies):
        """
        Plots the energy levels of the Hubbard model.

        Args:
            energies (numpy.ndarray): An array containing the energy levels to be plotted.
        """        
        plt.figure(figsize=(8, 6))
        for i, energy in enumerate(energies):
            plt.hlines(energy, 0, 1, colors='blue', linestyles='solid')
        plt.xlabel('System')
        plt.ylabel('Energy')
        plt.title('Energy Levels of the Hubbard Model')
        plt.xticks([])
        plt.show()

# # Usage example
# model = HubbardModel(num_sites=2, t=1.0, U=2.0)
# energies, _ = model.diagonalize()
# model.plot_energy_levels(energies)