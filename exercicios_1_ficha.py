#1º exercício

print('1. Faça um Programa que peça dois números e imprima a soma.')
a1 = float(input('digite um número:  '))
a2 = float(input('digite outro número:  '))
soma = a2+a1
print(f'O valor da soma de {a1} e {a2} é igual a {soma}')
print( )

#2º exercício

print('2. Faça um Programa que peça as 4 notas bimestrais e mostre a média.')
n1 = float(input('digite a nota do 1º bimestre:  '))
n2 = float(input('digite a nota do 2º bimestre:  '))
n3 = float(input('digite a nota do 3º bimestre:  '))
n4 = float(input('digite a nota do 4º bimestre:  '))
média = (n4+n2+n3+n1)/4
print(f"O valor da média anual é de {média}")
print( )

#3º exercício

print('3. Faça um Programa que converta metros para centímetros')
m1 = float(input('digite a medida em metros:  '))
c = m1 * 100
print(f'o valor de {m1} metros convertido para centímetros é de {c}cm')
print( )

#4º exercício

print('4. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área')
r = float(input('digite a medida do raio do círculo:  '))
area = 3.14 * r ** 2
print(f"O valor da área de um círculo de raio {r} é de {area}")
print( )

#5º exercício

print('5. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.')
l = float(input('digite a medida do lado do quadrado:  '))
square = l ** 2
square_2 = square * 2
print(f"O valor da área do quadrado é de {square}, e")
print(f"o valor do dobro da área do mesmo quadrado é de {square_2}")
print( )

#6º exercício

print('6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.')
d = float(input('Quanto você ganha por hora? R:  '))
h = float(input('Quantas horas você trabalha por mês? R:  '))
salário = d * h
print(f"Trabalhando {h} horas por mês e ganhando {d} por cada uma delas, seu salário será de R${salário}")
print( )

#7º exercício

print('7. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.')
f = int(input('Digite a temperatura em graus Fahrenheit:  '))
c = 5 * ((f-32) / 9)
print(f"{f} graus Fahrenheit é igual a {c} graus Celcius")
print( )

#8° exercício

print('8. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:')
print('- o produto do dobro do primeiro com metade do segundo .')
print('- soma do triplo do primeiro com o terceiro.')
print('- o terceiro elevado ao cubo.')

i1 = int(input('Digite um número inteiro:  '))
i2 = int(input('Digite outro número inteiro:  '))
real = float(input('Digite um número real:  '))

c1 = i1 * (i2/2)
c2 = (3*i1) + real
c3 = real ** 3

print(f'O produto do dobro do primeiro com metade do segundo é igual a {c1}.')
print(f'A soma do triplo do primeiro com o terceiro é igual a {c2}.')
print(f'O terceiro elevado ao cubo é igual a {c3}.')
print( )

#9º exercício

print('9. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal.')
      #(72.7*altura) - 58')
h = float(input('Insira o valor da sua altura, em metros:  '))
peso_ideal = (72.7 * h) - 58
print(f'o seu peso ideal é igual a {peso_ideal}.')
print( )

#10º exercícios

print('10. Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal com base em seu gênero.')
#-Para homens: (72.7*h) - 58
#-Para mulheres: (62.1*h) - 44.7
h1 = float(input('Insira o valor da sua altura, em metros:  '))
men = (72.7 * h1) - 58
w = (62.1 * h1) - 44.7
print(f'Se você for um homem, seu peso ideal é igual a {men}kg.')
print(f'ou, se você for uma mulher, seu peso ideal é igual a {w}kg.')
print( )