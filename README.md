
# A simplified Morgan Algorithm designed for V2000 MOL files

This repository contains **a Python implementation** of the MOrgan Algorithm for canonical atom labeling of molecular graphs. The implementation has minimal design **without external dependencies**.


The Morgan algorithm assigns iterative labels to atoms based on their local connectivity until label convergence is achieved. The final labels are then used to determine a canonical atom ordering.

This implementation follows these main steps:
1. Initialization of atom labels using atomic degree
2. Iterative refinement of labels based on neighboring atoms
3. Detection of convergence based on label uniqueness
4. Canonical atom numbering using final labels and bond priorities

At each iteration, a new label is assigned to each atom by summing the labels of its neighboring atoms. The algorithm continues iterating until label convergence is reached. Convergence is defined as the point at which the number of unique labels remains unchanged between consecutive iterations.
This stopping criterion ensures that further iterations do not introduce additional structural discrimination. After convergence, the atom with the highest final Morgan label is selected as the canonical starting atom.

When assigning canonical numbers to neighboring atoms, ordering is determined using a scheme:
- Neighboring atoms with higher final Morgan labels are prioritized.
- If two neighboring atoms have identical Morgan labels, bond order is used as a secondary sorting criterion with higher bond orders taking precedence.

__References__
Morgan, H. L. The Generation of a Unique Machine Description for
Chemical Structures - A Technique Developed at Chemical Abstracts
Service. J. Chem. Doc. 1965, 5, 107–112.
