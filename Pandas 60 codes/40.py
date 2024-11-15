# Example 40: Creating Custom Indexes with MultiIndex
import pandas as pd

# Creating a MultiIndex from tuples
index = pd.MultiIndex.from_tuples([('A', 2020), ('A', 2021), ('B', 2020), ('B', 2021)], names=['Category', 'Year'])
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

print('DataFrame with Custom MultiIndex:\n', df)