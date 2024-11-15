# Example 7: Using df.pivot with MultiIndex Columns
import pandas as pd

# Creating a DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'],
        'Type': ['Online', 'Store', 'Online', 'Store'],
        'Sales': [200, 250, 300, 350]}
df = pd.DataFrame(data)

# Pivoting to create a DataFrame with MultiIndex columns
pivot_df = df.pivot(index='Date', columns=['City', 'Type'], values='Sales')
print('Pivoted DataFrame with MultiIndex Columns:\n', pivot_df)