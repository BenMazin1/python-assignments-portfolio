import matplotlib.pyplot as plt
import random

# Function to check whether point (x, y) is inside
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
    
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)

    return A == A1 + A2 + A3

# Vertices of the triangle
vertices = [(0, 0), (1, 0), (0.5, 0.866)]

# ask the user for a seed point
while True:
    try:
        seed_x = float(input("Enter the x-coordinate of the seed point: "))
        seed_y = float(input("Enter the y-coordinate of the seed point: "))
        if isInside(0, 0, 1, 0, 0.5, 0.866, seed_x, seed_y):
            print("Valid seed point entered.")
            break
        else:
            print("The point is not inside the triangle. Please try again.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Start point
seed = (seed_x, seed_y)

# Initialize a list to store your points 
points = [seed]

# ask the user for the number of steps
while True:
    try:
        num_steps = int(input("Enter the number of steps: "))
        if num_steps > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Chaos Game algorithm
for _ in range(num_steps):
    # Roll the die
    roll = random.randint(0, 2)
    
    # Current seed point
    current_x, current_y = points[-1]

    # Vertex chosen 
    vertex_x, vertex_y = vertices[roll]

    # point is halfway between current point and chosen vertex
    new_x = (current_x + vertex_x) / 2
    new_y = (current_y + vertex_y) / 2

    # new point to the list
    points.append((new_x, new_y))

# Plot
x_vals, y_vals = zip(*points[12:])
plt.scatter(x_vals, y_vals, s=1)    # s=1 sets the size of the points
plt.show()






