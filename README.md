# Triangle Transformations Visualization

This project visualizes triangle transformations using different sets of matrices.

## Project Structure

```
src/
├── utils/
│   └── shared_utils.py      # Shared plotting and transformation utilities
├── standard_matrices/
│   ├── standard_triangle_utils.py  # Standard matrices (A, B, C) definitions
│   └── plot_triangles.py    # Script to run standard matrices visualization
├── non_dense_start/
│   ├── non_dense_utils.py  # Standard matrices (A, B, C) definitions
│   └── plot_non_dense.py    # Script to run standard matrices visualization
└── hk_matrices/
    ├── hk_triangle_utils.py # h_k matrices definitions
    └── plot_hk_triangles.py # Script to run h_k matrices visualization
```

## Running the Visualizations

### Standard Matrices (A, B, C)
```bash
cd src/standard_matrices
python plot_triangles.py
```
This will generate plots in the `Spanning_standard` directory.

### h_k Matrices
```bash
cd src/hk_matrices
python plot_hk_triangles.py
```
This will generate plots in the `Spanning_hk` directory.

## Output
- Each visualization creates a series of plots showing the accumulated transformations
- Plots are saved in their respective directories (`Spanning_standard` or `Spanning_hk`)
- Each step shows the accumulated transformations up to that point 
