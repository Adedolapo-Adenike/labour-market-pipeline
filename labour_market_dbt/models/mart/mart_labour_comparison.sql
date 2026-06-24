-- Mart model: Final labour market comparison table
-- This model creates a side by side comparison of Nigeria and UK
-- Ready for Looker Studio dashboard

WITH staging AS (
    SELECT *
    FROM {{ ref('stg_economic_data') }}
),

nigeria AS (
    SELECT
        year,
        gdp_billions AS nigeria_gdp,
        unemployment_rate AS nigeria_unemployment,
        inflation_rate AS nigeria_inflation,
        fdi_billions AS nigeria_fdi
    FROM staging
    WHERE country = 'Nigeria'
),

uk AS (
    SELECT
        year,
        gdp_billions AS uk_gdp,
        unemployment_rate AS uk_unemployment,
        inflation_rate AS uk_inflation,
        fdi_billions AS uk_fdi
    FROM staging
    WHERE country = 'United Kingdom'
)

SELECT
    n.year,
    n.nigeria_gdp,
    u.uk_gdp,
    n.nigeria_unemployment,
    u.uk_unemployment,
    n.nigeria_inflation,
    u.uk_inflation,
    n.nigeria_fdi,
    u.uk_fdi,
    ROUND(u.uk_gdp - n.nigeria_gdp, 2) AS gdp_gap,
    ROUND(n.nigeria_inflation - u.uk_inflation, 2) AS inflation_gap
FROM nigeria n
JOIN uk u ON n.year = u.year
ORDER BY n.year