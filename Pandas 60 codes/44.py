# Example 44: Using drop_duplicates() for Unique Rows
import pandas as pd

# Creating a DataFrame with duplicate rows
data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie'], 'Score': [85, 70, 85, 95]}
df = pd.DataFrame(data)

# Dropping duplicate rows
unique_df = df.drop_duplicates()

print('DataFrame after Dropping Duplicates:\n', unique_df)