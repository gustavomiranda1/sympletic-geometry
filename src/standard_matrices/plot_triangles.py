import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.standard_matrices.standard_triangle_utils import run_standard_visualization

def main():
    """Main function to demonstrate the triangle transformations using standard matrices."""
    colors={'transformed': 'purple', 'original': 'gray'}
    print("Starting to generate transformations with standard matrices...")  # Debug print
    run_standard_visualization(max_step=8, colors=colors)
    print("All steps completed!")  # Debug print

if __name__ == "__main__":
    main()