# Example 18: NumPy - Meshgrid Creation
import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Creating a meshgrid
X, Y = np.meshgrid(x, y)

print('Meshgrid X:\n', X)
print('Meshgrid Y:\n', Y)