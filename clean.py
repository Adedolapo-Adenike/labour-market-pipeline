import pandas as pd

# Load the raw economic data
df = pd.read_csv('economic_data.csv')

# Separate each indicator into its own dataframe
gdp = df[['country', 'year', 'gdp_billions']].dropna()
unemployment = df[['country', 'year', 'unemployment_rate']].dropna()
inflation = df[['country', 'year', 'inflation_rate']].dropna()

# Merge all three together on country and year
merged = gdp.merge(unemployment, on=['country', 'year'], how='outer')
merged = merged.merge(inflation, on=['country', 'year'], how='outer')

# Sort by country and year
merged = merged.sort_values(['country', 'year']).reset_index(drop=True)

# Print the result
print("--- Combined Economic Data ---")
print(merged.to_string())

print("\n--- Shape ---")
print(merged.shape)

# Save to new CSV
merged.to_csv('combined_data.csv', index=False)
print("\nSaved to combined_data.csv")