# Example 57: Merging with Indicator for Tracking Source
import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [3, 4, 5], 'Name': ['Charlie', 'David', 'Edward']})

# Merging with indicator to track the source
merged_df = pd.merge(df1, df2, on='ID', how='outer', indicator=True)

print('Merged DataFrame with Indicator:\n', merged_df)