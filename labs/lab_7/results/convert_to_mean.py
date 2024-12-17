import os
import pandas as pd

# Directory containing CSV files
directory = './'

# Initialize a list to store means
means = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Check if the file is a CSV
        filepath = os.path.join(directory, filename)
        try:
            # Read the CSV file
            df = pd.read_csv(filepath, delimiter=';')

            means.append((filename, df.FullValType.mean(), df.LevensteinValType.mean()))
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

# Print the means
for file, mean_full, mean_lev in means:
    print(f"File: {file}, Mean_full: {mean_full}, Mean_lev: {mean_lev}")
