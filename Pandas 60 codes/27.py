# Example 27: Using df.apply with Axis Parameter
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Applying a function to rows and columns using the axis parameter
row_sum = df.apply(lambda x: x.sum(), axis=1)
col_sum = df.apply(lambda x: x.sum(), axis=0)

print('Row-wise Sum:\n', row_sum)
print('Column-wise Sum:\n', col_sum)