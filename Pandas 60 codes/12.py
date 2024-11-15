# Example 12: Using pipe() for Method Chaining
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Score': [85, 70, 95]}
df = pd.DataFrame(data)

# Custom function for modifying the DataFrame
def add_grade_column(df):
    df['Grade'] = df['Score'].apply(lambda x: 'A' if x >= 90 else 'B')
    return df
# Using pipe for method

chaining_df = df.pipe(add_grade_column)
print('DataFrame after Using pipe():\n', df)