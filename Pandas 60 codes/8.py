# Example 8: Pivoting with fill_value
import pandas as pd

# Creating a DataFrame
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02'],
        'City': ['NY', 'NY', 'LA', 'LA'],
        'Sales': [200, 250, 300, None]}
df = pd.DataFrame(data)

# Pivoting with fill_value
pivot_df = df.pivot(index='Date', columns='City', values='Sales').fillna(0)
print('Pivoted DataFrame with fill_value:\n', pivot_df)