# A function that checks GDP growth for any country
def check_gdp_growth(country_name, years, gdp_values):
    print("\n---", country_name, "GDP Growth Check ---")
    for i in range(1, len(years)):
        growth = gdp_values[i] - gdp_values[i - 1]
        if growth > 0:
            print(years[i], "-> GROWTH of $", growth, "billion [UP]")
        elif growth == 0:
            print(years[i], "-> NO CHANGE")
        else:
            print(years[i], "-> DECLINE of $", abs(growth), "billion [DOWN]")
# Compare Nigeria vs UK GDP side by side each year
def compare_gdp(years, nigeria_gdp, uk_gdp):
    print("\n--- GDP Comparison by Year ---")
    for i in range(len(years)):
        difference = uk_gdp[i] - nigeria_gdp[i]
        if uk_gdp[i] > nigeria_gdp[i]:
            print(years[i], "-> United Kingdom leads by $", difference, "billion")
        elif nigeria_gdp[i] > uk_gdp[i]:
            print(years[i], "-> Nigeria leads by $", difference, "billion")
        else:
            print(years[i], "-> Both countries equal")
# Your data
years = [2019, 2020, 2021, 2022, 2023]
nigeria_gdp =[448, 432, 441, 477, 506]
uk_gdp = [2855, 2765, 3131, 3089, 3079]
# Call each function ONCE at the bottom
check_gdp_growth("Nigeria", years, nigeria_gdp)
check_gdp_growth("United Kingdom", years, uk_gdp)
compare_gdp(years, nigeria_gdp, uk_gdp)