# Example 19: NumPy - Setting Values Using Indexing
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Setting specific values using indexing
array[[1, 3]] = [100, 200]

print('Array after Setting Values:', array)