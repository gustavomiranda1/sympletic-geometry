from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
import os

# Define the vertices of the initial triangle (in columns)
vertices = np.array([[-1, 2, -1],  # x coordinates
                    [-1, -1, 2]])  # y coordinates

# Alternative Triangle (in columns)
vertices_2 = np.array([[-300000, -300000, -200000],  # x coordinates
                      [300000, 200000, 200000]])     # y coordinates

# non dense starting triangle (in columns)
vertices_3 = np.array([[-5.2, -4.6, -5.2],  # x coordinates
                    [4.8, 4.8, 5.4]])      # y coordinates

# Standard matrices A, B, C and inverses
A = np.array([[2, -1], [1, 0]])
B = np.array([[3, 1], [-4, -1]])
C = np.array([[3, 4], [-1, -1]])
A_inverse = np.linalg.inv(A)
B_inverse = np.linalg.inv(B)
C_inverse = np.linalg.inv(C)
matrix_map = {'A': A, 'B': B, 'C': C,
              'D': A_inverse, 'E': B_inverse, 'F': C_inverse}

def unpack_sequence(sequence_str):
    """Convert a string of matrix labels into a list of matrices."""
    try:
        return [matrix_map[char] for char in sequence_str]
    except KeyError:
        print("Invalid sequence. Use only 'A', 'B', 'C', 'D', 'E', 'F'.")
        return None

def apply_sequence(matrices, points):
    """Apply a sequence of matrices to points (column-based coordinates)."""
    for matrix in matrices:
        points = np.dot(matrix, points)  # Matrix multiplication with column-based coordinates
    return points

def generate_combinations(n, labels):
    """Generate all combinations of labels of length n."""
    return [''.join(comb) for comb in product(labels, repeat=n)]

def plot_triangles(triangles, title, color, original=True, step=None):
    """Plot triangles efficiently using PolyCollection."""
    output_folder = "Spanning"
    os.makedirs(output_folder, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the original triangle
    if original:
        ax.fill(vertices[0], vertices[1], color='gray', alpha=0.5, label='Original')

    # Convert column-based coordinates to list of triangles for PolyCollection
    triangle_list = []
    for triangle in triangles:
        vertices_list = np.column_stack((triangle[0], triangle[1]))
        triangle_list.append(vertices_list)
    
    poly = PolyCollection(triangle_list, facecolors=color, alpha=0.6, edgecolors='black', linewidths=0.3)
    ax.add_collection(poly)

    # Set fixed plot limits to -10 to 10 on both axes
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
    print(f"Saving plot to: {filename}")  # Debug print
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close(fig)  # Close the figure to free memory

def apply_sequence_with_cache(sequence, points, cache):
    """Apply a sequence of matrices with caching."""
    sequence_key = tuple(sequence)
    
    if sequence_key in cache:
        return cache[sequence_key]
    
    result = points
    for label in sequence:
        result = np.dot(matrix_map[label], result)
    
    cache[sequence_key] = result
    return result

def generate_steps(max_step, labels, vertices, cache):
    """Generate transformations for all steps."""
    all_steps = []
    current_step_triangles = [vertices]
    
    for step in range(1, max_step + 1):
        print(f"Step {step}")
        
        step_labels = generate_combinations(step, labels)
        new_triangles = [
            apply_sequence_with_cache(list(comb), vertices, cache)
            for comb in step_labels
        ]
        
        current_step_triangles.extend(new_triangles)
        all_steps.append((step, new_triangles, step_labels))
    
    return all_steps

def apply_sequence_with_steps(matrices, points):
    """Apply a sequence of matrices and track steps."""
    steps = [points]
    for index, matrix in enumerate(matrices):
        points = np.dot(matrix, points)
        steps.append(points)
        print(f"Step {index + 1}:")
        print(points.T)  # Transpose for better readability
    return steps

def plot_all_combinations(max_step, labels, vertices, color='purple'):
    """Plot all possible combinations of transformations up to max_step."""
    cache = {}
    all_steps = generate_steps(max_step, labels, vertices, cache)
    
    # List to store accumulated triangles
    cumulative_triangles = []
    
    # Plot each step
    for step, step_triangles, step_labels in all_steps:
        cumulative_triangles.extend(step_triangles)
        title = f"Step {step}: Accumulated Transformations"
        plot_triangles(cumulative_triangles, title, color, original=True, step=step)
        print(f"Completed step {step} with {len(step_triangles)} new triangles") 