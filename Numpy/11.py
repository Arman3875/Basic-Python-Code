# Example 11: NumPy - Random Array Generation
import numpy as np

# Generating random arrays
random_array = np.random.rand(3, 3)  # Random values in a 3x3 array
normal_array = np.random.randn(3, 3)  # Random values with a normal distribution

print('Random Array:\n', random_array)
print('Normal Distribution Array:\n', normal_array)