# Example 47: Using ffill and bfill for Missing Values
import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan]}
df = pd.DataFrame(data)

# Using ffill and bfill to fill missing values
df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')

print('DataFrame with Forward Fill:\n', df_ffill)
print('DataFrame with Backward Fill:\n', df_bfill)