# Hotel Booking Demand Analysis

### A Data Analytics Portfolio Project | Python & Power BI

## Project Overview

For this project, I worked with the Hotel Booking Demand dataset to explore how customers make hotel reservations and what factors are related to booking cancellations.

I wanted to understand the booking patterns of City Hotels and Resort Hotels, explore customer preferences, and turn the data into insights that could be useful for hotel management.

I used Python for data cleaning and analysis, and Power BI to build an interactive dashboard.

## What I Wanted to Explore

While working on this project, I focused on a few practical business questions:

- How many bookings do the hotels receive?
- Which type of hotel receives more bookings?
- How often do customers cancel their reservations?
- How do booking patterns change from month to month?
- Which market segments contribute the most bookings?
- How do hotel prices vary between City and Resort Hotels?

## Dataset

I used the Hotel Booking Demand dataset available on Kaggle.

The original dataset contained 119,390 records and 32 columns.

After cleaning and removing duplicate records, the final dataset contained 87,396 records and 38 columns.

## My Approach

### 1. Data Inspection

I started by exploring the dataset to understand its structure, data types, missing values, and overall quality.

### 2. Data Cleaning

Using Python and Pandas, I:

- Removed duplicate records.
- Handled missing values where appropriate.
- Checked unusual booking records.
- Identified zero-guest and zero-night bookings.
- Flagged negative and unusually high ADR values.
- Created additional columns to support analysis.

I kept unusual records where appropriate and used flags to identify them instead of automatically deleting them.

### 3. Exploratory Data Analysis

I analysed booking counts, cancellation patterns, average ADR, lead time, hotel performance, and monthly booking trends.

### 4. Dashboard Development

I used Power BI to create an interactive dashboard with KPI cards, filters, and charts to make the results easier to explore.
### Dashboard Preview

![Hotel Booking Dashboard](../dashboard_preview.png)

## Key Findings

Here are some of the main numbers from my analysis:

| Metric                |     Result |
| --------------------- | ---------: |
| Total Bookings        |     87,396 |
| Canceled Bookings     |     24,025 |
| Cancellation Rate     |     27.49% |
| Average ADR           |     106.34 |
| Average Lead Time     | 79.89 days |
| City Hotel Bookings   |     53,428 |
| Resort Hotel Bookings |     33,968 |

City Hotels received more bookings than Resort Hotels. The cancellation rate was also higher for City Hotels.

## Tools I Used

- Python – Data analysis and cleaning
- Pandas – Data manipulation
- Matplotlib – Data visualization
- Power BI – Interactive dashboard
- Visual Studio Code – Python development

## Project Structure

```text
Hotel_Booking_Analytics/
│
├── Dataset/
│   ├── hotel_bookings.csv
│   └── cleaned_hotel_bookings.csv
│
├── Python_Analysis/
│   ├── README.md
│   ├── 01_dataset_inspection.py
│   ├── 02_data_quality_check.py
│   ├── 03_anomaly_inspection.py
│   ├── 04_data_cleaning.py
│   ├── 05_validate_cleaned_data.py
│   ├── 06_eda_analysis.py
│   ├── 07_eda_visualizations.py
│   └── Charts/
│       ├── 01_hotel_booking_count.png
│       ├── 02_cancellation_rate.png
│       └── 03_monthly_booking_trend.png
│
├── dashboard_preview.png
└── Hotel_Booking_Analytics_Dashboard.pbix
```

## What I Learned

Working on this project helped me practise the complete data analytics process, from inspecting and cleaning raw data to exploring patterns and presenting findings through a Power BI dashboard.

It also helped me understand how data analysis can support better business decisions in the hospitality industry.

---

