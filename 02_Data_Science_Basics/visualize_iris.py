import pandas as pd
import matplotlib.pyplot as plt
import os

# Setting up paths for script portability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'iris_data.csv')

def analyze_iris_features():
    """
    Analyzes the Iris dataset by plotting Sepal length vs width.
    This is a classic data science entry-level project.
    """
    
    # Check if the dataset exists
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Please add the dataset first.")
        return

    # Load the professional Iris dataset
    df = pd.read_csv(DATA_FILE)

    plt.figure(figsize=(10, 6))

    # Define unique species and colors for visualization
    species_list = df['species'].unique()
    colors = ['#FF5733', '#33FF57', '#3357FF'] # Distinct professional colors

    # Plotting each species with a different color
    for i, species in enumerate(species_list):
        subset = df[df['species'] == species]
        plt.scatter(subset['sepal_length'], 
                    subset['sepal_width'], 
                    label=species, 
                    s=100, 
                    alpha=0.7, 
                    edgecolors='k', 
                    color=colors[i])

    # Adding professional labels and styling
    plt.title('Iris Flower Analysis: Sepal Dimensions', fontsize=16, fontweight='bold')
    plt.xlabel('Sepal Length (cm)', fontsize=12)
    plt.ylabel('Sepal Width (cm)', fontsize=12)
    plt.legend(title='Species')
    plt.grid(True, linestyle='--', alpha=0.5)

    # Save the professional visualization
    save_path = os.path.join(BASE_DIR, 'iris_scatter_plot.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    print(f"✅ Success! Professional plot saved at: {save_path}")
    plt.show()

if __name__ == "__main__":
    analyze_iris_features()