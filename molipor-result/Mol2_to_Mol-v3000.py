def convert_v2000_to_v3000(v2000_filename, v3000_filename):
    # Open the original V2000 file and the target V3000 file
    with open(v2000_filename, 'r') as v2000_file, open(v3000_filename, 'w') as v3000_file:

        # Read the contents of the V2000 file
        lines = v2000_file.readlines()

        # Get the number of atoms and bonds
        n_atoms = int(lines[3].split()[0])  # In the 4th line of the V2000 file, the first number is the atom count
        n_bonds = len(lines) - 5 - n_atoms  # Remaining lines correspond to bonds (excluding atom coordinates)

        # Write the V3000 file header
        v3000_file.write('     RDKit          3D\n\n  0  0  0  0  0  0  0  0  0  0999 V3000\n')
        v3000_file.write(f'M  V30 BEGIN CTAB\nM  V30 COUNTS {n_atoms} {n_bonds} 0 0 0\nM  V30 BEGIN ATOM\n')

        # Write atom information
        atom_lines = lines[4:4 + n_atoms]
        for i, line in enumerate(atom_lines):
            parts = line.split()
            x, y, z = parts[0], parts[1], parts[2]
            element = parts[3]
            v3000_file.write(f'M  V30 {i + 1} {element} {x} {y} {z} 0\n')

        # Write bond information
        v3000_file.write('M  V30 END ATOM\nM  V30 BEGIN BOND\n')
        bond_lines = lines[4 + n_atoms:]
        for i, line in enumerate(bond_lines):
            parts = line.split()
            atom1, atom2 = line[:3], line[3:6]  # This part needs correction (see note below)
            v3000_file.write(f'M  V30 {i + 1} 1 {atom1} {atom2}\n')

        # Write the end markers
        v3000_file.write('M  V30 END BOND\nM  V30 END CTAB\n')

        print(f'File converted successfully to {v3000_filename}')


# Use this script to convert the file
convert_v2000_to_v3000('Molfile.mol', 'W1-pdb.mol')
