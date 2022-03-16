# Background

The world needs more efficient chemical reactions. This will allow us to:

- Make hydrogen fuel cells cheaper, more efficient and using more abundant materials, improving energy storage vital to the renewable energy revolution
- Make ammonia using less energy (currently the Haber-Bosch process for making ammonia for fertilizer accounts for 1% of global $CO_2$ emissions)
- Lots more stuff

In order to improve chemical reactions, we should find better catalysts. The efficiency of a chemical reaction is affected significantly and predictably by the adsorption energy of the reactants being adsorbed into the surface of the catalyst material.

We can calculate the adsorption energy by calculating the energy of various structures.

Quantum Theory (in particular Schrödinger's Equation) tells us that we can compute the total energy of a system if we know the atomic positions, the nuclear charges, and the total charge. \[2\] However, it is generally considered impossible to calculate this analytically for more than 5 atoms.

Thus, we use approximations. One popular approximation is Density Functional Theory (DFT). This is a family of methods which take as input the electron density (i.e. the probability density function for electrons in space) and outputs the total energy of the system \[3\]. In the 1960s Hohenberg and Kohn proved that the total electronic energy is a function of the electron density, and later Kohn and Sham provided a practical method for approximating it.

DFT is used widely today, however it is computationally expensive and scales with $O(n^3)$ in the number of atoms \[1\]. Thus we search for cheaper ways to approximate the total electronic energy of a system.

An additional wrinkle is that, when inputting the atomic structure for DFT calculations, we only know the approximate locations of the atoms, since in practice they will move to find the location of minimum energy. This is known as the "relaxed energy", and the new structure the "relaxation". To find the relaxation, we must iteratively calculate the density functional for a configuration (in particular we calculate the atomic forces), and then calculate a new configuration minimizing the functional, repeating until convergence.

In order to accelerate ML research on approximating DFT calculations, the Open Catalyst Project created the OC230 dataset of 3 million structures, and the full relaxation trajectories, energies and forces.

For our purposes, we focus on the "S2EF" (Structure to Energy and Forces) task, in particular calculating the energy. We do not tackle the harder relaxation problem for now.

## References

\[1\]: C Lawrence Zitnick et al. An Introduction to Electrocatalyst Design using Machine Learning for Renewable Energy Storage. In ArXiv.

\[2\]: Jörg Behler. Constructing high-dimensional neural network potentials: A tutorial review. In: International Annal of Quantum Chemistry, Vol 115, Issue 16, pp. 1032-1050.

\[3\]: Kyle A. Baseden and Jesse W. Tye. Introduction to Density Functional Theory: Calculations by Hand on the Helium Atom. In: Journal of Chemical Education 2014 91 (12), 2116-2123