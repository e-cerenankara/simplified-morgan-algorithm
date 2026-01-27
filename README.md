# Simplified Morgan Algorithm for V2000 MOL Files

This repository contains a Python implementation of the Morgan algorithm for canonical atom labeling of molecular graphs. 
The implementation is designed to be minimal, self-contained, and focused onnthe core algorithmic logic without external dependencies.
---
# Features
- Canonical atom labeling using the Morgan algorithm
- Supports **V2000 MOL file format only**
- Pure Python implementation
- No external libraries required
---
# Algorithm Overview
The Morgan algorithm assigns iterative labels to atoms based on their local connectivity until label convergence is achieved.
The final labels are then used to determine a canonical atom ordering.

This implementation follows these main steps:
1. Initialization of atom labels using atomic degree
2. Iterative refinement of labels based on neighboring atoms
3. Detection of convergence based on label uniqueness
4. Canonical atom numbering using final labels and bond priorities
---
# Iterative Label Refinement and Stopping Criterion

At each iteration, a new label is assigned to each atom by summing the labels of its neighboring atoms.

The algorithm continues iterating until **label convergence** is reached.
Convergence is defined as the point at which the number of unique labels remains unchanged between consecutive iterations.
This stopping criterion ensures that further iterations do not introduce additional structural discrimination.
---
# Canonical Atom Selection

After convergence, the atom with the **highest final Morgan label** is selected as the canonical starting atom.

# Bond Priority and Neighbor Ordering

When assigning canonical numbers to neighboring atoms, ordering is determined using a scheme:

1. **Morgan label priority**  
   Neighboring atoms with higher final Morgan labels are prioritized.

2. **Bond order priority**  
   If two neighboring atoms have identical Morgan labels, bond order is used as a secondary sorting criterion, with higher bond orders taking precedence.
