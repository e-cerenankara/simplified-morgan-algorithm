def morgan(file):
    # Read MOL file lines
    with open(file) as f:
        lines = f.readlines()

    # This implementation supports only V2000 MOL format
    if "V2000" not in lines[3]:
        raise ValueError("Only V2000 MOL files are supported.")

    # Parse atom and bond counts
    values = lines[3].split()
    n_atoms = int(values[0])
    n_bonds = int(values[1])

    # Read atom symbols
    atom_symbol = []
    index = 4
    for _ in range(n_atoms):
        parts = lines[index].split()
        atom_symbol.append(parts[3])
        index += 1

    # Initialize degree, neighbor list, and bond order matrix
    degree = [0] * n_atoms
    a_neighbours = [[] for _ in range(n_atoms)]
    bond = [[0] * n_atoms for _ in range(n_atoms)]

    # Read bond information and build connectivity
    for b_index in range(n_bonds):
        items = lines[index + b_index].split()
        atom1 = int(items[0]) - 1
        atom2 = int(items[1]) - 1
        b_order = int(items[2])

        degree[atom1] += 1
        degree[atom2] += 1
        a_neighbours[atom1].append(atom2)
        a_neighbours[atom2].append(atom1)
        bond[atom1][atom2] = b_order
        bond[atom2][atom1] = b_order

    # Initial Morgan labels start with atom degrees
    labels = degree[:]
    prev_count = len(set(labels))
    final_label = labels[:]
    total_label = prev_count

    # Iterative Morgan label refinement
    while True:
        new_label = []
        for i in range(n_atoms):
            total = 0
            for neighbour in a_neighbours[i]:
                total += labels[neighbour]
            new_label.append(total)

        count = len(set(new_label))

        # Keep the labeling with the maximum number of unique values
        if count > total_label:
            total_label = count
            final_label = new_label[:]

        # Stop when the number of unique labels no longer changes
        if count == prev_count:
            break

        labels = new_label[:]
        prev_count = count

    # Select atom with highest label as canonical start
    highest = max(final_label)
    f_atom = final_label.index(highest)

    canonical = {f_atom: 1}
    next_num = 2
    left = [f_atom]

    # Canonical atom numbering
    while left:
        c_atom = left.pop(0)

        # Unvisited neighbors
        temp = [n for n in a_neighbours[c_atom] if n not in canonical]

        # Sort by Morgan label, then bond order
        temp.sort(
            key=lambda x: (final_label[x], bond[c_atom][x]),
            reverse=True
        )

        for atom in temp:
            canonical[atom] = next_num
            next_num += 1
            left.append(atom)

    return final_label, canonical
