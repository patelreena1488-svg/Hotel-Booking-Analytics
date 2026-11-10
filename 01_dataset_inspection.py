
import pandas as pd
from pathlib import Path

# Locate the dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "hotel_bookings.csv"
)

# Load the dataset
df = pd.read_csv(file_path)

print("DATASET LOADED SUCCESSFULLY")
print("Total Rows and Columns:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()
