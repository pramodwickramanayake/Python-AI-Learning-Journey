import pandas as pd
import os

# Set the file path relative to the script location
# This ensures it runs correctly on any machine
BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, 'data.csv')

def clean_my_data():
    """Simple script to handle missing values in the learning log."""
    
    if not os.path.exists(CSV_PATH):
        print(f"Error: Could not find {CSV_PATH}. Check your folder structure.")
        return

    # Load the dataset
    df = pd.read_csv(CSV_PATH)
    
    print("Checking for missing data points...")
    print(df.isnull().sum())

    # Filling missing Knowledge_Gain values with the mean
    # Sometimes I miss a day, so this keeps the trends accurate
    if 'Knowledge_Gain' in df.columns:
        avg_gain = df['Knowledge_Gain'].mean()
        df['Knowledge_Gain'] = df['Knowledge_Gain'].fillna(avg_gain)
        print(f"\nMissing values filled with average: {avg_gain:.2f}")

    # Displaying a quick preview of the cleaned data
    print("\n--- Cleaned Data Preview ---")
    print(df.head())

if __name__ == "__main__":
    clean_my_data()