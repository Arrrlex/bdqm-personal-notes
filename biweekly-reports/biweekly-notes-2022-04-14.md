# Biweekly Update

## Tasks Completed

- I investigated reproducing the relevant results in the GMP paper, but realized
  this requires the use of larger datasets than I currently have available
- I further improved and documented the project code \[1\]. It should now be possible
  for any grad students to use our codebase on any dataset and with any
  computational backend (e.g. a PACE cluster, a local computer with/without
  GPU, etc.)

## Tasks Planned

- [ ] (Carried over) Run some experiments comparing different samplers and different
  pruners
- [ ] Try to run the hyperparameter tuning pipeline on a larger dataset, for
  example progressively larger samples from the 200K OC20 dataset.

## Literature Review

For my literature review, I read the "paper" \[2\].

### Skimming Questions

#### Summarize the overall goal of the work.

The paper introduces graphs and Machine Learning over graph-structured data,
gives some examples of graph-structured data in the wild, and explains the
basics of how neural networks can operate on graphs.

#### What figure is most interesting or relevant? What is the main thing you learned from it?

As a Distill publication, this paper is chock-full of fascinating and
well-designed visualizations. For me the most interesting figure was in the
section "Passing messages between parts of the graph". This interactive
diagram illustrates a simple case of how a graph neural network layer uses the
connectivity between nodes: first it gets a list of all the neighbors of a
particular node, then it aggregates the previous layer's embeddings, then it
applies some learned transformation (e.g. an affine transformation).

This is important because the connectivity between nodes is what makes Graph
Neural Networks unique, and this is a clear illustration of one mechanism for
exploiting that graph structure.

### Reading Questions

#### What is the strongest point of the paper?

Almost all interactive diagrams feature 2 representations of the same
structure side-by-side, and the user can interact with one side and see the
corresponding change on the other side. This allows several concepts to be
very intuitively understood, such as adjacency matrix and tensor representations
of graphs.


#### What is the weakest point of the paper?

The authors have clearly tried to come up with a uniform "visual language" for
diagrammatically representing transformations on graphs (mostly in the section
"Graph Neural Networks"). However, this visual language is not well explained
and is difficult to understand. For example, the figure "Schematic of a Graph
Nets architecture leveraging global representations" is complicated and not
straightforward to interpret, but is not fully explained in the text (instead
the visual language is assumed to be sufficient).

#### How does the paper relate to your research project?

My research group is focusing on tuning hyperparameters for Neural Network
Potential models of atomic simulations. The inputs to these neural networks
can be understood as graphs whose nodes are atoms and whose edges are distances
or bonds. Indeed, the best-performing ML models for the OC20 dataset are
graph neural networks \[3\]. Thus, it's useful to understand how they work to
fruitfully compare them with our approach.

## References

\[1\]: [bdqm-hyperparam-tuning](https://github.com/Arrrlex/bdqm-hyperparam-tuning/tree/ed94ed8f6dd2aaa0eb9cbbf218af4c07a9e0941c)
\[2\]: B Sanchez-Lengenling, E Reif, A Pierce, A B Wiltschko. A Gentle Introduction to Graph Neural Networks. In: Distill. Published Sept 2. 2021.
\[3\]: [OC20 Leaderboard](https://opencatalystproject.org/leaderboard.html)