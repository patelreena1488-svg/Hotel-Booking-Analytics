
import pandas as pd
from pathlib import Path

file_path = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "hotel_bookings.csv"
)

df = pd.read_csv(file_path)

# Calculate total guests and nights
df["total_guests"] = (
    df["adults"] +
    df["children"].fillna(0) +
    df["babies"]
)

df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

columns = [
    "hotel",
    "is_canceled",
    "adults",
    "children",
    "babies",
    "total_guests",
    "total_nights",
    "adr",
    "reservation_status"
]

print("\n1. ZERO-GUEST BOOKINGS")
print(df.loc[df["total_guests"] == 0, columns].head(10))

print("\n2. ZERO-NIGHT BOOKINGS")
print(df.loc[df["total_nights"] == 0, columns].head(10))

print("\n3. NEGATIVE ADR RECORD")
print(df.loc[df["adr"] < 0, columns])

print("\n4. TOP 10 HIGHEST ADR RECORDS")
print(
    df.nlargest(10, "adr")[columns]
)

print("\nANOMALY INSPECTION COMPLETED")
