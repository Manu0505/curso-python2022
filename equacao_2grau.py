from cmath import sqrt
import math

print ('equação do 2º grau \nax² + bx - c')

a = float(input('digite o valor de a:  '))
b = float(input('digite o valor de b:  '))
c = float(input('digite o valor de c:  '))

delta = b ** 2 - 4 * a * c
x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b - sqrt(delta)) / 2 * a

