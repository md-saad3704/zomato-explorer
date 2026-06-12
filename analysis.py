# Analytics and data processing functions

import pandas as pd

from config import DATA_PATH


def load_raw_data():
    """
    Load the raw Zomato dataset from Excel.

    Returns:
        pd.DataFrame: Raw dataset.
    """
    df = pd.read_excel(DATA_PATH)

    return df


def get_dataset_summary(df):
    """
    Generate a high-level summary of the dataset.

    Args:
        df (pd.DataFrame): Raw dataset

    Returns:
        dict: Dataset summary metrics
    """

    summary = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "total_cities": df["city"].nunique(),
        "unique_restaurant_names": df["name"].nunique()
    }

    return summary

## Missing value Report

def get_missing_value_report(df):
    """
    Generate missing value statistics.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    missing_report = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isnull().sum().values,
        "missing_percentage": (
            df.isnull().sum() / len(df) * 100
        ).round(2).values
    })

    missing_report = missing_report.sort_values(
        by="missing_percentage",
        ascending=False
    )

    return missing_report

##City Distribution

def get_city_distribution(df):
    """
    Calculate restaurant count per city.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame
    """

    city_distribution = (
        df["city"]
        .value_counts()
        .reset_index()
    )

    city_distribution.columns = [
        "city",
        "restaurant_count"
    ]

    return city_distribution