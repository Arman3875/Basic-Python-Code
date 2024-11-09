# Example 17: NumPy - Indexing with np.where()
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Using np.where to find indices where elements are greater than 25
indices = np.where(array > 25)

print('Indices where elements > 25:', indices)
print('Values where elements > 25:', array[indices])