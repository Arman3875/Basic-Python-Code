# Example 55: Melting DataFrames
import pandas as pd

# Creating a DataFrame
data = {'ID': [1, 2], 'Math': [90, 80], 'Science': [85, 88]}
df = pd.DataFrame(data)

# Melting the DataFrame
melted_df = pd.melt(df, id_vars=['ID'], value_vars=['Math', 'Science'], var_name='Subject', value_name='Score')

print('Melted DataFrame:\n', melted_df)