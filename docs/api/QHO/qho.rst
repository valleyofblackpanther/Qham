QuantumHarmonicOscillator class
===============================

.. class:: QuantumHarmonicOscillator(n, omega)

   Represents a quantum harmonic oscillator, which is a fundamental model for quantum systems with quadratic potential energy.

   :param n: The number of quantum states to consider in the model.
   :type n: int
   :param omega: The angular frequency of the oscillator.
   :type omega: float

   .. attribute:: n

      The number of quantum states included in the model.

   .. attribute:: omega

      The angular frequency of the harmonic oscillator.

   .. attribute:: hamiltonian

      The Hamiltonian matrix representing the quantum harmonic oscillator.


   .. method:: create_annihilation_operator()

      Generates the annihilation operator matrix, which is a lower-triangular matrix whose entries are related to the square root of the quantum number of each state.

      :returns: The annihilation operator matrix for `n` quantum states.
      :rtype: torch.Tensor


   .. method:: create_hamiltonian()

      Constructs the Hamiltonian matrix for the quantum harmonic oscillator using the annihilation and creation (adjoint of annihilation) operators.

      :returns: The Hamiltonian matrix for the oscillator.
      :rtype: torch.Tensor


   .. method:: find_eigenstates()

      Diagonalizes the Hamiltonian matrix to find the eigenvalues and eigenvectors, which correspond to the energy levels and quantum states of the oscillator.

      :returns: A tuple containing an array of eigenvalues and a matrix of eigenvectors.
      :rtype: (torch.Tensor, torch.Tensor)


   .. method:: print_eigenvalues()

      Prints the eigenvalues of the Hamiltonian, which represent the energy levels of the quantum harmonic oscillator.

Example Usage
-------------

The following example demonstrates how to instantiate the ``QuantumHarmonicOscillator`` class and print out the energy levels of the oscillator:

.. code-block:: python

   # Initialize the quantum harmonic oscillator with 10 states and an angular frequency of 1.0
   qho = QuantumHarmonicOscillator(n=10, omega=1.0)

   # Print the energy levels of the oscillator
   qho.print_eigenvalues()

This will display the energy levels of a quantum harmonic oscillator with 10 quantum states and an angular frequency of 1.0.