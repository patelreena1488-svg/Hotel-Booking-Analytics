
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

file_path = (
    project_folder
    / "Dataset"
    / "cleaned_hotel_bookings.csv"
)

df = pd.read_csv(file_path)

print("CLEANED DATA VALIDATION")
print("=" * 40)

print("Rows and Columns:", df.shape)

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nMissing Values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nQuality Flags:")
print("Zero Guests:", df["zero_guest_flag"].sum())
print("Zero Nights:", df["zero_night_flag"].sum())
print("Negative ADR:", df["negative_adr_flag"].sum())
print("Extreme ADR:", df["extreme_adr_flag"].sum())

print("\nFirst 5 Records:")
print(df.head())

print("\nVALIDATION COMPLETED")
