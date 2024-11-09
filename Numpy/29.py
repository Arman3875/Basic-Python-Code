# Example 29: NumPy - Using np.choose for Multiple Conditions
import numpy as np

# Creating arrays for conditions
array = np.array([2, 1, 6, 3])
choices = [list(array*2), list(array+10), list(array**2)]

# Using np.choose to apply different conditions
result = np.choose([2,1,0,1], choices)

print('Result using np.choose:', result)