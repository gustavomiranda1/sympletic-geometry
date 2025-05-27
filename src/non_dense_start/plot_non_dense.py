"""
Script to run triangle transformations using h_k matrices.
For each k value (2, 4, 5, 9), generates visualizations using h_k, h_k inverse, t, and t inverse matrices.
"""
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.non_dense_start.non_dense_utils import run_standard_visualization

def main():
    """Main function to demonstrate the triangle transformations using standard matrices."""
    colors={'transformed': 'purple', 'original': 'gray'}
    print("Starting to generate transformations with standard matrices...")  # Debug print
    run_standard_visualization(max_step=9, colors=colors)
    print("All steps completed!")  # Debug print

if __name__ == "__main__":
    main() 