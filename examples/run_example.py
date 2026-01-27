import sys
import os

# Allow importing from the repository root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from morgan_algorithm import morgan

labels, canonical = morgan("../ethanol.mol")

print(" ")
print("Molecule File: ethanol.mol")
print("-" * 60)
print("Atom Index - Morgan Label - Canonical Index")
print("-" * 60)

for i, value in enumerate(labels):
    print(" " * 3, i + 1, " " * 12, value, " " * 12, canonical[i])

print("-" * 60)
print("Final List:", labels)
