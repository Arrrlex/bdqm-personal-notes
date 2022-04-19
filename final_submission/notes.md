# Files Attached

You will find the following files attached:

- `config.py`, which contains the results of the AmpOpt hyperparameter search. This can be plugged directly into AMPTorch to train a model.
- `report.md`, detailing our strategy and reasoning, and containing useful links

# Contribution Description

I designed and wrote all the code for AmpOpt, a package for running hyperparameter tuning jobs in parallel.

I tested AmpOpt on PACE ICE as well as my personal computer.

Using AmpOpt, I:

- generated data
- trained models and evaluated them against validation datasets
- Orchestrated PACE jobs for MySQL and hyperparameter tuning
- Generated reports

I also did ad-hoc data analysis to understand why different datasets were giving us radically different results.

# Self Assessment

## Things I did well

I think the code package I delivered is well-structured and solves a real problem faced by researchers developing models using AmpTorch.

I feel that AmpOpt provides a vastly easier way to run parallel hyperparameter tuning jobs for AMPTorch than any alternative.

AmpOpt is many times faster than any alternatives thus far developed.

I also wrote extensive documentation and I'm optimistic about people using it.

## Things I could improve

1. I could have insisted more on getting feedback early, from both my teammates and the Medford Group grad students for the AmpOpt codebase.
1. I could have written unit tests, which would have helped me catch many refactoring bugs significantly earlier
1. I could have spent less time "bikeshedding" the design of AmpOpt and more time focused on running experiments
1. I was not very happy with the collaboration in our team. I felt like for parts of the semester I was working alone, and to the end I was the only person contributing to the AmpOpt code base. I could have raised my concerns about this setup earlier, in order to either get contributions or feedback (either about the code, my approach or my collaboration style).
1. Finally, I often changed my mind about priorities during the semester (as can be seen from my biweekly reports), and I think I could have benefitted from better focus and setting myself clearer goals.
