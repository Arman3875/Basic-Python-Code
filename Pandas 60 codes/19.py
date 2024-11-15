# Example 19: Stacking and Unstacking DataFrames
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA'], '2020': [100, 150], '2021': [200, 250]}
df = pd.DataFrame(data).set_index('City')

# Stacking and unstacking the DataFrame
stacked_df = df.stack()
unstacked_df = stacked_df.unstack()

print('Stacked DataFrame:\n', stacked_df)
print('Unstacked DataFrame:\n', unstacked_df)