import formulas
import math


print ('equação do 2º grau \nax² + bx - c')

a = float(input('digite o valor de a:  '))
b = float(input('digite o valor de b:  '))
c = float(input('digite o valor de c:  '))


print (f'a equação a ser resolvida é: {a}x² + {b}x - {c}')

delta = formulas.delta(a, b, c)
print (delta)
if delta >= 0:
    x1 = formulas.bhaskara1(a, b, delta)
    x2 = formulas.bhaskara2(a, b, delta)
    print (f'o valor das raízes da equação é de {x1} e {x2}')

else:
    print('não existem raízes dentro do conjunto dos números reais para esta equação')