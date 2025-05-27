"""
Script to run triangle transformations using h_k matrices.
For each k value (2, 4, 5, 9), generates visualizations using h_k, h_k inverse, t, and t inverse matrices.
"""
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.hk_matrices.hk_triangle_utils import run_hk_visualization

def main():
    """Run visualizations for all k values with different colors."""
    # Define colors for each k value
    colors = {
        2: 'blue',   # k=2: blue
        4: 'green',  # k=4: green
        5: 'red',    # k=5: red
        9: 'purple'  # k=9: purple
    }
    
    print("Starting h_k matrix transformations...")
    run_hk_visualization(max_step=8, colors=colors)
    print("All transformations completed!")

if __name__ == "__main__":
    main() 