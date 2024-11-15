import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95, 60]}
df = pd.DataFrame(data)

# Applying styles to highlight scores above 80
styled_df = df.style.applymap(
    lambda x: 'background-color: yellow' if isinstance(x, int) and x > 80 else ''
)

# Exporting to HTML
styled_html = styled_df._render_html()
with open("styled_dataframe.html", "w") as f:
    f.write(styled_html)

print("Styled DataFrame exported to 'styled_dataframe.html'. Open it in a browser to view.")
