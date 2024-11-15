# Example 23: Setting and Resetting Indexes
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'SF'], 'Year': [2020, 2021, 2021], 'Sales': [100, 200, 300]}
df = pd.DataFrame(data)

# Setting an index
df.set_index('City', inplace=True)

print('DataFrame after Setting Index:\n', df)

# Resetting the index
df.reset_index(inplace=True)

print('DataFrame after Resetting Index:\n', df)