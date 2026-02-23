import pandas as pd
import matplotlib.pyplot as plt
import os

# Setting up directory paths to ensure the script runs anywhere
# This helps other developers who might download your project
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, 'data_topics.csv')

def generate_progress_pie_chart():
    """Reads topic-wise data and generates a distribution pie chart."""
    
    # Safety check for the dataset
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Please ensure the CSV exists.")
        return

    # Load the topic-based dataset
    df = pd.read_csv(DATA_FILE)

    # Plotting the pie chart
    plt.figure(figsize=(8, 8))
    
    # Defining custom colors for a modern look
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
    
    plt.pie(df['Knowledge_Gain'], 
            labels=df['Topic'], 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=colors,
            wedgeprops={'edgecolor': 'white'}) # Adds a clean white border
    
    plt.title('Learning Progress Distribution by Topic', fontsize=14, pad=20)
    
    # Save the output for documentation
    plt.savefig('learning_pie_chart.png', dpi=300, bbox_inches='tight')
    print("✅ Success! Chart saved as learning_pie_chart.png")
    
    plt.show()

if __name__ == "__main__":
    generate_progress_pie_chart()