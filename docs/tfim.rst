TFIMSimulation class
====================

.. class:: TFIMSimulation(size=10, beta=0.4, h=0.05, steps=100)

   A class to simulate the Transverse Field Ising Model (TFIM) on a two-dimensional lattice. The TFIM is a model of magnetism in statistical mechanics.

   :param size: The width and height of the square lattice. Defaults to 10.
   :type size: int, optional
   :param beta: The inverse temperature parameter for the simulation. Defaults to 0.4.
   :type beta: float, optional
   :param h: The transverse field strength applied to the system. Defaults to 0.05.
   :type h: float, optional
   :param steps: The number of Monte Carlo steps to perform in the simulation. Defaults to 100.
   :type steps: int, optional

   .. attribute:: size

      The size of the lattice (size x size).

   .. attribute:: beta

      The inverse temperature parameter for the simulation.

   .. attribute:: h

      The transverse field strength.

   .. attribute:: steps

      The number of simulation steps to run.

   .. attribute:: lattice

      The lattice representing the spins, initialized randomly.


   .. method:: initialize_lattice()

      Initializes the lattice to a random state where each spin is either up or down with equal probability.

      :returns: A square lattice of spins.
      :rtype: torch.Tensor


   .. method:: tfim_step()

      Performs a single Monte Carlo step in the TFIM simulation, potentially flipping each spin based on the Metropolis-Hastings algorithm.


   .. method:: run_simulation()

      Runs the TFIM simulation for the number of steps specified in the constructor.


   .. method:: plot_lattice()

      Plots the current state of the lattice using matplotlib, showing the spins as a heatmap.

Example Usage
-------------

The following example sets up a TFIM simulation with a lattice of size 10x10, runs it for 100 steps, and then plots the final configuration of spins:

.. code-block:: python

   # Initialize the TFIM simulation
   sim = TFIMSimulation(size=10, beta=0.4, h=0.05, steps=100)

   # Run the simulation
   sim.run_simulation()

   # Plot the final lattice configuration
   sim.plot_lattice()

This will produce a plot showing the spin configuration of the lattice after running the specified number of Monte Carlo steps.