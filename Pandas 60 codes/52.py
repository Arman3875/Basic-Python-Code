# Example 52: Handling Missing Values with Custom Functions
import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 'Age': [25, np.nan, 35, 40]}
df = pd.DataFrame(data)

# Filling missing values using a custom function
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)

print('DataFrame after Handling Missing Values:\n', df)