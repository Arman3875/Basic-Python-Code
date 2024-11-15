# Example 10: Using pivot_table with Multiple Indexes
import pandas as pd

# Creating a DataFrame
data = {'City': ['NY', 'LA', 'NY', 'SF', 'LA'], 
        'Year': [2020, 2020, 2021, 2021, 2020], 
        'Sales': [100, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Creating a pivot table with multiple indexes
pivot_table = pd.pivot_table(df, values='Sales', index=['City', 'Year'], aggfunc='sum')
print('Pivot Table with Multiple Indexes:\n', pivot_table)