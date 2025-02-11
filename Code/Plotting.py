import numpy as np
import matplotlib.pyplot as plt
from Getting_Data import get_data
from Data_Scaling_and_Experimentation import test_function

# Fetch and process data
data = test_function(get_data())

# Compute histogram properties
mean = np.mean(data)
std = np.std(data)/2

# Create histogram with normalisation and borders
bin_count = 50
hist_data, bin_edges, _ = plt.hist(data, bins=bin_count, color='blue', alpha=0.7, density=True, edgecolor='black', label='Histogram')

# Generate normal distribution values
x = np.linspace(min(data), max(data), 500)
normal_dist = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)

# Plot the normal distribution
plt.plot(x, normal_dist, color='red', label='Normal Distribution')

# Add labels, legend, and title
plt.xlabel('Returns: Conjecture 1')
plt.ylabel('Density')
plt.title(f'Normalised Histogram with Normal Distribution (Bins: {bin_count})')
plt.legend()

# Show the plot
plt.show()
