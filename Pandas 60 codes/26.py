# Example 26: Using applymap for Element-wise Operations
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Applying an operation to each element in the DataFrame
df_transformed = df.applymap(lambda x: x**2)

print('DataFrame with Squared Values:\n', df_transformed)