# Example 2:Resampling with Different Aggregations
import pandas as pd

# Creating a time series DataFrame
date_range = pd.date_range(start='2023-01-01', periods=30, freq='D')
data = {'Sales': range(30)}
df = pd.DataFrame(data, index=date_range)

# Resampling with different aggregations
resampled_df = df.resample('W').agg({'Sales' : ['sum', 'mean', 'max']})
print('Resampled DataFrame with Different Aggregations:\n', resampled_df)