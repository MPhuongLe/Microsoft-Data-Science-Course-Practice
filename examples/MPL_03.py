"""
Honey Production Trends — Variant Exercise 

Goal:
Analyze production trends over time and identify insights across years and states.

What you'll practice:
- Yearly aggregation (sum by year)
- Identifying extreme values (highest/lowest)
- Filtering based on multi-year conditions
- Grouping by state and computing multiple statistics
- Sorting to explore top/bottom ranked values
- Answering a real data question

Dataset required: honey.csv
"""

import pandas as pd
pd.options.display.float_format = "{:,.0f}".format

# ===================================
#              READ DATA 
# ===================================
data = pd.read_csv("data/honey.csv")
print("✅ Load data successfully!")
print(list(data.columns))

# ===================================
#               FILTER  
# ===================================
year_to_filter = 2010
print("-" * 50)
print(f"FILTER DATA BY YEAR {year_to_filter}")
print("-" * 50)
filtered_data = data[data["year"] == year_to_filter]
print(f"Found {len(filtered_data)} records")
print(filtered_data.head())

# ===================================
#    FILTER (MULTIPLE CONDITIONS) 
# ===================================

# Display records in 2010 that have total honey production value higher than average
print("-" * 50)
print(f"FILTER HIGH PRODUCTION RECORDS IN YEAR {year_to_filter}")
print("-" * 50)
mean_prod = filtered_data["totalprod"].mean()
print(f"High production records have the total production higher than mean of {mean_prod:,.3f} pounds")
high_prod_data = filtered_data[filtered_data["totalprod"] >= mean_prod]
print(f"Found {len(high_prod_data)} records")
print(high_prod_data.sort_values("totalprod", ascending=False))


# ===================================
#              AGGREGATION 
# ===================================
print("-" * 50)
print("YEARLY HONEY PRODUCTION (AGGREGATION)")
print("-" * 50)
yearly_prod = data.groupby("year")["totalprod"].sum()
print(f"Found {len(yearly_prod)} records")
# print(yearly_prod.head().apply(lambda x: f"{x:,.0f} pounds"))
print(yearly_prod.head())
print()

highest_prod_year = yearly_prod.idxmax()
print(f"Highest production year: {highest_prod_year} ({yearly_prod[highest_prod_year]} pounds)")

lowest_prod_year = yearly_prod.idxmin()
print(f"Lowest production year: {lowest_prod_year} ({yearly_prod[lowest_prod_year]} pounds)")

mean_yearly_prod = yearly_prod.mean()
print(f"Average yearly production: {mean_yearly_prod} pounds")

# ===================================
#              COUNT VALUES 
# ===================================

# Count how many records we have for each state
state_counts = data["state"].value_counts()
print(state_counts)

state = "OK"
filtered_by_state = data[data["state"] == "OK"]
print(f"State {state} only has {len(filtered_by_state)}")
print(filtered_by_state)

# ===================================
#            REAL QUESTION 
# ===================================

# Question: Which state had the highest honey production in 2012?
data_2012 = data[data["year"] == 2012]
max_prod_2012 = data_2012["totalprod"].max()
highest_list = list(data_2012[data_2012["totalprod"] == max_prod_2012]["state"])
print(f"Answer: {highest_list} ({max_prod_2012:,.0f} pounds)")

# Suggestion
max_prod_idx = data_2012["totalprod"].idxmax()
max_prod_state = data_2012.loc[max_prod_idx, "state"]
max_prod_amount = data_2012.loc[max_prod_idx, "totalprod"]
print(f"Answer: {max_prod_state} ({max_prod_amount:,.0f} pounds)")

# ======== END OF PROGRAM ==========