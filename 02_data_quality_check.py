
import pandas as pd
from pathlib import Path

# Load dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "hotel_bookings.csv"
)

df = pd.read_csv(file_path)

print("DATA QUALITY CHECK")
print("=" * 40)

# Duplicate records
print("Duplicate Rows:", df.duplicated().sum())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Guest count check
df["total_guests"] = (
    df["adults"] + df["children"].fillna(0) + df["babies"]
)

print("\nBookings with zero guests:",
      (df["total_guests"] == 0).sum())

# Stay duration check
df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

print("Bookings with zero nights:",
      (df["total_nights"] == 0).sum())

# ADR check
print("Negative ADR:", (df["adr"] < 0).sum())
print("Maximum ADR:", df["adr"].max())

print("\nDATA QUALITY CHECK COMPLETED")
