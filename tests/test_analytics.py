import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)


from analysis import (
    load_clean_data,
    get_city_data,
    extract_cuisines,
    get_city_kpis,
    get_top_cuisines,
    get_top_localities,
    get_locality_cost_analysis,
    get_highest_rated_areas,
    get_hidden_gems
    
)

# Validation script for city-specific analysis and cuisine extraction.

df = load_clean_data()

city_df = get_city_data(
    df,
    "Lucknow"
)

print(
    f"Total Restaurants: {len(city_df)}"
)

print(
    city_df[
        ["name", "city"]
    ].head()
)

# Extract cuisines and analyze popularity


cuisines = extract_cuisines(city_df)

print("\nTop 10 Cuisines")

print(
    cuisines
    .value_counts()
    .head(10)
)


# Calculate and display city-specific KPIs

print("\nCITY KPIs\n")

kpis = get_city_kpis(
    df,
    "Lucknow"
)

for key, value in kpis.items():
    print(
        f"{key}: {value}"
    )
    
# Get and display top cuisines in the city  
  
    
print("\nTOP CUISINES\n")

top_cuisines = get_top_cuisines(
    df,
    "Lucknow"
)

print(top_cuisines)


# Get and display top localities in the city


print("\nTOP LOCALITIES\n")

top_localities = get_top_localities(
    df,
    "Lucknow"
)

print(top_localities)


# Analyze and display average cost for top localities in the city


print("\nLOCALITY COST ANALYSIS\n")

locality_costs = (
    get_locality_cost_analysis(
        df,
        "Lucknow"
    )
)

print(
    locality_costs.head(10)
)


# Analyze and display highest rated areas in the city


print("\nHIGHEST RATED AREAS\n")

highest_rated = (
    get_highest_rated_areas(
        df,
        "Lucknow"
    )
)

print(highest_rated)



# Analyze and display hidden gems in the city

print("\nHIDDEN GEMS\n")

hidden_gems = get_hidden_gems(
    df,
    "Lucknow"
)

print(hidden_gems.head(10))