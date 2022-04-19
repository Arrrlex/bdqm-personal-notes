# Hyperparameter Optimization Final Report

Attached to this report is a file, `config.py`, containing the best hyperparameters found by AmpOpt for amptorch.

The code used to find these hyperparameters, as well as to generate all the plots seen in the final presentation, can be found in the notebook \[2\] in the AmpOpt \[1\] repository.

## Strategy

Our strategy was to take advantage of the parallelism afforded us by the PACE
cluster to run larger hyperparameter optimization jobs.

When running jobs with AmpOpt, we used a Bayesian approach, in particular using
the Cma-Es \[3\] sampler and the Hyperband \[4\] trial pruner.

We searched for the following hyperparameters:

- Number of layers of network
- Number of nodes per layer
- Learning rate
- Decay parameter for learning rate

We additionally attempted to search over the rate of dropout, but we found that this resulted in the hyperparameter optimization routine getting stuck in local minima, so we set dropout rate to 0.

On advice from Nicole, we did not attempt using different values for the activation function.

## Reasoning

There were 3 main differences between our approach and the approach of the
previous semester:

1. Use larger datasets
1. Search a wider search space
1. Consider additional hyperparameters

Since our dataset is considerably larger (50,000 vs 3,000), it makes sense that
the best model is a more complex one with more parameters.

The optimal value of `gamma` found was close to 1, suggesting that learning rate
decay had minimal positive effect on the final result.

The learning rate found was fairly close to the learning rate chosen by the
previous semester of `0.001`, though notably our algorithm suggested a
smaller value, which makes sense, again considering the additional complexity
of the model and the additional information in the data.

## References

\[1\]: [AmpOpt](https://github.com/Arrrlex/bdqm-hyperparam-tuning)

\[2\]: [analysis.ipynb](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/84c68addee0e046ad95d2ef45780f9e52369ecf2/notebooks/analysis.ipynb)

\[3\]: N. Hansen, The CMA Evolution Strategy: A Tutorial. arXiv:1604.00772, 2016.

\[4\]: Li et al. Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization.
In: Journal of Machine Learning Research 18 (2018) 1-52
