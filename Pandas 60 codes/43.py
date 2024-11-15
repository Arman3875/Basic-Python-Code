# Example 43: Detecting and Replacing Outliers
import pandas as pd
import numpy as np

# Creating a DataFrame
data = {'Values': [10, 12, 14, 100, 15, 13, 12]}
df = pd.DataFrame(data)

# Detecting outliers using the IQR method
Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['Values'] < (Q1 - 1.5 * IQR)) | (df['Values'] > (Q3 + 1.5 * IQR))

# Replacing outliers with the median
df.loc[outliers, 'Values'] = df['Values'].median()

print('DataFrame after Replacing Outliers:\n', df)