import matplotlib.pyplot as plt
import numpy as np

# Data from the figures with updated values and task names
# Memory usage comparison for human activity recognition task using smart phones sensor data (Figure 2)
fig2 = {
    "CNN": [1000, 900, 850],
    "LSTM": [640, 600, 560],
    "LTC": [280, 260, 250],
    "LTC-SE": [250, 230, 220]
}

# Memory usage comparison for language modeling task (Figure 3)
fig3 = {
    "CNN": [480, 520, 580],
    "LSTM": [720, 800, 860],
    "LTC": [420, 460, 500],
    "LTC-SE": [380, 420, 480]
}

# Memory usage comparison for room occupancy task (Figure 4)
fig4 = {
    "CNN": [9.6, 9.7, 9.8],
    "LSTM": [8.6, 8.7, 8.9],
    "LTC": [3.8, 3.9, 4],
    "LTC-SE": [3.9, 3.9, 4]
}

# Memory usage comparison for time series prediction task (Figure 5)
fig5 = {
    "CNN": [700, 600, 550],
    "LSTM": [800, 900, 1000],
    "LTC": [350, 400, 450],
    "LTC-SE": [300, 350, 400]
}

# X-axis labels
labels = ["Feature Engineering", "Model Training", "Model Evaluation"]

# Plotting function
def plot_memory_usage(data, title, filename):
    fig, ax = plt.subplots()
    
    for model, values in data.items():
        ax.plot(labels, values, marker='o', label=model)
    
    ax.set_xlabel('Sub-Tasks')
    ax.set_ylabel('Memory Usage (MB)')
    ax.set_title(title)
    ax.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Plotting the data from figures
plot_memory_usage(fig2, "Memory Usage Comparison for Human Activity Recognition Task", "fig2_memory_usage_updated.png")
plot_memory_usage(fig3, "Memory Usage Comparison for Language Modeling Task", "fig3_memory_usage_updated.png")
plot_memory_usage(fig4, "Memory Usage Comparison for Room Occupancy Task", "fig4_memory_usage_updated.png")
plot_memory_usage(fig5, "Memory Usage Comparison for Time Series Prediction Task", "fig5_memory_usage_updated.png")
