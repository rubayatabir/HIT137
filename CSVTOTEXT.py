import pandas as pd
import os

# Path to the directory where CSVs are stored
extract_path = '/Users/rubayatabeer/Downloads/Assignment'

# List the CSV files
csv_paths = [os.path.join(extract_path, file) for file in os.listdir(extract_path) if file.endswith('.csv')]

# Inspect the first few rows of each CSV to find the 'text' column
csv_data = {}
for path in csv_paths:
    print(f"Inspecting {path}")
    print(pd.read_csv(path).head())  # View first few rows
