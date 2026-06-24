-- Staging model : Clean and standardise raw economic data
-- This model removes incomplete rows and renames columns  clearly
WITH source AS (SELECT country, year, gdp_billions, unemployment_rate, inflation_rate,fdi_billions FROM {{ source('raw', 'ECONOMIC_DATA')}})
SELECT country, year, gdp_billions, unemployment_rate, inflation_rate,fdi_billions, 'World Bank API' AS data_source 
FROM source
WHERE gdp_billions IS NOT NULL AND inflation_rate IS NOT NULL AND fdi_billions IS NOT NULL 