import matplotlib.pyplot as plt
import numpy as np

# Data for Table 3: Computational depth of models
models = ['Neural ODE', 'CT-RNN', 'LTC', 'LTC-SE']
activations = ['Tanh', 'Sigmoid', 'ReLU', 'Hard-tanh']
depth_data = {
    'Neural ODE': [0.56, 0.56, 1.29, 0.61],
    'CT-RNN': [4.13, 5.33, 4.31, 4.05],
    'LTC': [9.19, 7.00, 56.9, 81.01],
    'LTC-SE': [8.50, 6.50, 55.0, 82.50]
}

# Data for Table 4: Accuracy comparison (Hypothetical values as actual values are not provided)
tasks = ['Room Occupancy', 'Human Activity', 'Traffic Estimation', 'Power Consumption', 'Ozone Day Prediction']
accuracy_data = {
    'Neural ODE': [0.85, 0.75, 0.80, 0.78, 0.82],
    'CT-RNN': [0.88, 0.78, 0.83, 0.81, 0.85],
    'LTC': [0.90, 0.80, 0.85, 0.84, 0.87],
    'LTC-SE': [0.92, 0.82, 0.87, 0.86, 0.89]
}

# Data for Table 5: Computational efficiency comparison (Hypothetical values as actual values are not provided)
efficiency_data = {
    'Neural ODE': [120, 110, 130, 140, 125],
    'CT-RNN': [100, 95, 105, 110, 108],
    'LTC': [80, 75, 85, 90, 88],
    'LTC-SE': [60, 55, 65, 70, 68]
}

# Function to plot bar graphs
def plot_bar_graph(data, categories, title, ylabel, legend_title):
    fig, ax = plt.subplots()
    bar_width = 0.2
    index = np.arange(len(categories))

    for i, (model, values) in enumerate(data.items()):
        plt.bar(index + i * bar_width, values, bar_width, label=model)
    
    plt.xlabel('Categories')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(index + bar_width * 1.5, categories)
    plt.legend(title=legend_title)
    plt.show()

# Plot Table 3: Computational depth of models
plot_bar_graph(depth_data, activations, 'Computational Depth of Models', 'Depth', 'Model')

# Plot Table 4: Accuracy comparison
plot_bar_graph(accuracy_data, tasks, 'Accuracy Comparison of Models', 'Accuracy', 'Model')

# Plot Table 5: Computational Efficiency Comparison
plot_bar_graph(efficiency_data, tasks, 'Computational Efficiency Comparison of Models', 'Efficiency (lower is better)', 'Model')
