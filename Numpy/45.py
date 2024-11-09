# Example 45: NumPy - Slicing with Step
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Slicing with a step
step_slice = array[::2]  # Every second element

print('Sliced Array with Step 2:', step_slice)