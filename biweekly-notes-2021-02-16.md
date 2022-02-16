# Biweekly Update

## Tasks Completed

As part of the Hyperparameter Optimization project group, in the last 2 weeks I:
 
- Set up PACE and learned how to submit jobs
- Successfully trained an AMPTorch model using the PACE ICE cluster on a GPU
  - I wrote up detailed instructions for doing this on a shared Google Doc, including troubleshooting tips
- Did deeper research into hyperparameter optimization libraries (in particular optuna)
  - The previous semester's cohort used Facebook's Ax, but in our shared notes I outlined why we might use Optuna instead
- Made a list of hyperparameters to optimize
- Converted the training data from `.traj` format to `.lmdb` format (see [this script]))
- Did an initial literature search for papers related to hyperparameter optimization

## Tasks Planned

For the next 2 weeks, I will:

- Train an AMPTorch model using the correct data for this project, instead of the (small) water dataset
- Run a simple hyperparameter optimization job 
- Dockerize the hyperparameter optimization job, in order to share the code with people with better GPUs 
- Parallelize the hyperparameter optimization job, to enable a larger search space

## Contribution Description

Figuring out how to run AMPTorch on a GPU on the PACE ICE cluster is an important step in enabling us to run GPU-accelerated hyperparameter optimization jobs, since this is the only GPU available to all of us in the group. Carefully documenting my steps in getting it to work will be instrumental in getting the other members of the group up to speed rapidly.

The rest of the work I did was mostly researching libraries and techniques we can use. Having a better understanding of how hyperparameter optimization works and what tools are available will help us to make informed implementation decisions, potentially saving us from going down the wrong path (e.g. using a library with poor parallelization support, requiring us to run all training runs in serial, significantly slowing down our iteration time).

## Literature Review

For my literature review, I read the paper \[2\].

### Skimming Questions

#### Summarize the overall goal of the work.

Finding the optimal values for so-called "hyper-parameters" of a ML model cannot be done using the same optimization techniques as are used to optimize the parameters of the model itself, because of the graph structure of the hyper-parameters: some hyper-parameters only make sense if other hyper-parameters have been set to particular values. This paper introduces 2 new methods for hyperparameter optimization, and demonstrates that they can both outperform random search in the same amount of time.

#### What figure is most interesting or relevant? What is the main thing you learned from it?

Figure 4 is the most interesting. It shows that both hyper-parameter optimization methods outperform human hyper-parameter tuning over a reasonable number of trials.

### Reading Questions

#### What is the strongest point of the paper?

The results are all very strong: the algorithms given outperform both random search and manual search. The paper comes with a reference implementation of the algorithms, mentioned almost as an afterthought, which is still widely used 11 years later.

#### What is the weakest point of the paper?

Though the algorithms as stated are sequential (i.e. serial), it's noted briefly that the algorithms are run asynchronously, and that this impacts the per-trial efficiency of the optimization. Though understandable that the researchers had limited time and compute resources, it's disappointing that the per-trial performance is not as good as it could have been given the algorithms and setup in the paper.

#### How does the paper relate to your research project?

Since we are performing a hyperparameter optimization for AMPTorch, it's highly relevant to look at the paper introducing both two of the most widely-used hyperparameter optimization algorithms, and one of the most robust and widely-used Python software packages (hyperopt).

Looking at the results of the paper, and the description of the two algorithms, helps me to understand which algorithms are likely to perform better on our particular domain. In particular, I will focus my initial efforts on using the Tree Parzen Estimator.

## References

\[1\]: [https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/main/hpopt/create_lmdb.py](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/main/hpopt/create_lmdb.py)

\[2\]: James Bergstra and Yoshua Bengio. Algorithms for Hyper-Parameter Optimization. In NIPS, 2011, pp. 2546-2554.
