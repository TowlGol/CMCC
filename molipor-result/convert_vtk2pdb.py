from Input_methond import read_positions_and_atom_names_from_file
import numpy as np

def read_vtk_points(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.startswith("POINTS"):
            start_idx = i + 1
            break
    if start_idx is None:
        raise ValueError("No POINTS section found in VTK file.")

    points = []
    for line in lines[start_idx:]:
        if line.strip() == '' or not any(c.isdigit() for c in line):
            break
        try:
            coords = list(map(float, line.strip().split()))
            for i in range(0, len(coords), 3):
                points.append(coords[i:i+3])
        except:
            return np.array(points)
    return np.array(points)

def compute_max_non_colliding_radii(points, positions, vdw_radii):
    max_radii = []
    for pt in points:
        dists = np.linalg.norm(positions - pt, axis=1) - vdw_radii
        dists = dists[dists > 0]  
        if len(dists) == 0:
            max_radii.append(0.0)
        else:
            max_radii.append(np.min(dists))
    return np.array(max_radii)

def write_spheres_to_pdb(points, radii, output_filename):
    with open(output_filename, 'w') as f:
        for i, (pt, r) in enumerate(zip(points, radii)):
            f.write("HETATM{:5d}  VSP VOR A{:4d}    {:8.3f}{:8.3f}{:8.3f}  1.00{:6.2f}           V\n".format(
                i + 1, i + 1, pt[0], pt[1], pt[2], r
            ))

        f.write("END\n")

# Usage
name = "F2"
vtk_file = "C:/Users/pc/Desktop/Molipor/"+name+"/Voronoi_interior.vtk"
Path = "G:/Doc/datasets/dataset-2/"
filename = name+".pdb"

positions, atom_names, atom_masses, atom_vdw = read_positions_and_atom_names_from_file(str(Path) + str(filename))

points = read_vtk_points(vtk_file)

max_radii = compute_max_non_colliding_radii(points, positions, atom_vdw)

# output PDB
write_spheres_to_pdb(points, max_radii, name+"_voronoi_spheres.pdb")
