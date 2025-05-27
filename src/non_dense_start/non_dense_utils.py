"""
Module for visualizing triangle transformations using standard matrices.
Uses matrices A, B, C and their inverses (D, E, F) for transformations.
"""
import numpy as np
from src.utils.shared_utils import plot_all_combinations

# Define the vertices of the initial triangle (in columns)
vertices = np.array([[5.2, 4.6, 5.2],  # x coordinates
                    [4.8, 4.8, 5.4]])  # y coordinates

def create_matrix_map():
    """Create the matrix map for standard matrices.
    
    Returns:
        dict: A dictionary mapping labels to matrices:
        - 'A': Standard matrix A
        - 'B': Standard matrix B
        - 'C': Standard matrix C
        - 'D': Inverse of A
        - 'E': Inverse of B
        - 'F': Inverse of C
    """
    # Define standard matrices
    A = np.array([[2, -1], [1, 0]])
    B = np.array([[3, 1], [-4, -1]])
    C = np.array([[3, 4], [-1, -1]])
    
    # Calculate inverses
    A_inverse = np.linalg.inv(A)
    B_inverse = np.linalg.inv(B)
    C_inverse = np.linalg.inv(C)
    
    # Create matrix map
    return {
        'A': A, 'B': B, 'C': C,
        'D': A_inverse, 'E': B_inverse, 'F': C_inverse
    }

def run_standard_visualization(max_step=7, colors=None):
    """Run the standard matrices visualization task.
    
    Args:
        max_step: Maximum number of transformation steps
        colors: Dictionary mapping matrix types to colors. If None, uses default colors.
    """
    if colors is None:
        colors = {
            'original': 'gray',
            'transformed': 'purple'
        }
    
    matrix_map = create_matrix_map()
    labels = 'ABCDEF'  # Labels for matrices
    
    print("\nProcessing standard matrices...")
    plot_all_combinations(
        max_step=max_step,
        labels=labels,
        vertices=vertices,
        matrix_map=matrix_map,
        color=colors['transformed'],
        output_folder="Spanning_non_dense",
        title_prefix="(Non dense start)"
    ) 