# Zomato India Restaurant Explorer

An interactive multi-city restaurant analytics dashboard built using Python, Pandas, Plotly, and Streamlit.

## Project Overview

This project analyzes 224,000+ restaurant records from the Zomato India Restaurants dataset and transforms raw restaurant data into interactive city-level insights.

The dashboard is designed to help users explore restaurant trends, cuisine preferences, locality patterns, pricing insights, and hidden gems across Indian cities.

## Dataset

* Source: Kaggle Zomato India Restaurants Dataset
* Records: 224,520+
* Cities Covered: 83
* Data Collection Year: 2019

## Features (Planned)

* City-wise restaurant exploration
* KPI dashboard
* Cuisine analytics
* Locality analysis
* Hidden gems finder
* Dining mode comparison
* Multi-city comparison
* Smart restaurant search
* Data transparency section
* Zomato verification links

## Data Engineering Pipeline

Raw Excel Dataset

→ Data Audit

→ Data Cleaning

→ Schema Validation

→ Parquet Dataset

→ Analytics Layer

→ Streamlit Dashboard

## Cleaning Steps Implemented

* Removed invalid restaurant names
* Converted NEW ratings to missing values
* Converted zero ratings to missing values
* Converted zero cost values to missing values
* Standardized city names
* Standardized text columns
* Generated processed Parquet dataset

## Project Structure

zomato/

├── data/

├── analysis.py

├── data_cleaning.py

├── run_cleaning.py

├── app.py

├── styles.py

├── utils.py

├── config.py

└── tests/

## Tech Stack

* Python
* Pandas
* NumPy
* PyArrow
* Plotly
* Streamlit

## Status

Phase 1: Data Audit ✅

Phase 2: Data Quality Analysis ✅

Phase 3: Data Cleaning Pipeline ✅

Phase 4: Analytics Engine 🔄 In Progress
