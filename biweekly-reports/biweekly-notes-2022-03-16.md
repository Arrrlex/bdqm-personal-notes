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
- Began to write up systematic notes on the project, beginning with the background. \[3\]

Also, as a group we created our midterm presentation.

## Tasks Planned

- [ ] One of the pieces of feedback we received from our midterm presentation was that we should present our metrics using a standardized unit. In order to do that, I'll need to take a deeper dive into the amptorch code to ensure I understand where to normalize the units.
- [ ] Tyler and I have both done some work on implementing trial pruning (early stopping), but I think it would be useful for us to pool our resources and make sure it's working correctly.
- [ ] I realized that I have never verified I'm able to reproduce the relevant results from the GMP paper \[5\], so I would like to do that as a "sanity check" on our training code
- [ ] I'd like to write up notes on how to use our hyperparameter tuning code, both with and without PACE.
- [ ] Finally, Reading the OC20 overview paper \[6\], I realized that our random train-validate split might make our hyperparameter search prone to overfitting. I'd like to investigate incorporating out-of-domain data to see how the training performs.

## Contribution Description

Now that jobs can run successfully in parallel and (soon) with early stopping, we are able to run far more wide-ranging hyperparameter tuning jobs than before. This should enable us to find better hyperparameter values.

Beginning to work on a report will help us to communicate our results, as well as educate about bayesian hyperparameter optimization in general.

## Literature Review

For my literature review, I read the paper \[6\].

### Skimming Questions

#### Summarize the overall goal of the work.

This work introduces problems relevant to climate change which motivate the search for catalysts, explains the chemistry behind catalysis, introduces simulation for catalyst search, introduces Machine Learning for catalysis simulation, and describes the OC20 dataset produced for this purpose.

#### What figure is most interesting or relevant? What is the main thing you learned from it?

Figure 15, though not hugely interesting, is highly relevant. It demonstrates the relationships between the different tasks in the OC20 dataset and the DFT process. From this diagram it's immediately obvious that IS2RE and IS2RS take the place of larger chunks of work than S2EF, and are hence "harder".

### Reading Questions

#### What is the strongest point of the paper?

This paper does a fantastic job of covering background from multiple disciplines such that, for the non-expert, the material is accessible, yet comprehensive and deep enough to provide an intuitive sense of the difficulty and importance of the material.

In particular, the paper contains:
- Environmental science (explaining the relevance of catalysis to climate change, in particular carbon emission reduction, via technologies such as hydrogen energy storage)
- Chemistry (explaining the role of a catalyst in a reaction, the relevant properties of catalysis, and the role of atomic simulation in determining catalyst suitability)
- Computer Science (Giving a more-or-less mathematically precise description of the tasks in a machine learning context, describing the baseline ML models)

#### What is the weakest point of the paper?

From the paper, it's unclear exactly how the catalyst is included in the dataset's inputs. In section 4.1.2, we read "Along with the atom information described above, additional information is provided for the catalyst." However, in Table 4 all input information is either "per atom" or "per bond", with no field for catalyst information.

#### How does the paper relate to your research project?

The hyperparameter tuning pipeline uses the OC20 dataset to train on, so the description of the dataset itself is valuable for that reason.

In addition, the paper provides a lot of context for doing ML-driven atomic simulations in general.

## References

\[1\]: [bdqm-hyperparam-tuning README.md](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/README.md)

\[2\]: [bdqm-hyperparam-tuning create_lmdb.py](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/hpopt/create_lmdb.py#L126)

\[3\]: [bdqm-hyperparam-tuning hp_study.py](https://github.com/Arrrlex/bdqm-hyperparam-tuning/blob/202df3e7f9dea2ae03c9cd9b2640157c565d6ccb/hpopt/hp_study.py#L43-L48)

\[4\]: [bdqm-personal-notes notes](https://github.com/Arrrlex/bdqm-personal-notes/tree/53b62fa65d3daa804fd7252a6a24383bda2c7ca4/notes)

\[5\]: Lei, X., & Medford, A. J. (2021). A Universal Framework for Featurization of Atomistic Systems. [http://arxiv.org/abs/2102.02390](http://arxiv.org/abs/2102.02390)

\[6\]: C Lawrence Zitnick et al. An Introduction to Electrocatalyst Design using Machine Learning for Renewable Energy Storage. [https://arxiv.org/pdf/2010.09435.pdf](https://arxiv.org/pdf/2010.09435.pdf)