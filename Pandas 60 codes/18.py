# Example 18: Using style for DataFrame Styling
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)

# Applying styles using the recommended `map` method
styled_df = df.style.map( lambda x: 'background-color: yellow' if isinstance(x, int) and x > 80 else '')
print(styled_df)
