# Example 13: MultiIndex Slicing
import pandas as pd

# Creating a MultiIndex DataFrame 
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2020, 2021]]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

# Slicing the MultiIndex DataFrame
sliced_df = df.loc['A']
print('Sliced MultiIndex DataFrame:\n', sliced_df)