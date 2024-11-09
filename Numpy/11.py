# Example 11: NumPy - Extracting Upper Triangle of a Matrix
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the upper triangle (above the main diagonal)
upper_triangle = np.triu(matrix)

print('Upper Triangle of the Matrix:\n', upper_triangle)