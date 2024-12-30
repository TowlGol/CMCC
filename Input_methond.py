import numpy as np
import re
# from Extension_Balloon.data import atom_mass, vdw_radii

from data import atom_mass, vdw_radii


def atom_names_to_masses(names):
    """
    根据原子名称获取原子质量。

    :param atom_names: 原子名称列表
    :return: 对应的原子质量数组
    """
    atom_masses = []
    for name in names:
        if name in atom_mass:
            atom_masses.append(atom_mass[name])
        else:
            atom_masses.append(0.0)
    return np.array(atom_masses)


def atom_names_to_vdw(names):
    """
    根据原子名称获取范德华半径。

    :param atom_names: 原子名称列表
    :return: 对应的范德华半径数组
    """
    atom_vdw_radii = []
    for name in names:
        if name in vdw_radii:
            atom_vdw_radii.append(vdw_radii[name])
        else:
            atom_vdw_radii.append(0.0)
    return np.array(atom_vdw_radii)

def read_positions_and_atom_names_from_file(filename):
    """
    根据文件扩展名读取原子位置和名称。

    :param filename: 要读取的文件名
    :return: 原子位置、原子名称、原子质量和范德华半径
    """
    positions = None
    atom_names = None
 
    print("FileName = " + filename)
    if filename.endswith(".pdb"):
        positions, atom_names = read_pdb(filename)
    elif filename.endswith(".mol2"):
        positions, atom_names = read_mol2(filename)
    else:
        positions, atom_names = read_other(filename)

    return positions, atom_names, atom_names_to_masses(atom_names), atom_names_to_vdw(atom_names)


def read_pdb(filename):
    positions = []
    atom_names = []
    with open(filename) as File:
        text = File.read()
        for line in text.splitlines():
            if line.split()[0] == "HETATM" or line.split()[0] == "ATOM":
                temp = np.array(list(map(float, line[30:54].split())))
                positions.append(temp)
                name_and_number = line[12:16].upper()
                name_strip_number = re.match('\s*([A-Z]+)', name_and_number).group(1)
                atom_names.append(name_strip_number)
            elif line.split()[0] == "END":
                break

    return np.array(positions), atom_names


def read_mol2(filename):
    positions = []
    atom_names = []
    with open(filename) as File:
        text = File.read()

        text = text[text.find("@<TRIPOS>ATOM") + 14:]
        text = text[:text.find("@<TRIPOS>")]

        for line in text.splitlines():
            if len(line) > 0:
                positions.append([float(line.split()[2]), float(line.split()[3]), float(line.split()[4])])
                name_and_number = line.split()[1].upper()
                name_strip_number = re.match('([A-Z]+)', name_and_number).group(1)
                atom_names.append(name_strip_number)

    return np.array(positions), atom_names


def read_other(filename):
    try:
        import MDAnalysis
    except:
        print("The other formats are supported by MDAnalysis, which has been not found")
        exit()
    syst = MDAnalysis.Universe(filename)

    # we take only first two inputs (positions and atoms)
    return read_mdanalysis(syst)[:2]


def read_cgbind(cgbind_cage):
    try:
        import cgbind
    except:
        print("Could not load cgbind")
        exit()

    atom_names = [atom.label.upper() for atom in cgbind_cage.atoms]
    positions = cgbind_cage.get_coords()
    return np.array(positions), atom_names, atom_names_to_masses(atom_names), atom_names_to_vdw(atom_names)


def read_mdanalysis(syst):
    try:
        import MDAnalysis
    except:
        print("Could not load MDAnalysis")
        exit()

    atom_names = []
    for name in syst.atoms.names:
        name_strip_number = re.match('([A-Z]+)', name.upper()).group(1)
        atom_names.append(name_strip_number)
    positions = syst.atoms.positions

    return np.array(positions), atom_names, atom_names_to_masses(atom_names), atom_names_to_vdw(atom_names)

def read_positions_and_atom_names_from_array(positions, atom_names):

    just_atom_names = [re.match('([A-Z]+)', name_and_number.upper()).group(1) for name_and_number in atom_names]
    return positions, just_atom_names, atom_names_to_masses(just_atom_names), atom_names_to_vdw(just_atom_names)

