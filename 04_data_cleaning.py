
import pandas as pd
from pathlib import Path

# Project folders
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "Dataset" / "hotel_bookings.csv"
output_file = project_folder / "Dataset" / "cleaned_hotel_bookings.csv"

# Load original dataset
df = pd.read_csv(input_file)

print("DATA CLEANING STARTED")
print("Original rows:", len(df))

# 1. Remove exact duplicate records
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates().copy()

# 2. Handle missing values
df["children"] = df["children"].fillna(0)
df["country"] = df["country"].fillna("Unknown")

# Keep missing agent and company values as blank.
# These may represent bookings without an agent/company.

# 3. Create quality flags
df["total_guests"] = (
    df["adults"] + df["children"] + df["babies"]
)

df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

df["zero_guest_flag"] = df["total_guests"] == 0
df["zero_night_flag"] = df["total_nights"] == 0
df["negative_adr_flag"] = df["adr"] < 0
df["extreme_adr_flag"] = df["adr"] > 1000

# 4. Save cleaned dataset
df.to_csv(output_file, index=False)

# 5. Print cleaning summary
print("\nDATA CLEANING SUMMARY")
print("------------------------------")
print("Duplicates removed:", duplicates_removed)
print("Remaining rows:", len(df))
print("Remaining columns:", len(df.columns))
print("Missing children:", df["children"].isnull().sum())
print("Missing country:", df["country"].isnull().sum())
print("Missing agent:", df["agent"].isnull().sum())
print("Missing company:", df["company"].isnull().sum())

print("\nQuality flags:")
print("Zero guests:", df["zero_guest_flag"].sum())
print("Zero nights:", df["zero_night_flag"].sum())
print("Negative ADR:", df["negative_adr_flag"].sum())
print("Extreme ADR:", df["extreme_adr_flag"].sum())

print("\nCleaned file saved at:")
print(output_file)

print("\nDATA CLEANING COMPLETED")
