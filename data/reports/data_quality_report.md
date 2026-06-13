# Data Quality Report

## Dataset Overview

* Total Rows: 224,520
* Total Columns: 18
* Total Cities: 83
* Unique Restaurant Names: 146,658

## Missing Values

### Highest Missing Columns

| Column      | Missing % |
| ----------- | --------- |
| famous_food | 76.61%    |
| timings     | 1.32%     |
| address     | 0.80%     |

## Rating Analysis

Special values identified:

* NEW: 27,731 records
* 0 Rating: 52,052 records

Cleaning action:

* Converted NEW → NaN
* Converted 0 → NaN

## Cost Analysis

Zero-cost records identified:

* 3,648 records

Cleaning action:

* Converted 0 → NaN

## Duplicate Analysis

* Exact Duplicates: 0
* Outlet Duplicates: 927

## Cleaning Summary

Removed invalid restaurant names:

* Missing names
* Datetime values
* Time values

Total removed records: 6

Final cleaned dataset:

* Rows: 224,514
* Cities: 83
