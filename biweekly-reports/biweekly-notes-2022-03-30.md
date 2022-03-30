# Biweekly Update

## Tasks Completed

### Notes

Over the last 2 weeks, I continued to write systematic notes on the project,
focusing on the motivation and mathematical background for the GMP fingerprinting
scheme \[1\]. Primarily I'm doing this for my own understanding, though it should
be helpful to other team members. I'm also hoping that, although we're currently
focused on neural network hyperparameters, this writeup might help us to
understand whether it's worth exploring including any hyperparameters from the
fingerprinting process in the hyperparameter tuning jobs.

### Code

I continued to do major work on the codebase \[2\]. Most prominently, I wrapped
all functionality in a CLI, meaning that the following tasks can all be run
via the same command:

- Generating GMP fingerprints and saving them to LMDB files
- Splitting the data into train and validation sets
- Running a hyperparameter tuning job on a single node
- Starting arbitrarily many PACE jobs and running hyperparameter
  tuning in parallel
- Generating a report from a study of hyperparameters (after running one or
  many hyperparameter tuning jobs)

Putting all of these as sub-commands of the same CLI command aids
discoverability and ease-of-use. In addition, exposing configuration as CLI
arguments makes it very easy to run different experiments, such as:

- What's the practical difference between hyperparameter tuning using random
  sampling vs. various Bayesian sampling algorithms?
- If I activate pruning of trials, how much time do I save?
- What's the practical disadvantages and advantages to increasing the size and
  dimension of the hyperparameter search space?

I'm hoping that having a coherent, easy-to-use CLI will allow us to answer these
questions in a rigorous, reproducible way.

As part of my refactor of the codebase, I improved the documentation, in
particular adding more detail to the setup instructions and example usage.

Since it's strongly discouraged to run computationally intensive code on the
login node of PACE ICE, I added some validation to the CLI to prevent
hyperparameter tuning jobs from running on the login node.

Finally, I fixed the implementation of trial pruning.

### Setup

I helped Tyler and Ryan to set up their environments so they can run
hyperparameter tuning jobs using this library.

This was helpful for many reasons. Firstly, running through the setup process
with both Tyler and Ryan helped me to see several places where the instructions
were unclear or incorrect. Now that these are fixed, the process should be
smoother for grad students hoping to run hyperparameter tuning jobs.

Secondly, now that we are all "onboarded" to the hyperparameter library, we will
be able to run experiments independently and validate one another's results.

### AMPTorch Research

I read through the `amptorch` code enough to convince myself that, after
training and predicting, the units of the Mean Absolute Error of a trained model
really are eV. This means that, when communicating the results of a
hyperparameter tuning job, I can confidently compare it to other trained models.

## Tasks Planned

- [ ] (Carried over) I realized that I have never verified I'm able to reproduce the relevant results from the GMP paper, so I would like to do that as a "sanity check" on our tuning code
- [ ] Run some experiments comparing different samplers and different
  pruners
- [ ] Verify that, given a suitable search space or enough trials,
  we can find the optimal known hyperparameters for the OC20-3K sample
- [ ] Try to run the hyperparameter tuning pipeline on a larger dataset, for
  example progressively larger samples from the 200K OC20 dataset.

## Literature Review

For my literature review, I read the paper \[3\].

### Skimming Questions

#### Summarize the overall goal of the work.

The paper proposes using Tree of Parzen Estimators, a hyperparameter tuning
algorithm, for deep learning workloads. It compares this algorithm to random
search using several benchmark datasets and finds that TPE is faster and gets
overall better results.

#### What figure is most interesting or relevant? What is the main thing you learned from it?

Figure 3 is striking, since it shows how TPE easily outperforms not only random
search (expected) but hand-tuned hyperparameters on the highly non-trivial task
CIFAR-10. Taken together with Figure 2, it paints a compelling picture that
hand-tuning hyperparameters is not only inefficient but not even the way to
get the best results!

### Reading Questions

#### What is the strongest point of the paper?

The main contribution of this paper is demonstrating the efficacy of TPE over
a high-dimensional (238 dimensions) search space. As noted in the paper, this
is an order of magnitude larger than previous literature. Since this search
space is far too large for exhaustive search, the case for automatic tuning
is clear.

#### What is the weakest point of the paper?

The weakest point, and a real missed opportunity, is a lack of meaningful
effort to compare TPE with another hyperparameter tuning algorithm which is
a little smarter than random search. A good example would be the CMA Evolution
Strategy \[4\].

#### How does the paper relate to your research project?

Since the project is tuning hyperparameters for a deep learning model, it's
informative to learn that TPE has been successful in this domain.

## References

\[1\]: [bdqm-personal-notes fingerprinting.md](https://github.com/Arrrlex/bdqm-personal-notes/blob/0bcc40535dcd9277005aded4521531e32374a6ac/notes/fingerprinting.md)

\[2\]: [bdqm-hyperparam-tuning](https://github.com/Arrrlex/bdqm-hyperparam-tuning/tree/9394cf2d309b6142dffd125480167c91a28c7448)

\[3\]: Bergstra, Yamins, Cox. Making a Science of Model Search: Hyperparameter Optimization in Hundreds
of Dimensions for Vision Architectures. [http://proceedings.mlr.press/v28/bergstra13.pdf](http://proceedings.mlr.press/v28/bergstra13.pdf)

\[4\]: Auger, Hansen. A Restart CMA Evolution Strategy with Increasing Population Size. In: Proceedings of the IEEE Congress on Evolutionary Computation, CEC 2005, pp. 1769-1776.