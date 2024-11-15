# Example 36: Pandas - Renaming Index and Columns
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob'], 'Score': [85, 90]}
df = pd.DataFrame(data, index=['Row1', 'Row2'])

# Renaming index and columns
df_renamed = df.rename(index={'Row1': 'Student1', 'Row2': 'Student2'}, columns={'Score': 'Grade'})
print('Renamed DataFrame:\n', df_renamed)
