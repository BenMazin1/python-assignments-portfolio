import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, diff, sqrt, ln
import math

# exersice 1
# define function e^x
x, y = sp.symbols('x y')
f = sp.exp(x)*sp.sin(y) + y**3

# computer first partial derivative of f with respect to x and y
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

# print the results
print("exercise 1")
print("First partial derivative of f with respect to x: ", df_dx)
print("First partial derivative of f with respect to y: ", df_dy)

# exersice 2
# Define the symbols and function
x, y = symbols('x y')
g = x**2 * y + x * y**2

# Compute the gradient vector/first partial derivatives
grad_g = [diff(g, x), diff(g, y)]

# Compute the magnitude of the gradient vector
magnitude = sqrt(grad_g[0]**2 + grad_g[1]**2)

# Evaluate at the point (1, -1)
grad_g_at_point = [partial.evalf(subs={x: 1, y: -1}) for partial in grad_g]
magnitude_at_point = magnitude.evalf(subs={x: 1, y: -1})

# Print the results
print("exercise 2")
print("Magnitude of the gradient vector of g at point (1, -1): ", magnitude_at_point)

# exersice 3
# Define the function h(x, y)
h = ln(x**2 + y**2)

# Compute the second partial derivatives
d2h_dx2 = diff(h, x, x)
d2h_dy2 = diff(h, y, y)
d2h_dxdy = diff(h, x, y)

# Print the results
print("exercise 3")
print("Second partial derivative of h with respect to x: ", d2h_dx2)
print("Second partial derivative of h with respect to y: ", d2h_dy2)
print("Second partial derivative of h with respect to x and y: ", d2h_dxdy)

# exersice 4
# Define the function j(x, y)
x, y = sp.symbols('x y')
j = x**3 - 3*x*y + y**3

# Compute the gradient vector/first partial derivatives
j_func = sp.lambdify((x, y), j, 'numpy')
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)

# Plot the contour plot
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('contour_plot.png')

#exersice 5
# Define the function j(x, y)
x, y = sp.symbols('x y')
j = math.pi*y**3 - x*y
j_func = sp.lambdify((x, y), j, 'numpy')

# Compute the gradient vector/first partial derivatives
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)

# Plot the contour plot
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of pi*y**3 - x**y')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.savefig('contour_plot2.png')