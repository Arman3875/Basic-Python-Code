# Example 31: Using pd.cut for Binning Data
import pandas as pd

# Creating a DataFrame
data = {'Scores': [50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)

# Binning the scores into categories
df['Grade'] = pd.cut(df['Scores'], bins=[0, 59, 69, 79, 89, 100], labels=['F', 'D', 'C', 'B', 'A'])

print('DataFrame with Binned Scores:\n', df)