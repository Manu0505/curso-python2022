# 1. Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('digite um número:  '))
n2 = float(input('digite outro número:  '))

if n1 > n2:
    print(f'{n1} é o maior deles')

else:
    print(f'{n2} é o maior deles')

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

v = float(input('digite qualquer valor:  '))

if v >= 0:
    print(f'{v} é positivo')

else:
    print(f'{v} é negativo')

# 3. Faça um programa pra calcular o IMC e informar qual categoria pertence o IMC da pessoa.
# É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
# Entre 17 e 18,49	Abaixo do peso
# Entre 18,50 e 24,99	Peso normal
# Entre 25 e 29,99	Acima do peso
# Entre 30 e 34,99	Obesidade I

kg = float(input('digite seu peso (em kg):  '))
h = float(input('digite sua altura (em metros):  '))

imc = kg / h ** 2

print(f'seu imc é de {imc}')

if 17 <= imc <= 18.49:
    print(f'seu IMC é de {imc}. Isso significa que você está abaixo do peso.')

if 18.50 <= imc <= 24.99:
    print(f'seu IMC é de {imc}. Isso significa que você está com peso normal.')

if 25 <= imc <= 29.99:
    print(f'seu IMC é de {imc}. Isso significa que você está acima do peso.')

    if 30 <= imc <= 34.99:
        print(
            f'seu IMC é de {imc}. Isso significa que você está com Obesidade I.')

# 4. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

l = input('digite F ou M:  ')

if l == 'f' or 'F':
    print('F - Feminino')

elif l == 'm' or 'M':
    print('M - Masculino')

else:
    print('Sexo inválido')

    # 5. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

a = str(input('insira uma letra:  '))

if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
    print(f'{a} é uma vogal')

else:
    print(f'{a} é uma consoante')

    # 6. Faça um programa para a leitura de duas notas parciais de um aluno. O
# programa deve calcular a média alcançada por aluno e apresentar:
# a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b. A mensagem "Reprovado", se a média for menor do que sete;
# c. A mensagem "Aprovado com Distinção", se a média for igual a dez.

x1 = float(input('insira sua primeira nota:  '))
x2 = float(input('insira sua segunda nota:  '))

media = (x1 + x2) / 2

if 7 <= media < 10:
    print(f'Sua média é de {media}. Você foi aprovado(a)!.')

if media < 7:
    print(f'Sua média é de {media}. Você foi reprovado(a). :(')

if media == 10:
    print(
        f'Sua média é de {media}. Parabéns, você foi aprovado(a) com distinção!.')

# 7. Faça um Programa que leia três números e mostre o maior deles

t1 = float(input('insira um número:  '))
t2 = float(input('insira um segundo número:  '))
t3 = float(input('insira um terceiro número:  '))

if t1 > t2 and t1 > t3:
    print(f'{t1} é o maior número dentre os digitados')

if t2 > t1 and t2 > t3:
    print(f'{t2} é o maior número dentre os digitados')

if t3 > t2 and t3 > t1:
    print(f'{t3} é o maior número dentre os digitados')

# 8. Faça um Programa que leia três números e mostre o maior e o menor deles.

y1 = float(input('insira um número:  '))
y2 = float(input('insira um segundo número:  '))
y3 = float(input('insira um terceiro número:  '))

if y1 > y2 and y1 > y3:
    print(f'{t1} é o maior número dentre os digitados')

if y2 > y1 and y2 > y3:
    print(f'{t2} é o maior número dentre os digitados')

if y3 > y2 and y3 > y1:
    print(f'{t3} é o maior número dentre os digitados')

if y1 < y2 and y1 < y3:
    print(f'{t1} é o menor número dentre os digitados')

if y2 < y1 and y2 < y3:
    print(f'{t2} é o menor número dentre os digitados')

if y3 < y2 and y3 < y1:
    print(f'{t3} é o menor número dentre os digitados')


# 9. Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('insira o preço do 1º produto:  '))
p2 = float(input('insira o preço do 2º produto:  '))
p3 = float(input('insira o preço do 3º produto:  '))

if p1 < p2 and p1 < p3:
    print(f'{t1} é o produto mais barato')

if p2 < p1 and p2 < p3:
    print(f'{t2} é o produto mais barato')

if p3 < p2 and p3 < p1:
    print(f'{t3} é o produto mais barato')

# 10.Faça um Programa que leia três números e mostre-os em ordem decrescente

d1 = float(input('insira o 1º número:  '))
d2 = float(input('insira o 2º número:  '))
d3 = float(input('insira o 3º número:  '))

if d1 > d2 > d3:
    print(f'em ordem decrescente: {d1}, {d2}, {d3}')

elif d1 > d3 > d2:
    print(f'em ordem decrescente: {d1}, {d3}, {d2}')

elif d2 > d1 > d3:
    print(f'em ordem decrescente: {d2}, {d1}, {d3}')

elif d2 > d3 > d1:
    print(f'em ordem decrescente: {d2}, {d3}, {d1}')

elif d3 > d2 > d1:
    print(f'em ordem decrescente: {d3}, {d2}, {d1}')

elif d3 > d1 > d2:
    print(f'em ordem decrescente: {d3}, {d1}, {d2}')


# 11. Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

t = input(
    'Em que turno você estuda? (M-matutino ou V-Vespertino ou N- Noturno)  R:  ')

if t == 'm':
    print('Bom Dia!')

elif t == 'v':
    print('Boa Tarde!')

elif t == 'n':
    print('Boa Noite!')

else:
    print('Valor Inválido!')

# 12.Faça um Programa que peça um número inteiro e determine se ele é par ou
# impar. Dica: utilize o operador módulo (resto da divisão - operador de módulo
# % - se x % 2 == 0 então é par).

i = int(input('insira um numero:  '))

if i % 2 == 0:
    print('o número inserido é par')

else:
    print('o número inserido é impar')

# 13.Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
# conceitos obedece à tabela abaixo:
# 9 10
#7.5 e 9
#6 e 7.5
# 4 e 6
# 4 e 0


g1 = float(input('insira a primeira nota:  '))
g2 = float(input('insira a segunda nota:  '))

med = (g1+g2) / 2

if 9 <= med <= 10:
    print ('Você recebeu um A')

elif 7.5 <= med < 9:
    print ('Você recebeu um B')

elif 6 <= med < 7.5:
    print ('Você recebeu um C')

elif 4 <= med < 6:
    print ('Você recebeu um D')

elif 4 <= med < 0:
    print ('Você recebeu um E')

# 14.Faça um Programa que leia um número e exiba o dia correspondente da
# semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
# valor inválido.

z = int(input('insira um numero correspondente ao dia da semana. (1-Domingo, 2- Segunda,(...) 7-Sábado):  '))

if z == 1:
    print(f'o número é correspondente ao Domingo')

elif z == 2:
    print(f'o número é correspondente à segunda')

elif z == 3:
    print(f'o número é correspondente à terça')

elif z == 4:
    print(f'o número é correspondente à quarta')

elif z == 5:
    print(f'o número é correspondente à quinta')

elif z == 6:
    print(f'o número é correspondente à sexta')

elif z == 7:
    print(f'o número é correspondente ao sábado')

else:
     print(f'valor invalido')



# 15.Faça um programa que permita o usuário escolher entre três opções de
# bebidas e mostre na tela a bebida escolhida:

j = int(input('escolha uma entre as seguintes bebidas:(1- água, 2- refrigerante, 3- vinho):  '))

if j == 1:
    print('a bebida escolhida foi água')

if j == 2:
    print('a bebida escolhida foi refrigerante')

if j == 3:
    print('a bebida escolhida foi vinho')

