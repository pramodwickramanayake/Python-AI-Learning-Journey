import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('data.csv')

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(df['Day'], df['Knowledge_Gain'], marker='o', color='green', label='Knowledge Gain (%)')

# Add labels and title
plt.title('Daily Learning Progress Analysis', fontsize=14)
plt.xlabel('Day of Study')
plt.ylabel('Knowledge Gain Percentage')
plt.grid(True)
plt.legend()

# Save the plot as an image
plt.savefig('learning_graph.png')
print("Success: Graph save as learning_graph.png")

# Display the Chart
plt.show()