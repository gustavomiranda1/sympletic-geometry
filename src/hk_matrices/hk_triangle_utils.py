"""
Module for visualizing triangle transformations using h_k matrices.
Each k value (2, 4, 5, 9) has its own set of matrices: h_k, h_k inverse, t, and t inverse.
"""
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
import os
from src.utils.shared_utils import plot_all_combinations

# Define the vertices of the initial triangle (in columns)
vertices = np.array([[-1, 2, -1],  # x coordinates
                    [-1, -1, 2]])  # y coordinates

# Define t matrix and its inverse
t = np.array([[1, 1], [0, 1]])
t_inverse = np.linalg.inv(t)

# Define h_k matrices for different k values
k_values = [2, 4, 5, 9]  # The k values we want to use

def create_matrix_maps():
    """Create matrix maps for each k value.
    
    Returns:
        dict: A dictionary mapping k values to their corresponding matrix maps.
        Each matrix map contains:
        - 'T': t matrix
        - 'I': t inverse
        - 'H': h_k matrix
        - 'K': h_k inverse
    """
    matrix_maps = {}
    for k in k_values:
        # Create h_k matrix and its inverse
        h_k = np.array([[1, 0], [k, 1]])
        h_k_inverse = np.linalg.inv(h_k)
        
        # Create matrix map for this k value
        matrix_maps[k] = {
            'T': t, 'I': t_inverse,  # t and t inverse
            'H': h_k, 'K': h_k_inverse  # h_k and h_k inverse
        }
    return matrix_maps

def plot_triangles(triangles, title, color, original=True, step=None, matrix_map=None, output_folder="Spanning_hk"):
    """Plot triangles efficiently using PolyCollection.
    
    Args:
        triangles: List of triangle vertices
        title: Plot title
        color: Color for the triangles
        original: Whether to plot the original triangle
        step: Current step number
        matrix_map: Dictionary mapping labels to matrices
        output_folder: Folder to save the plot
    """
    os.makedirs(output_folder, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the original triangle
    if original:
        ax.fill(vertices[0], vertices[1], color='gray', alpha=0.5, label='Original')

    # Convert column-based coordinates to list of triangles for PolyCollection
    triangle_list = [np.column_stack((triangle[0], triangle[1])) for triangle in triangles]
    poly = PolyCollection(triangle_list, facecolors=color, alpha=0.6, edgecolors='black', linewidths=0.3)
    ax.add_collection(poly)

    # Set plot properties
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(title)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid()

    # Save the plot
    filename = os.path.join(output_folder, f"Step_{step}.png" if step is not None else "output.png")
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close(fig)

def run_hk_visualization(max_step=9, colors=None):
    """Run the h_k matrices visualization task for each k value.
    
    Args:
        max_step: Maximum number of transformation steps
        colors: Dictionary mapping k values to colors. If None, uses default colors.
    """
    if colors is None:
        colors = {
            2: 'blue',
            4: 'green',
            5: 'red',
            9: 'purple'
        }
    
    matrix_maps = create_matrix_maps()
    
    for k in k_values:
        print(f"\nProcessing k = {k}")
        labels = 'THIK'  # T, H_k, I (t inverse), K (h_k inverse)
        plot_all_combinations(
            max_step=max_step,
            labels=labels,
            vertices=vertices,
            matrix_map=matrix_maps[k],
            color=colors[k],
            output_folder=f"Spanning_h{k}",
            title_prefix=f"(h_{k} matrices)"
        )

def unpack_sequence(sequence_str, matrix_map):
    """Convert a string of matrix labels into a list of matrices."""
    try:
        return [matrix_map[char] for char in sequence_str]
    except KeyError:
        valid_labels = ', '.join(sorted(matrix_map.keys()))
        print(f"Invalid sequence. Use only: {valid_labels}")
        return None

def apply_sequence(matrices, points):
    """Apply a sequence of matrices to points (column-based coordinates)."""
    for matrix in matrices:
        points = np.dot(matrix, points)  # Matrix multiplication with column-based coordinates
    return points

def generate_combinations(n, labels):
    """Generate all combinations of labels of length n."""
    return [''.join(comb) for comb in product(labels, repeat=n)]

def apply_sequence_with_cache(sequence, points, matrix_map, cache):
    """Apply a sequence of matrices with caching."""
    sequence_key = tuple(sequence)
    
    if sequence_key in cache:
        return cache[sequence_key]
    
    result = points
    for label in sequence:
        result = np.dot(matrix_map[label], result)
    
    cache[sequence_key] = result
    return result

def generate_steps(max_step, labels, vertices, matrix_map, cache):
    """Generate transformations for all steps."""
    all_steps = []
    current_step_triangles = [vertices]
    
    for step in range(1, max_step + 1):
        print(f"Step {step}")
        
        step_labels = generate_combinations(step, labels)
        new_triangles = [
            apply_sequence_with_cache(list(comb), vertices, matrix_map, cache)
            for comb in step_labels
        ]
        
        current_step_triangles.extend(new_triangles)
        all_steps.append((step, new_triangles, step_labels))
    
    return all_steps

def plot_all_combinations(max_step, labels, vertices, matrix_map, color='blue', output_folder="Spanning_hk", title_prefix=""):
    """Plot all possible combinations of transformations up to max_step."""
    cache = {}
    all_steps = generate_steps(max_step, labels, vertices, matrix_map, cache)
    
    # List to store accumulated triangles
    cumulative_triangles = []
    
    # Plot each step
    for step, step_triangles, step_labels in all_steps:
        cumulative_triangles.extend(step_triangles)
        title = f"Step {step}: Accumulated Transformations {title_prefix}"
        plot_triangles(
            cumulative_triangles, 
            title, 
            color, 
            original=True, 
            step=step,
            matrix_map=matrix_map,
            output_folder=output_folder
        )
        print(f"Completed step {step} with {len(step_triangles)} new triangles")

# Remove the old run_hk_visualization function at the end 