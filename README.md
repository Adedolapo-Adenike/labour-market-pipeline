# Cross-Border Labour Market Intelligence Pipeline
## Nigeria & UK Economic Indicators

An end-to-end data pipeline that automatically fetches, cleans, 
and analyses economic indicators for Nigeria and the United Kingdom 
using the World Bank API.

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
- **ONS UK** - UK labour market statistics
- **Reed.co.uk API** - UK data engineering job postings

---

## Economic Indicators Tracked

- GDP (current USD billions)
- Unemployment rate (%)
- Inflation rate (%)
- Foreign Direct Investment (USD billions)

---

## Pipeline Architecture

World Bank API -> Python ingest.py -> AWS S3 -> Snowflake -> dbt -> Looker Studio

---

## Project Status

- [x] Python ingestion script
- [x] World Bank API integration
- [x] Data cleaning with pandas
- [x] 4 economic indicators
- [ ] AWS S3 upload
- [ ] Snowflake warehouse
- [ ] dbt transformations
- [ ] Airflow orchestration
- [ ] Looker Studio dashboard

---

## Author

Adedolapo Badejoko
Economics BSc | Information Science MSc
Aspiring Data Engineer | Nigeria -> UK