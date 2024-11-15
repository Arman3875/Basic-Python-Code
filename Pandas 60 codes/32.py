# Example 32: Combining DataFrames with Multi-level Indexes
import pandas as pd

# Creating DataFrames with MultiIndex
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2020, 2021]]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data1 = [100, 150, 200, 250]
df1 = pd.DataFrame(data1, index=index, columns=['Sales'])

data2 = [300, 400, 500, 600]
df2 = pd.DataFrame(data2, index=index, columns=['Profit'])

# Combining DataFrames
combined_df = pd.concat([df1, df2], axis=1)

print('Combined DataFrame with Multi-level Indexes:\n', combined_df)