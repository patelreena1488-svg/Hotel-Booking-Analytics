import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned dataset
project_folder = Path(__file__).resolve().parent.parent

file_path = (
    project_folder / "Dataset" / "cleaned_hotel_bookings.csv"
)

df = pd.read_csv(file_path)

# Create charts folder
charts_folder = project_folder / "Python_Analysis" / "Charts"
charts_folder.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")