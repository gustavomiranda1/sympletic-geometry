import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the initial triangle
vertices = np.array([[-1, -1], [2, -1], [-1, 2]])

# Define monodromy matrices
M1 = np.array([[2, -1], [1, 0]])
M2 = np.array([[3, 1], [-4, -1]])
M3 = np.array([[3, 4], [-1, -1]])

# Function to apply matrix to a set of points
def apply_monodromy(matrix, points):
    return np.dot(points, matrix.T)

# Initial plot
plt.figure(figsize=(8, 6))
plt.plot(*zip(*np.append(vertices, [vertices[0]], axis=0)), 'o-', label='Original Triangle')

# Apply each matrix once to see individual effects
matrices = [M1, M2, M3]
colors = ['orange', 'green', 'red']

for i, matrix in enumerate(matrices):
    transformed = apply_monodromy(matrix, vertices)
    plt.plot(*zip(*np.append(transformed, [transformed[0]], axis=0)), 'o--', color=colors[i], label=f'Transformed by M{i+1}')

# Set coordinate limits and labels
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monodromy Action on Moment Triangle')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid()
plt.show()