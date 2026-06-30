# Cross-Border Labour Market Intelligence Pipeline
## Nigeria & UK Economic Indicators

An end-to-end data pipeline that automatically fetches, cleans, 
and analyses economic indicators for Nigeria and the United Kingdom 
using the World Bank API.

---

## Live Dashboard

View the interactive dashboard here:
https://datastudio.google.com/s/phcV0Wt-4FE

The dashboard shows:
- Nigeria vs UK GDP comparison (2016-2024)
- Nigeria vs UK Unemployment comparison
- Nigeria vs UK Inflation comparison
- GDP Gap trend over time
- Inflation Gap trend over time
- Key economic metrics scorecard

---

## Project Purpose

This pipeline tracks key economic indicators that drive labour 
migration between Nigeria and the UK, including GDP, unemployment, 
inflation, and foreign direct investment (FDI).

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data ingestion and cleaning |
| pandas | Data transformation and merging |
| World Bank API | Source of economic data |
| AWS S3 | Cloud data storage |
| Snowflake | Data warehouse |
| dbt | Data transformation models |
| Apache Airflow | Pipeline orchestration |
| Looker Studio | Dashboard and visualisation |
| GitHub | Version control and portfolio |

---

## Data Sources

- **World Bank API** - GDP, unemployment, inflation, FDI

---

## Economic Indicators Tracked

- GDP (current USD billions)
- Unemployment rate (%)
- Inflation rate (%)
- Foreign Direct Investment (USD billions)

---

## Pipeline Architecture

World Bank API -> Python ingest.py -> AWS S3 -> Snowflake -> dbt -> Airflow -> Looker Studio

---

## Project Status

- [x] Python ingestion script
- [x] World Bank API integration
- [x] Data cleaning with pandas
- [x] 4 economic indicators
- [x] AWS S3 upload
- [x] Snowflake warehouse
- [x] dbt transformations
- [x] Airflow orchestration
- [x] Looker Studio dashboard

---

## Author

Adedolapo Badejoko
Economics BSc | Information Science MSc
Aspiring Data Engineer | Nigeria -> UK