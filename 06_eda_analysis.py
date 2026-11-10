
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Dataset" / "cleaned_hotel_bookings.csv"

df = pd.read_csv(file_path)

print("EXPLORATORY DATA ANALYSIS")
print("=" * 45)

total_bookings = len(df)
canceled_bookings = df["is_canceled"].sum()

cancellation_rate = (
    canceled_bookings / total_bookings
) * 100

average_adr = df["adr"].mean()
average_lead_time = df["lead_time"].mean()

print("\nKEY BUSINESS KPIs")
print("-" * 45)

print("Total Bookings:", total_bookings)
print("Canceled Bookings:", canceled_bookings)
print("Cancellation Rate:", round(cancellation_rate, 2), "%")
print("Average ADR:", round(average_adr, 2))
print("Average Lead Time:", round(average_lead_time, 2), "days")

print("\nHOTEL-WISE PERFORMANCE")
print("-" * 45)

hotel_analysis = df.groupby("hotel").agg(
    total_bookings=("hotel", "count"),
    canceled_bookings=("is_canceled", "sum"),
    average_adr=("adr", "mean"),
    average_lead_time=("lead_time", "mean")
)

hotel_analysis["cancellation_rate"] = (
    hotel_analysis["canceled_bookings"] /
    hotel_analysis["total_bookings"] * 100
)

print(hotel_analysis.round(2))

print("\nEDA ANALYSIS COMPLETED")
