import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns when printing a DataFrame

# ============== LOAD DATASET ==================
df = pd.read_csv("data/mushrooms.csv")
print("✅ Load the dataset successfully!")
print()

# ======== BASIC DATASET INFORMATION ===========
rows, columns = df.shape
print(f"📊 Dataset size: {rows} rows x {columns} columns")

print("📋 Column names:")
for i, column in enumerate(df.columns, 1):
    print(f"   {i}. {column}")

print('-' * 50)
print("Preview the dataset:")
print('-' * 50)
print("⬇️  Top 5 rows:")
print(df.head(5))
print("⬆️  Last 5 rows:")
print(df.tail(5))

print("-" * 50)
print("Data Types and Non-Null Counts")
print("-" * 50)
print(df.info())

print("-" * 50)
print("Statistical Summary (for numerical columns)")
print("-" * 50)
print(df.describe())

print("-" * 50)
print("Missing Values Check")
print("-" * 50)
print("Number of missing values per column")
missing_values = df.isnull().sum()
print(missing_values)

if missing_values.sum() == 0:
    print("✅  Great! There is no missing values found in the dataset.")
else:
    print("⚠️  Some columns have missing values. We may need to handle them later.")

# ============ END OF PROGRAM ================  
