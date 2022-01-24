import math

def delta(a, b, c):
    delta = math.pow (b, 2) - 4 * a * c
    return delta

def x1 (a, b, delta):
    x1 = (-b + math.sqrt(delta)) / 2 * a
    return x1
    
def x2 (a, b, delta):
    x2 = (-b - math.sqrt(delta)) / 2 * a
    return x2

