# Example 41: Using DataFrame.eval for Efficient Calculations
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Using eval for calculations
df['C'] = df.eval('A + B * 2')

print('DataFrame with Evaluated Calculations:\n', df)