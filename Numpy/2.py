# Example 2: NumPy - 2D Array Indexing
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing individual elements
element = array_2d[1, 2]  # Accessing element at row 1, column 2

# Slicing rows and columns
row_slice = array_2d[0, :]  # First row
column_slice = array_2d[:, 1]  # Second column

print('Element at (1,2):', element)
print('First Row:', row_slice)
print('Second Column:', column_slice)