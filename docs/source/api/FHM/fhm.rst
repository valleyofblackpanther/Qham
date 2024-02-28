HubbardModel class
==================

.. class:: HubbardModel(num_sites, t, U)

   A class that represents the Hubbard model for a system of interacting electrons on a lattice. It is used to study phenomena in condensed matter physics such as high-temperature superconductivity.

   :param num_sites: The number of lattice sites in the model.
   :type num_sites: int
   :param t: The hopping parameter representing the kinetic energy for electrons hopping between sites.
   :type t: float
   :param U: The on-site Coulomb interaction parameter.
   :type U: float


   .. method:: create_hamiltonian()

      Constructs the Hamiltonian matrix for the Hubbard model given the parameters specified during class instantiation.

      :returns: A Hamiltonian matrix of dimensions `(4**num_sites, 4**num_sites)`.
      :rtype: numpy.ndarray


   .. method:: diagonalize()

      Diagonalizes the Hamiltonian matrix to find the energy levels of the system.

      :returns: A tuple containing an array of eigenvalues and a matrix of eigenvectors.
      :rtype: (numpy.ndarray, numpy.ndarray)


   .. method:: plot_energy_levels(energies)

      Plots the energy levels of the Hubbard model as horizontal lines.

      :param energies: The array of energy levels to plot.
      :type energies: numpy.ndarray

Example Usage
-------------

The following example demonstrates how to instantiate the ``HubbardModel`` class, compute the energy levels of the system, and plot them:

.. code-block:: python

   # Instantiate the model with 2 sites, hopping parameter t=1.0, and interaction U=2.0
   model = HubbardModel(num_sites=2, t=1.0, U=2.0)

   # Diagonalize the Hamiltonian to find the energy levels
   energies, _ = model.diagonalize()

   # Plot the energy levels
   model.plot_energy_levels(energies)

This will produce a plot of the energy levels of the Hubbard model for a system with two lattice sites.