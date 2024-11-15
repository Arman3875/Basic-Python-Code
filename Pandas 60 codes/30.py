# Example 30: Using at and iat for Fast Scalar Access
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Accessing a single value using at and iat
value_at = df.at[1, 'A']
value_iat = df.iat[1, 0]

print('Value using at:', value_at)
print('Value using iat:', value_iat)