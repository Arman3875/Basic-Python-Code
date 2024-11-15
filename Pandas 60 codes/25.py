# Example 25: Adding a Prefix or Suffix to Column Names
import pandas as pd

# Creating a DataFrame
data = {'Math': [90, 80], 'Science': [85, 88]}
df = pd.DataFrame(data)

# Adding a prefix to column names
df_prefixed = df.add_prefix('Grade_')

# Adding a suffix to column names
df_suffixed = df.add_suffix('_Score')

print('DataFrame with Prefix:\n', df_prefixed)
print('DataFrame with Suffix:\n', df_suffixed)