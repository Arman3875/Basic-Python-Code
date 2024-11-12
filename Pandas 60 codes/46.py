# Working with timezones

import pandas as pd

# Creating a time series with a timezone
date_range = pd.date_range(start='2024-01-01', periods=5, freq= 'D', tz='UTC')
data = {'sales':[100,200,150,250,300]}
df = pd.DataFrame(data, index =date_range)

# Converting to a different timezone
df = df.tz_convert('US/Eastern')
print('Time series dataFrame with timezone:\n',df)
