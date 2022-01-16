import math

def delta(a, b, c):
    x = math.pow (b, 2) - 4 * a * c
    return x

def bhaskara1 (a, b, d):
    x1 = (-b + math.sqrt(d)) / 2 * a
    return x1
    
def bhaskara2 (a, b, d):
    x2 = (-b - math.sqrt(d)) / 2 * a
    return x2

