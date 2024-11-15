# Example 23: Pandas - Query Method for Conditional Filtering
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)

# Using query for filtering
filtered_df = df.query('Score > 80')
print('Filtered DataFrame using query:\n', filtered_df)