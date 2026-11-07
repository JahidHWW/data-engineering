# Earthquake ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Python to process earthquake data from the United States Geological Survey (USGS).

The pipeline reads earthquake records from a downloaded CSV file, transforms and validates the data to improve consistency and reliability, and loads the cleaned records into a PostgreSQL database for further analysis.

**Data Source:** [USGS Earthquake Catalog](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv)

**Dataset:** 9,728 earthquake records from a 30-day USGS CSV snapshot.

## Technologies

- Python
- PostgreSQL
- Docker
- psycopg
- pytest

## ETL Pipeline

### Extract

extract.py uses Python's built-in csv module and pathlib to read earthquake data from a local CSV file.

Using csv.DictReader, each CSV row is converted into a dictionary. The function returns a list of dictionaries representing the extracted earthquake records.

### Transform

Validation includes:

- Checking for missing dictionary fields
- Rejecting empty values
- Handling invalid numeric values
- Converting magnitude and depth values into floating-point numbers

Invalid records return None, while valid records are returned as cleaned dictionaries.

### Load

load.py uses psycopg to insert validated earthquake records into PostgreSQL.

The load_earthquake() function accepts an existing database connection and an earthquake dictionary, then executes a parameterized SQL INSERT statement.

Duplicate earthquake IDs are handled using ON CONFLICT (id) DO NOTHING, allowing the pipeline to be rerun without inserting duplicate records.

### Pipeline Execution

pipeline.py connects the extraction, transformation, and loading stages. It reads the source CSV, processes each record, filters out invalid records, and loads the accepted records into PostgreSQL using a shared database connection.

## SQL Analysis and Key Findings

| Metric | Result |
|---|---:|
| Earthquakes analyzed | 9,728 |
| Average magnitude | 1.79 |
| Small earthquakes | 6,619 |
| Moderate earthquakes | 1,965 |
| Larger earthquakes | 1,144 |
| Average depth - Small | 14.12 km |
| Average depth - Moderate | 29.20 km |
| Average depth - Larger | 72.54 km |
| Negative-depth records | 283 |

### Key Observations

- Although larger-magnitude earthquakes have greater average depths in this dataset, smaller-magnitude earthquakes can occur at greater depths than individual larger-magnitude earthquakes.
- Approximately **2.9% of earthquakes (283 records)** have negative depth values. These values were preserved for further investigation rather than automatically modified.
- The average earthquake magnitude across the **9,728 records analyzed was 1.79**.

## Automated Testing

I implemented eight automated tests using pytest to validate the earthquake transformation function.

These tests cover valid earthquake records, missing fields, empty values, and invalid numerical data. All eight tests passed successfully.