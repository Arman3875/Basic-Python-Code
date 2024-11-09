# Example 49: NumPy - Basic Indexing and Slicing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# Accessing elements by index
first_element = array[0]
last_element = array[-1]

# Slicing the array
slice_array = array[1:4]

print('First Element:', first_element)
print('Last Element:', last_element)
print('Sliced Array:', slice_array)