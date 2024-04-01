import numpy as np
from scipy.special import gamma


# function to calculate t-distribution
def t_distribution_pdf(x, nu):
    coeff = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2))
    density = coeff * (1 + x**2 / nu)**(-0.5 * (nu + 1))
    return density

# function to calculate mean
def calculate_mean(data):
    total_sum = 0
    for i in range(0, len(data)):
        total_sum = total_sum + data[i]
    mean = total_sum / len(data)
    return mean

# function to calculate standard deviation
def calculate_std_dev(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    std_dev = variance ** 0.5
    return std_dev

# function to compute t0
def compute_t0(sample_mean, population_mean, sample_std_dev, sample_size):
    se = sample_std_dev / (sample_size ** 0.5)
    t0 = (sample_mean - population_mean) / se
    return t0

# function to find t*
def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):
    x = np.linspace(x_start, x_end, num_points)
    y = t_distribution_pdf(x, nu)
    cdf = np.cumsum(y) * (x[1] - x[0])

    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]

# function to determine significance level
def determine_significance_level(t0, t_star):
    # if t0 is between -t* and t*, we fail to reject the null hypothesis
    if -t_star < t0 < t_star:
        print("true")
        return True
    else:
        print("False")
        return False

#data
#scores from the new teaching technique
sample_data = [92.64, 79.00, 84.79, 97.41, 93.68, 65.23, 84.50, 73.49, 73.97, 79.11]  
national_average = 75

#Calculate mean and standard deviation
sample_mean = calculate_mean(sample_data)
sample_std_dev = calculate_std_dev(sample_data)

# find t0
sample_size = len(sample_data)
t0 = compute_t0(sample_mean, national_average, sample_std_dev, sample_size)

# Find critical (t*)
t_star = find_t_star(0.95, sample_size - 1)

# Determine significance level
significance_level = determine_significance_level(t0, t_star)

# Output results
print(f"Mean: {sample_mean}")
print(f"Standard Dev: {sample_std_dev}")
print(f"t0: {t0}")
print(f"(t*): {t_star}")
print(f"Is the result significant? {significance_level}")