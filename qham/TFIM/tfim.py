import torch
import matplotlib.pyplot as plt

class TFIMSimulation:
    
    """Simulate the Transverse Field Ising Model (TFIM) on a square lattice.

    Attributes:
        size (int): The width and height of the square lattice.
        beta (float): The inverse temperature parameter for the simulation.
        h (float): The transverse field strength applied to the system.
        steps (int): The number of Monte Carlo steps to perform in the simulation.
        lattice (torch.Tensor): The lattice representing the spins, initialized randomly.

    """

    def __init__(self, size=10, beta=0.4, h=0.05, steps=100):
        """Initialize the simulation with the given parameters.

        Args:
            size (int): The lattice size. Defaults to 10.
            beta (float): The inverse temperature parameter. Defaults to 0.4.
            h (float): The transverse field strength. Defaults to 0.05.
            steps (int): The number of simulation steps. Defaults to 100.
        """        
        self.size = size
        self.beta = beta
        self.h = h
        self.steps = steps
        self.lattice = self.initialize_lattice()

    def initialize_lattice(self):
        """Initialize the lattice to a random state with spins up or down."""        
        return torch.randint(2, (self.size, self.size), dtype=torch.float32) * 2 - 1

    def tfim_step(self):
        """Perform a single Monte Carlo step of the TFIM simulation."""        
        for _ in range(self.lattice.numel()):
            i, j = torch.randint(0, self.lattice.shape[0], (1,)).item(), torch.randint(0, self.lattice.shape[1], (1,)).item()
            S = self.lattice[i, j]
            neighbors = self.lattice[(i+1)%self.lattice.shape[0], j] + \
                        self.lattice[i, (j+1)%self.lattice.shape[1]] + \
                        self.lattice[(i-1)%self.lattice.shape[0], j] + \
                        self.lattice[i, (j-1)%self.lattice.shape[1]]
            deltaE = 2 * S * neighbors
            if deltaE < 0 or torch.rand(1).item() < torch.exp(-self.beta * deltaE):
                self.lattice[i, j] *= -1
            if torch.rand(1).item() < self.h:
                self.lattice[i, j] *= -1

    def run_simulation(self):
        """Run the simulation for the specified number of steps."""        
        for _ in range(self.steps):
            self.tfim_step()

    def plot_lattice(self):
        """Plot the current state of the lattice."""        
        plt.figure(figsize=(5, 5))
        plt.imshow(self.lattice.numpy(), cmap='coolwarm')
        plt.colorbar(label='Spin')
        plt.title('TFIM Lattice Configuration')
        plt.show()

# Example usage
# if __name__ == "__main__":
#     sim = TFIMSimulation(size=10, beta=0.4, h=0.05, steps=100)
#     sim.run_simulation()
#     sim.plot_lattice()