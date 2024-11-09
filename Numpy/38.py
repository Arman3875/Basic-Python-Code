# Example 12: NumPy - Combining Boolean and Fancy Indexing
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Boolean condition combined with specific indices
result = array[(array > 10) & (array < 30)][[0, 2]]

print('Combined Boolean and Fancy Indexing Result:', result)