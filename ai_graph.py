import numpy as np
import matplotlib.pyplot as plt

def plot_learning_progress():
    # 1. Define data points using NumPy arrays
    days = np.array([1, 2, 3, 4, 5, 6, 7])
    progress = np.array([10, 20, 30, 40, 55, 85, 100])

    # 2. Configure the plot style and color
    plt.plot(days, progress, marker='o', color='green', label='My Progress')

    # 3. Set labels for better readability
    plt.title("Software Engineering Learning Progress")
    plt.xlabel("Days")
    plt.ylabel("Knowledge Percentage (%)")

    # 4. Add a grid and legend for clarity
    plt.grid(True)
    plt.legend()

    # 5. Render the final graph
    plt.show()

    # run the function
if __name__ == "__main__":
    plot_learning_progress()