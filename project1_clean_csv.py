import pandas as pd

# Load the messy CSV
df = pd.read_csv("fresh_messy_sales.csv")

# Clean customer names
df["Customer Name"] = df["Customer Name"].str.strip().str.title()

# Convert price to numeric (turns bad values into NaN)
df["Sale Price"] = pd.to_numeric(df["Sale Price"].astype(str).strip(), errors='coerce')

# Convert quantity to numeric
df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')

# Convert date to datetime format
df["Purchase Date"] = pd.to_datetime(df["Purchase Date"], dayfirst=True, errors="coerce")

# Print result
print(df)

# Optional: export cleaned version
df.to_csv("cleaned_sales_output.csv", index=False)
