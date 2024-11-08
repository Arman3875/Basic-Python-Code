# Example 1: NumPy - Array Creation Basics
import numpy as np

# Creating arrays with different functions
array_zeros = np.zeros((3, 3))
array_ones = np.ones((2, 2))
array_full = np.full((2, 2), 7)
array_range = np.arange(10)

print('Array of Zeros:\n', array_zeros)
print('Array of Ones:\n', array_ones)
print('Array with All Elements as 7:\n', array_full)
print('Array with Range of Numbers:', array_range)