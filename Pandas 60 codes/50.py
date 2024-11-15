# Example 50: Applying Multiple Functions with Groupby
import pandas as pd

# Creating a DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Applying multiple functions with groupby
grouped_df = df.groupby('Category')['Value'].agg(['mean', 'sum', 'max'])

print('Grouped DataFrame with Multiple Functions:\n', grouped_df)