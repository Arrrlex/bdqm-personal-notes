# Biweekly Update

## Tasks Completed

As part of the Hyperparameter Optimization project group, in the last 4 weeks I:

- Ran parallel hyperparameter optimization using Optuna. This required:
    - Setting up MySQL on PACE ICE
    - Implementing the code for running jobs using the shared MySQL DB
    - Creating scripts for starting the MySQL PACE job automatically, and running multiple PACE hyperparameter jobs simultaneously
    - Documenting all of this in the README for the project \[1\].
- Increased the number and range of hyperparameters to search over
- Fix the LMDB creation script to enable use of `torch.DoubleTensor` rather than `torch.FloatTensor` \[2\]
- Began to generate plots automatically, in order to create a report \[3\]
-

Also, as a group we created our midterm presentation.

## Tasks Planned

## Contribution Description

## Literature Review

### Skimming Questions

#### Summarize the overall goal of the work.

#### What figure is most interesting or relevant? What is the main thing you learned from it?

### Reading Questions

#### What is the strongest point of the paper?

#### What is the weakest point of the paper?

#### How does the paper relate to your research project?

## References

\[1\]: [bdqm-hyperparam-tuning README.md](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/README.md)

\[2\]: [bdqm-hyperparam-tuning create_lmdb.py](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/hpopt/create_lmdb.py#L126)

\[3\]: [bdqm-hyperparam-tuning hp_study.py](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/hpopt/hp_study.py#L43-L48)