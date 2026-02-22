"""
Project: Real-World Data Analysis with Pandas
Author: Pramod Wickramanayake
Description: Demonstrating professional data manipulation, filtering, 
             and statistical analysis using Pandas. Essential for 
             Data Science and Freelancing.
"""

import pandas as pd
import os

# Configuration
FILE_NAME = 'data.csv'

def run_analysis():
    # 1. Check file
    if not os.path.exists(FILE_NAME):
        print(f"Error: {FILE_NAME} not found.")
        return

    # 2. Load and Show Data
    df = pd.read_csv(FILE_NAME)
    print("--- Dataset Summary ---")
    print(df.head())

    # 3. Filter Knowledge Gain > 50%
    top_days = df[df['Knowledge_Gain'] > 50]
    
    print("\n--- High Progress Days ---")
    print(top_days)

    # 4. Quick Average
    avg_hours = df['Study_Hours'].mean()
    print(f"\nAverage Study Time: {avg_hours} hours")

if __name__ == "__main__":
    run_analysis()