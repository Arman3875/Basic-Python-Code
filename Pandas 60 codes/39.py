# Example 39: Using Custom Functions with Groupby
import pandas as pd

# Creating a DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Applying a custom function with groupby
grouped_df = df.groupby('Category')['Value'].apply(lambda x: x.max() - x.min())

print('Custom Aggregation Result:\n', grouped_df)