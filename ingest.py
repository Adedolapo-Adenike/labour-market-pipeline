import requests
import csv

# World Bank indicator codes
INDICATORS = {
    'gdp_billions': 'NY.GDP.MKTP.CD',
    'unemployment_rate': 'SL.UEM.TOTL.ZS',
    'inflation_rate': 'FP.CPI.TOTL.ZG'
}

# Function to fetch any indicator for any country
def fetch_indicator(country_code, country_name, indicator_code, indicator_name):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=10"
    response = requests.get(url)
    data = response.json()
    records = data[1]

    results = []
    for record in records:
        year = record['date']
        value = record['value']

        if value is not None:
            if indicator_name == 'gdp_billions':
                value = round(value / 1_000_000_000, 2)
            else:
                value = round(value, 2)

            results.append({
                'country': country_name,
                'year': year,
                indicator_name: value
            })

    return results

# Fetch all indicators for both countries
print("Fetching GDP data...")
nigeria_gdp = fetch_indicator("NG", "Nigeria", INDICATORS['gdp_billions'], 'gdp_billions')
uk_gdp = fetch_indicator("GB", "United Kingdom", INDICATORS['gdp_billions'], 'gdp_billions')

print("Fetching unemployment data...")
nigeria_unemployment = fetch_indicator("NG", "Nigeria", INDICATORS['unemployment_rate'], 'unemployment_rate')
uk_unemployment = fetch_indicator("GB", "United Kingdom", INDICATORS['unemployment_rate'], 'unemployment_rate')

print("Fetching inflation data...")
nigeria_inflation = fetch_indicator("NG", "Nigeria", INDICATORS['inflation_rate'], 'inflation_rate')
uk_inflation = fetch_indicator("GB", "United Kingdom", INDICATORS['inflation_rate'], 'inflation_rate')

# Combine all data
all_data = nigeria_gdp + uk_gdp + nigeria_unemployment + uk_unemployment + nigeria_inflation + uk_inflation

# Save to CSV
with open('economic_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['country', 'year', 'gdp_billions', 'unemployment_rate', 'inflation_rate'])
    writer.writeheader()
    writer.writerows(all_data)

print("\nData saved successfully to economic_data.csv")
print("Total records saved:", len(all_data))