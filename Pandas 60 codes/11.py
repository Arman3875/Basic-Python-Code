# Example 11: Creating a Pivot Table with Multiple Aggregations
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'NY', 'SF', 'LA'], 
        'Year': [2020, 2020, 2021, 2021, 2020], 
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Creating a pivot table with multiple aggregations
pivot_table = pd.pivot_table(df, values='Sales', index='City', columns='Year', aggfunc=['sum', 'mean'])
print('Pivot Table with Multiple Aggregations:\n', pivot_table)
