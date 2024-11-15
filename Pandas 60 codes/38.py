# Example 38: Creating Custom Aggregations with Groupby
import pandas as pd

# Creating a DataFrame
data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Using groupby with custom aggregation
custom_agg = df.groupby('Category').agg(max_value=('Value', 'max'), min_value=('Value', 'min'))

print('Custom Aggregation Result:\n', custom_agg)