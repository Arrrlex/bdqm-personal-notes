# Fingerprinting

Our task is to create a ML model to perform well at the energy calculation portion of the "S2EF" (Structure to Energy and Forces) task in the Open Catalyst Project OC20 dataset \[1\].

The inputs of this dataset consist of a list of atoms, a list of atom bonds between pairs of atoms, and information about the catalyst. For our ML models, we disregard all information except the atoms positions and which elements they are. This is enough information to predict the energy.

The difficulty is that this is a list of variable length. Naively, we would need a different neural network for each number of atoms. That's going to be extremely inefficient for learning, and won't generalize in case our dataset is missing lists of a certain length. Instead, let's find a way to train a single model which works for any number of atoms.

No matter how we arrange our learning and prediction scheme, we'll want to satisfy certain properties:
- Order invariance: if we change the order in which we present the atoms, the result doesn't change
- Translational invariance: if we shift the whole system by a constant, the result doesn't change
- Rotational invariance: if we rotate the whole system, the result doesn't change

The first trick we apply is to train a model which predicts per-atom energy, which we then sum to get the total energy. This has a number of benefits:
- It's theoretically sound (apparently)
- Since we're doing something to each atom, then summing them (a commutative operation), this gives us order invariance (provided that whatever we're doing to each atom is also order-invariant)
- Summation is differentiable, so we'll be able to apply backpropogation

Let's fix an atom that we're focusing on. For practical reasons, let's apply a cutoff function to discard any atoms which aren't within a neighborhood of our chosen atom (say $r$). We're still left with a variable-length list of atoms.

What we want is a _fingerprinting scheme_, i.e. a function from this variable-length list of atoms to a fixed-length vector, which we can then feed into a neural network. Our fingerprinting scheme should satisfy these properties as above:
- Order invariance
- Translational invariance
- Rotational invariance

In addition, to be successful as an input to the neural network, the fingerprint should be more-or-less unique.

## Probes

Our approach uses _probes_. Probes are functions that tell us about the neighborhood of a particular point. We'll be looking at 2 types of probes: radial probes and angular probes. Radial probes tell us how far away other atoms are. Angular probes tell us which directions other atoms are in.

Each probe is constructed by taking some function and placing a copy of it over each atom within the cutoff, then adding all the values up.

The Gaussian radial probe is constructed from Gaussians. It takes a parameter $\sigma$, the "radius" of the Gaussian. If we have several probes each with different value for $\sigma$, we can build up a picture of how far away nearby atoms are.

The MCSH angular probe is constructed from Maxwell-Cartesian spherical harmonic functions. For a given "order" $n$, there are $n!$ spherical harmonic functions of that order. These functions all "point" in different directions. If we have a probe for every function up to order $n$, we can build up a picture of which directions nearby atoms are in.

We pointwise multiply each radial probe $G_\sigma$ with each angular probe $S_{abc}$ to get $\mathrm{probe}_{\sigma, abc}$.

## GMP and Electron Density

The simplest thing to do with these probe functions is to evaluate them all at the location of our atom, then we get a feature vector that we can feed to the neural network. The problem is that this feature vector doesn't know anything about the element of the atom!

We could try to solve this problem by just adding an extra feature (or features) encoding the atom's element, but that doesn't work, because the whole calculation ought to be different for different elements. Thus in practice a _High-Dimensional Neural Network Architecture_ is used, which is just fancy talk for saying there's a separate neural network with separate parameters for each element.

We can do better! If we can use just a single neural network, the learning will be more efficient, and the whole model will be much smaller. We can do that by using electron densities.

Electron density refers to the probability density function for electrons, i.e. for a particular location, what's the probability (density) that an electron will be here? It's theoretically sound to replace element information with electron density information.

We can approximate electron density by fitting a sum-of-Gaussians model for each element. The Medford group has already done this.

If we then put this electron density sum-of-Gaussian over each atom in the neighborhood and add them all up, we get the electron density for the whole neighborhood $\hat{\rho}$. Now, to compute our features, instead of evaluating our probe at the atom's location, we can take the inner product of the probe and the electron density function:

$$
\mu_{\sigma, abc} = \left\langle \mathrm{probe}_{\sigma, abc}, \hat{\rho} \right\rangle
$$

Taking the inner product of two 3D functions is a volume integral, but luckily the fine folks at the Medford group have solved it analytically.

## Rotational Invariance

Oh no, we forgot about rotational invariance! Since our angular probes $\mu$ have direction, if we rotate the system we'll end up hitting different angular probes so the final result will change.

Fear not however! The MCSH functions are divided up into _groups_, which are closed under rotation. Thus, for each group $p_1, p_2, \ldots, p_n$ in group $P$, we replace the features $\mu_{\sigma, p_1}, \ldots, \mu_{\sigma, p_n}$ with their _norm_:

$$
\Phi_{\sigma, P} = \sqrt{\sum_{i=1}^n \mu_{\sigma, p_i}}
$$

The features $\Phi$ are the final features for the GMP fingerprinting scheme.

## GMP Parameters

There are 3 decisions to take when taking GMP fingerprints:

1. Which sigmas should I use for the radial probes?
2. How many sigmas should I use?
3. What's the max order I should use for the angular probes?
4. What cutoff should I apply?

For 1, in the original paper the sigmas were chosen manually. It might be nice to consider choosing the sigmas using hyperparameter tuning.

For 2 and 3, increasing the number will increase the number of features, improving the model's accuracy but increasing its size.

For 4, increasing the number will improve the feature quality but will also increase feature computation time.

## References

\[1\]: C Lawrence Zitnick et al. An Introduction to Electrocatalyst Design using Machine Learning for Renewable Energy Storage. [https://arxiv.org/abs/2010.09435](https://arxiv.org/abs/2010.09435)

\[2\]: Jörg Behler. Constructing high-dimensional neural network potentials: A tutorial review. In: International Annal of Quantum Chemistry, Vol 115, Issue 16, pp. 1032-1050.

\[3\]: Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. [http://arxiv.org/abs/2102.02390](http://arxiv.org/abs/2102.02390)