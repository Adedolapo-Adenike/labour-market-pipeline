# Variables - storing information
country_1 = "Nigeria"
country_2 = "United Kingdom"
gdp_nigeria = 477 # GDP in billions USD
gdp_uk = 3089 # GDP in billions USD
# Print - display something on screen
print("Country 1:", country_1)
print("Country 2:", country_2)
print("Nigeria GDP (USD billions):", gdp_nigeria)
print("UK GDP (USD billions):", gdp_uk)
# Your turn - calculate GDP per capita
population_nigeria = 220 # millions
gdp_per_capita = (gdp_nigeria * 1_000_000_000) / (population_nigeria * 1_000_000)
print("Nigeria GDP per capita: $", round(gdp_per_capita, 2))
# Lists - store multiple values in one variable
years = [2019, 2020, 2021, 2022, 2023]
nigeria_gdp = [448, 432, 441,477,506] # billions USD per year
uk_gdp = [2855,2765, 3131,3089,3079] # billions USD per year
print("Years tracked:", years)
print("First year:", years[0]) # 0 means first item
print("First year:", years[-1]) # -1 means last item
# Loop - repeat an action for every iteam in a list
print("\n--- Nigeria GDP by Year ---")
for year in years:
    print("Year:", year)
# Loop using index - access two lists at the same time
print("\n--- Nigeria GDP Table ---")
for i in range(len(years)):
    print(years[i], "> $", nigeria_gdp[i], "billions")
# If statements - make decisions based on conditions
print("\n--- Nigeria GDP Growth Check ---")
for i in range(1, len(years)): # start from 1 so we can look back
    growth = nigeria_gdp[i] - nigeria_gdp[i - 1]
    if growth > 0:
        print(years[i], "->GROWTH of $", growth, "billion [UP]")
    elif growth ==0:
        print(years[i], "-> NO CHANGE")
    else:
        print(years[i], "-> DECLINE of $", abs(growth), "billions [DOWN]")
# If statements - make decisions based on conditions
print("\n--- UK GDP Growth Check ---")
for i in range(1, len(years)): # start from 1 so we can look back
    growth = uk_gdp[i] - uk_gdp[i - 1]
    if growth > 0:
        print(years[i], "->GROWTH of $", growth, "billions UP")
    elif growth == 0:
        print(years[i], "-> NO CHANGE")
    else:
        print(years[i], "-> DECLINE of $", abs(growth), "billion DOWN")