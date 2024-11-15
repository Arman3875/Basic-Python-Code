# Example 33: Concatenating DataFrames
import pandas as pd

# Creating DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Concatenating DataFrames
concat_df = pd.concat([df1, df2], ignore_index=True)

print('Concatenated DataFrame:\n', concat_df)