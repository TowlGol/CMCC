import numpy as np
from collections import namedtuple
from tqdm import tqdm  # For progress bar display

# Define atom data structure
Atom = namedtuple('Atom', ['x', 'y', 'z', 'radius'])

def parse_pdb_data(pdb_content):
    """Parse PDB format data"""
    atoms = []
    for line in pdb_content.split('\n'):
        line = line.strip()
        if line.startswith(('HETATM', 'ATOM')):
            try:
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                radius = float(line[60:66].strip())  # Use B-factor directly as radius
                atoms.append(Atom(x, y, z, radius))
            except:
                continue
    return atoms

def calculate_bounding_box(atoms, padding=0.0):
    """Calculate bounding box with optional padding"""
    coords = np.array([(a.x, a.y, a.z) for a in atoms])
    radii = np.array([a.radius for a in atoms])

    min_corner = coords.min(axis=0) - radii.max() - padding
    max_corner = coords.max(axis=0) + radii.max() + padding

    return min_corner, max_corner

def grid_based_volume(atoms, grid_size=0.5, padding=2.0):
    """
    Calculate union volume of multiple spheres using grid subdivision method

    Parameters:
        atoms: List of atoms, each containing (x, y, z, radius)
        grid_size: Grid resolution (cube side length)
        padding: Extra margin for bounding box

    Returns:
        Union volume
    """
    # 1. Compute bounding box
    min_corner, max_corner = calculate_bounding_box(atoms, padding)

    # 2. Create grid
    grid_shape = np.ceil((max_corner - min_corner) / grid_size).astype(int)

    # 3. Compute coordinates of grid centers
    x_coords = np.linspace(min_corner[0] + grid_size / 2,
                           max_corner[0] - grid_size / 2,
                           grid_shape[0])
    y_coords = np.linspace(min_corner[1] + grid_size / 2,
                           max_corner[1] - grid_size / 2,
                           grid_shape[1])
    z_coords = np.linspace(min_corner[2] + grid_size / 2,
                           max_corner[2] - grid_size / 2,
                           grid_shape[2])

    # 4. Mark which grids are inside any sphere
    contained = np.zeros(grid_shape, dtype=bool)

    # Convert to numpy arrays for faster computation
    centers = np.array([(a.x, a.y, a.z) for a in atoms])
    radii = np.array([a.radius for a in atoms])

    # Progress bar display
    pbar = tqdm(total=grid_shape[0], desc="Processing grid slices")

    for i, x in enumerate(x_coords):
        for j, y in enumerate(y_coords):
            # Create grid point coordinates (x, y, z)
            x_coords_mesh, y_coords_mesh, z_coords_mesh = np.meshgrid(x, y, z_coords)
            points = np.vstack([x_coords_mesh.ravel(), y_coords_mesh.ravel(), z_coords_mesh.ravel()]).T

            # Calculate distances from all grid points to all sphere centers
            distances = np.linalg.norm(centers - points[:, np.newaxis, :], axis=2)

            # Check whether each grid point is inside any sphere
            inside = np.any(distances <= radii, axis=1)
            contained[i, j, :] = inside
        pbar.update(1)
    pbar.close()

    # 5. Compute total volume
    grid_volume = grid_size ** 3
    total_volume = np.sum(contained) * grid_volume

    return total_volume

def read_pdb_file(file_path):
    """Read PDB data from file"""
    with open(file_path, 'r') as file:
        pdb_content = file.read()
    return pdb_content

# Example
pdb_file_path = "B13_voronoi_spheres.pdb"
# Read PDB file content
pdb_data = read_pdb_file(pdb_file_path)

# Parse data
atoms = parse_pdb_data(pdb_data)

# Compute union volume
volume = grid_based_volume(atoms, grid_size=0.2)  # Using grid size of 0.2

print(f"Number of atoms: {len(atoms)}")
print(f"Union volume: {volume:.2f} cubic units")
