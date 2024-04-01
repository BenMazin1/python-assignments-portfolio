import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Function to compute normal density
def normal_density(mean, std_dev, x):
    # Computes the normal density for a given x, mean, and standard deviation.

    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev**2))

# Function to plot the normal density for different means and variances
def plot_normal_density(means, std_devs, x_range):
    x_values = np.linspace(x_range[0], x_range[1], 1000)
    for mean, std_dev in zip(means, std_devs):
        y_values = [normal_density(mean, std_dev, x) for x in x_values]
        plt.plot(x_values, y_values, label=f'Mean: {mean}, Std. Dev.: {std_dev}')
    plt.legend()
    plt.show()

# Function for numerical integration
def integrate_normal_density(mean, std_dev, a, b):
    result, _ = quad(normal_density, a, b, args=(mean, std_dev))
    return result

# Plotting the normal density for different means and variances
#plot_normal_density([0, 5, 12, 14], [1, 2, 100, 0.5], [-10, 15, 0.01, 30])


# Calculating the probability for a given range
mean_height = 171  # Mean height in cm
variance_height = 7.12  # Given variance in height
std_dev_height = np.sqrt(variance_height)  # Standard deviation is the square root of variance
plot_normal_density([mean_height], [std_dev_height], [150, 200])
# Calculating the probability for a given range using the standard deviation
probability = integrate_normal_density(mean_height, std_dev_height, 162, 190)
print(f"Probability that a randomly chosen man has a height between 162cm and 190cm: {probability:.4f}")



