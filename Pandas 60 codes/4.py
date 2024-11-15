# Example 4: Using query() with Variables
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 70, 95]}
df = pd.DataFrame(data)

# Using query() with variables
threshold = 80
filtered_df = df.query('Score > @threshold')
print('Filtered DataFrame with query() and Variables:\n', filtered_df)