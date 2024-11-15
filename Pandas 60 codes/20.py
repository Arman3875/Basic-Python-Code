# Example 20: Sorting by Multiple Columns
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 85], 'Age': [25, 30, 35, 22]}
df = pd.DataFrame(data)

# Sorting by multiple columns
sorted_df = df.sort_values(by=['Score', 'Age'], ascending=[False, True])

print('Sorted DataFrame by Multiple Columns:\n', sorted_df)