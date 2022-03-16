## What I've Done
1. I read through the lectures on the [BDQM Github Repo](https://github.com/medford-group/bdqm-vip/tree/master/lectures), including running the code
2. I trained an AMPTorch model on the Hyperparameter Optimization project dataset with sample hyperparameters (see Appendix 1). Though this model probably isn't particularly performant, and I still don't fully understand all the parameters, it's useful to verify that I can run AMPTorch locally on my computer. Note: I had to change the Python version specified in the env.yaml file in the amptorch repo to 3.7. 
3. I read through [1], focusing on understanding the mathematics of Gaussian Multipole featurization. 
4. I performed an initial round of research for hyperparameter tuning libraries in Python, which aren't tied to a specific ML framework. My search turned up 3 libraries, all popular (as measured by Github stars):
	1. optuna
	2. ray.tune
	3. hyperopt

## Plans for Next 2 Weeks
Firstly, I would like to better structure my research and my thoughts. Concretely:
1. I will sign up for Mendeley (or resurrect my Zotero account) and keep track of relevant papers there (with Bibtex references)
2. I will create 2 private repos: one (shared with Ryan Chou and Tyler Yoshihara) for code, one for personal notes.

There are 3 main avenues I'd like to pursue in the next 2 weeks:
1. Getting a better grasp of the theory. Concrete steps: deep diving the lectures and the Gaussian Multipoles paper [1], playing around with the maths on paper. Objective: I understand the role of every parameter and configuration in AMPTorch.
2. Understanding last semester's progress. Concrete steps: reading, running and understanding the code from the previous semester's cohort. Objective: I can describe the approach taken by the previous semester, I understand their performance uplift compared to a reasonable baseline, and I have a concrete plan for improving on it.
3. Getting started with hyperparameter optimisation for AMPTorch using a library. Concrete steps: running a (small) hyperparameter optimisation for an AMPTorch model locally on my computer. If possible: running an optimisation on a (possibly GPU-based) cloud platform. Reading some review papers on hyperparameter optimisation. Objectives: I have a working proof-of-concept for hyperparameter optimisation; I understand the state-of-the-art.

## Reflections

As can be seen, my progress so far is not huge, but I think it was necessary to first get a lay of the land.

I've also (for personal reasons) not been able to devote as much time as I'd have liked to the VIP. Going forward I will have much more time, and I expect to make faster progress.

## Paper Review

I here review [1]. 
### Skimming Questions
1. **Summarize the overall goal of the work.** The work introduces a new method "Gaussian Multipoles" of featurizing molecular systems as a preprocessing step for using neural networks to compute simulations. Unlike previous featurising schemes, this scheme produces the same number of dimensions for all input systems. The scheme, paired with a neural network, is trained on two standard datasets and compares favourably in performance and efficiency to previous ML schemes.
2. **What figure is most relevant or important? What is the main thing you learned from it?** Figure 1 is the most relevant, since it gives a schematic overview of the novel featurization scheme. This figure shows me that each atom in a system is translated into a separate feature vector (all of which are presumably then concatenated for the final feature vector), and that the resulting features are invariant under rotation of the system.
### Reading Questions
1. **What is the strongest point of the paper?** The direct comparison with other featurization schemes shows that GMP is clearly preferable, both conceptually (since it enables a Single Neural Network architecture) and technically (better score and lower training time with comparable number of features per atom) 
2. **What is the weakest point of the paper?** The comparison with DimeNet++ does not scale up to the full size of the best-performing DimeNet architecture, so it's hard to know what to attribute the difference in performance to. Figure 5 is somewhat confusing, since a) seems to be about comparing with DimeNet++, whereas b) has no comparison.
3. **How does the paper relate to your research project?** The first step of the machine learning pipeline is the Gaussian Multipole featurization. Fully understanding the mechanics of GMP will help me to set reasonable ranges on hyperparameters and understand the hyperparameter space better (perhaps informing priors for any Bayesian hyperparameter searches).


## References

[1] Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. [http://arxiv.org/abs/2102.02390](http://arxiv.org/abs/2102.02390)

## Appendix 1: Model Training Code

To be run from the root of the bdqm-vip repo.

```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import torch
from ase import Atoms
import ase.io
from ase.calculators.emt import EMT
from ase.build import molecule

from amptorch.ase_utils import AMPtorch
from amptorch.trainer import AtomsTrainer

from pathlib import Path


bdqm_path = Path(".")
amptorch_path = Path("../amptorch")

train_data = ase.io.read(bdqm_path / "data/amptorch_data/oc20_3k_train.traj")

elements = list(set(atom.symbol for atom in train_data))

def get_path_to_gaussian(element):
    gaussians_path = amptorch_path / "examples/GMP/valence_gaussians"
    return next(p for p in gaussians_path.iterdir() if p.name.startswith(element + "_"))


atom_gaussians = {element: get_path_to_gaussian(element) for element in elements}


sigmas = [0.2, 0.69, 1.1, 1.66, 2.66]

MCSHs = {
    "MCSHs": {
        "0": {"groups": [1], "sigmas": sigmas},
        "1": {"groups": [1], "sigmas": sigmas},
        "2": {"groups": [1, 2], "sigmas": sigmas},
    },
    "atom_gaussians": atom_gaussians,
    "cutoff": 8,
}

config = {
    "model": {
        "name":"singlenn",
        "get_forces": True,
        "num_layers": 3,
        "num_nodes": 10,
        "batchnorm": True,
    },
    "optim": {
        "force_coefficient": 0.01,
        "lr": 1e-3,
        "batch_size": 16,
        "epochs": 10,
        "loss": "mse",
        "metric": "mae",
    },
    "dataset": {
        "raw_data": str(bdqm_path / "data/amptorch_data/oc20_3k_train.traj"),
        "fp_scheme": "gmp",
        "fp_params": MCSHs,
        "elements": elements,
        "save_fps": True,
        "scaling": {"type": "normalize", "range": (0, 1)},
        "val_split": 0.1,
    },
    "cmd": {
        "debug": False,
        "run_dir": "./",
        "seed": 1,
        "identifier": "test",
        "verbose": True,
        # Weights and Biases used for logging - an account(free) is required
        "logger": False,
    },
}

torch.set_num_threads(1)
trainer = AtomsTrainer(config)
trainer.train()
```
