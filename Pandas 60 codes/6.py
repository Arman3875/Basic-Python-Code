# Pivoting DataFrames

import pandas as pd

# Creating a DataFrame
date = {'Date': ['2023-02-01','2023-02-02', '2023-02-01', '2023-02-02'],
'City':['NY','NY','LA','LA'],
'Sales':[200,225,345,455]}
df =pd.DataFrame(date)

# Pivoting the DataFrame
pivot_df = df.pivot(index='Date', columns='City', values='Sales')
print("pivoted DataFrame: \n", pivot_df)