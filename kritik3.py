import numpy as np
def one(x):
    return x**2
def two(x):
    return np.sin(x)
def three(x):
    return np.e**x

functions = [one, two, three]
cValues = [1, np.pi/4, 0]
eValues = [0.1, 0.05, 0.01] 
deltaX = 10**-8
for i in range(0, len(functions)):
    x1 = cValues[i]
    x2 = cValues[i]
    for p in range(0, 100):
        x1 -= 0.00001
        aprox = (functions[i](cValues[i])) + ((functions[i](x1 + deltaX) - functions[i](x1 - deltaX)) / (2*deltaX)) * (x1 - cValues[i])
        if abs(functions[i](x1) - aprox) <= eValues[i]:
            print(x1)
            break
    else:
        print("No x1")
    for p in range(0, 100):
        x2 += 0.00001
        aprox = (functions[i](cValues[i])) + ((functions[i](x2 + deltaX) - functions[i](x2 - deltaX)) / (2*deltaX)) * (x2 - cValues[i])
        if abs(functions[i](x2) - aprox) <= eValues[i]:
            print(x2)
            break
    else:
        print("No x2")




        