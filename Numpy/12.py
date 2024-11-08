# Example 12: NumPy - Boolean Indexing
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# Boolean indexing
even_numbers = array[array % 2 == 0]

print('Original Array:', array)
print('Even Numbers:', even_numbers)