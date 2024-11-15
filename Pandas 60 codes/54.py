# Example 54: DataFrame Info and Memory Usage
import pandas as pd

# Creating a DataFrame
data = {'A': range(1000), 'B': range(1000, 2000)}
df = pd.DataFrame(data)

# Displaying DataFrame info and memory usage
df_info = df.info(memory_usage='deep')

print('DataFrame Info and Memory Usage:', df_info)