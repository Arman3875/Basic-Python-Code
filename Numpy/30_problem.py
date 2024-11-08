# Example 30: NumPy - Combining Multiple Indexing Techniques
import numpy as np

# Creating a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Combining boolean, fancy, and slice indexing
result = array_2d[array_2d > 30][:, [0, 2]]

print('Combined Indexing Result:', result)