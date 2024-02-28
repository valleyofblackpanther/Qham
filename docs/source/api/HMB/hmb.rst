HeisenbergModel class
=====================

.. class:: HeisenbergModel(N, J)

   A class that simulates the 1D Heisenberg model, a fundamental model in quantum mechanics for understanding magnetic properties in materials.

   :param N: The number of spins in the 1D Heisenberg chain.
   :type N: int
   :param J: The exchange interaction strength between neighboring spins.
   :type J: float

   .. attribute:: N

      The number of spins in the Heisenberg chain.

   .. attribute:: J

      The coupling constant representing the strength of the exchange interaction.

   .. attribute:: Sx

      The Pauli X matrix used to represent spin interactions along the x-axis.

   .. attribute:: Sy

      The Pauli Y matrix used to represent spin interactions along the y-axis.

   .. attribute:: Sz

      The Pauli Z matrix used to represent spin interactions along the z-axis.

   .. attribute:: I

      The identity matrix representing no spin interaction.


   .. method:: build_hamiltonian()

      Constructs the Hamiltonian matrix for the Heisenberg model using the tensor product of Pauli matrices to represent spin interactions.

      :returns: The Hamiltonian matrix of the system.
      :rtype: torch.Tensor


   .. method:: solve_eigenvalues()

      Diagonalizes the Hamiltonian matrix to find the eigenvalues and eigenvectors, which represent the energy levels and the corresponding quantum states of the system.

      :returns: A tuple containing an array of eigenvalues and a matrix of eigenvectors.
      :rtype: (torch.Tensor, torch.Tensor)


   .. method:: plot_energy_levels(eigenvalues)

      Generates a plot of the energy levels of the Heisenberg model.

      :param eigenvalues: The array of energy levels obtained from diagonalizing the Hamiltonian.
      :type eigenvalues: torch.Tensor

Example Usage
-------------

To instantiate the ``HeisenbergModel``, calculate the energy levels, and plot them, you can use the following code:

.. code-block:: python

   model = HeisenbergModel(N=4, J=1)
   eigenvalues, eigenvectors = model.solve_eigenvalues()
   model.plot_energy_levels(eigenvalues)

The output will be a matplotlib plot displaying the energy levels of a 1D Heisenberg chain with 4 spins and an exchange interaction strength of 1.