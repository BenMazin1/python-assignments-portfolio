import matplotlib.pyplot as plt
import numpy as np

def gradient_descent(f, learning_rate, initial_point):
    def deriv(f, base_point):
       # estimate the derivative
        h = 10**(-5)  # A small step size for the finite difference method.
        return (f(base_point + h) - f(base_point - h)) / (2 * h)

    # Initialize lists to store the coordinates of each step.
    x_coords = [initial_point]
    y_coords = [f(initial_point)]

    # Gradient descent algorithm.
    for _ in range(1000):  # Set a limit to the number of iterations to prevent infinite loops.
        derivative = deriv(f, x_coords[-1])
        new_x = x_coords[-1] - learning_rate * derivative
        x_coords.append(new_x)
        y_coords.append(f(new_x))
        
        # Check if the absolute value of the derivative is small enough to stop.
        if abs(derivative) < 1e-9:
            break

    # Plot the function and the steps taken by gradient descent.
    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 10000)
    function_range = [f(i) for i in plot_range]
    plt.plot(plot_range, function_range, label="Function f(x)")
    plt.scatter(x_coords, y_coords, color='red', label="Gradient Descent Steps")
    plt.title("Gradient Descent Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()

    # Return the last position and function value, rounded to three decimal places.
    return round(x_coords[-1], 3), round(y_coords[-1], 3)

# Test examples
def example1(x):
    # A simple quadratic function
    return x**2

def example2(x):
    return -3*x**3 + 10*x**2 -5*x - 3

def example3(x):
    return np.exp(x) - 4 * x

def example4(x):
    if x > 0:
        return x**x
    elif x == 0:
        return 1
    else:
        return abs(x)**abs(x)

# Run the gradient descent algorithm on each example and print the results.
print("Example 1 :", gradient_descent(example1, learning_rate=0.1, initial_point=10))
print("Example 2 :", gradient_descent(example2, learning_rate=0.1, initial_point=2))
print("Example 3 :", gradient_descent(example3, learning_rate=0.1, initial_point=0))
print("Example 4 :", gradient_descent(example4, learning_rate=0.1, initial_point=1))








