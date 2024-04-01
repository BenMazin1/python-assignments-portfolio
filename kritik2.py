import math

def bisection(f, a, b, tol=1e-9):
    if f(a) * f(b) > 0:
        return "No root generated"
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

def one(x):
    if x <= 0:
        return float('inf')
    return math.exp(x) + math.log(x)

def two(x):
    return math.atan(x) - x ** 2

def three(x):
    if x <= 0:
        return float('inf')
    return math.sin(x) / math.log(x)

def four(x):
    return math.log(math.cos(x))

print(bisection(one, 0.0000000001, 1))
print(bisection(two, 0, 2))
print(bisection(three, 3, 4))
print(bisection(four, 5, 7))