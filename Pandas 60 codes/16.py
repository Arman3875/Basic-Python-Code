# Example 16: Creating Time Series with Business Days
import pandas as pd

# Creating a time series with business days only
date_range = pd.date_range(start='2023-01-01', periods=10, freq='B')
data = {'Sales': range(10)}
df = pd.DataFrame(data, index=date_range)

print('Time Series DataFrame with Business Days:\n', df)