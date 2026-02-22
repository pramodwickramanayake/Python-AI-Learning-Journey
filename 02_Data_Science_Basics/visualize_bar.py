import pandas as pd
import matplotlib.pyplot as plt
import os

# Getting the current directory to avoid 'File Not Found' errors
CURRENT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(CURRENT_DIR, 'data.csv')

def create_bar_chart():
    # Load my study data
    if not os.path.exists(FILE_PATH):
        print("Wait, I can't find data.csv in this folder!")
        return

    df = pd.read_csv(FILE_PATH)

    # Setting up the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Day'], df['Knowledge_Gain'], color='lightgreen', edgecolor='darkgreen')

    # Adding labels so it's easy to read
    plt.title('Daily Progress - Bar Chart View', fontsize=14)
    plt.xlabel('Day')
    plt.ylabel('Knowledge Gain (%)')

    # Saving the output for my GitHub README
    plt.savefig('learning_bar_chart.png')
    print("Nice! Your bar chart is saved as learning_bar_chart.png")
    
    plt.show()

if __name__ == "__main__":
    create_bar_chart()