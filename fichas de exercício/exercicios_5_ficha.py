#1. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. 
# A função deve retornar um valor booleano.

def inteiro():
    n1 =  int(input('digite um numero inteiro:  '))
    if bool(n1 >= 0):
        print (True)

    elif bool(n1 < 0):
        print (False)
        return bool
inteiro()

#2. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. 
# A função deve retornar um valor booleano.

def par_impar():
    n1 =  int(input('digite um numero inteiro:  '))
    if bool(n1 % 2 == 0):
        print (True)

    elif bool(n1 % 2 != 0):
        print (False)
        return bool

par_impar()

#3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#fiz a concatenação pq não foi especificado se esses argumentos precisam ser números
a1 = input('digite algo:  ')
a2 = input('digite algo:  ')
a3 = input('digite algo:  ') 

def somar(a1, a2, a3):
    soma = a1 + a2 + a3
    print(soma)

somar(a1, a2, a3)

#4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
#  se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

n = int(input('digite um número:'))

def P_N(n):
    if n >= 0:
        print ('P')

    elif n < 0:
        print ('N')
    

P_N(n)

#5. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
# DICA(Converta o número usando str e função len)

def tam():
    num = int(input('informe um numero inteiro: '))
    tam = len(str(num))
    print(f'a quantidade de dígitos do número informado é {tam}.')

tam()

#6. Crie uma função que calcula o aumento do salário de um funcionário. A função deve receber a porcentagem de 
# aumento e o salário atual e retornar o no salário. O usuário deve informar o salário atual e a porcentagem de aumento.

def aumento():
    salario = float(input('informe seu salário atual: '))
    porcentagem = float(input('informe a porcentagem de aumento do salário (sem o símbolo %): '))

    pct = porcentagem / 100

    aumento = salario * pct

    novo_salario = salario + aumento

    print (f'Você recebeu um aumento de {aumento}, e seu novo salário será de {novo_salario}')

aumento()

#7. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (volume = (4/3)*pi*raio3).
raio = float(input('digite o raio da esfera: '))

def esfera (raio):
    volume = (4/3)*3.14*raio**3
    print (f'para uma esfera de raio {raio}, seu volume é de {volume}')

esfera(raio)

#8. Escreva um função que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra 
# for A a função calcula a média aritmética das notas do aluno, 
# se for P, a sua média ponderada (pesos: 5, 3 e 2) e se 
# for H, a sua média harmônica. A média calculada também 

nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
print ('''Se a letra for A, a função calcula a média aritmética das notas do aluno,
se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica''')
letra = input('digite uma das letras (A, P ou H): ')

def notas(nota1, nota2, nota3, letra):
    if letra == 'a' or letra == 'A':
        a = (nota1 + nota2 + nota3)/3
        print (f'a média aritmética é de {a}')

    elif letra == 'p' or letra == 'P':
        p = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
        print (f'a média ponderada é de {p}')

    elif letra == 'h' or letra == 'H':
        n1_inv = nota1 ** -1
        n2_inv = nota2 ** -1
        n3_inv = nota3 ** -1

        h = 3 / n1_inv + n2_inv + n3_inv
        print (f'a média harmônica é de {h}')

    else:
        print ('caractere inválido')

notas(nota1, nota2, nota3, letra)

# 9. Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro (True)
#  caso o valor seja primo e Falso (False) em caso contrário.

num = int(input('digite um numero inteiro: '))
 
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "não é um número primo")
            break
    else:
        print(num, "é um número primo")
 
else:
    print(num, "não é um número primo")

#10.Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

anos = int(input('idade: '))
meses = int(input('meses: '))
dias = int(input('dias: '))

def idade(anos, meses, dias):
    dias2 = anos * 365
    dias1=meses * 30
    total = dias + dias1 + dias2
    print(f'você possui {total} dias de idade!')

idade(anos, meses, dias)

#11. Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna , também por parâmetro, 
# a categoria desse nadador de acordo com a tabela abaixo:
# 6-7 inf A
# 8-10 inf B
# 11-13 juv A
# 14 - 17 juv B
# +18 adulto

age = int(input('digite sua idade: '))

def categoria(age):
    if 6 >= age <= 7:
        print ('a categoria é infantil A')

    elif 8 >= age <= 10:
        print ('a categoria é infantil B')

    elif 11 > age <= 13:
        print ('a categoria é juvenil A')

    elif 14 > age <= 17:
        print ('a categoria é juvenil B')

    elif age >= 18:
        print ('a categoria é adulto')

categoria(age)

#12.Faça uma função que recebe a média final de um aluno por parâmetro e retorna
#o seu conceito, conforme a tabela abaixo:

media = float(input('digite sua media: '))

def conceito(media):
    if 0 >= media <= 4.9:
        print ('D')

    elif 5 >= media <= 6.9:
        print ('C')

    elif 7 >= media <= 8.9:
        print ('B')

    elif 9 >= media <= 10:
        print ('A')

conceito(media)

#13.Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal.
#  Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x alt - 58 e, 
# para mulheres, peso ideal = 62.1 x alt - 44.7.

altura = float(input('digite sua altura: '))
sexo = input('digite seu sexo (fem - feminino, masc - masculino): ')

def peso_ideal(altura, sexo):
    if sexo == 'fem':
        pesoideal = 62.1 * altura - 44.7
        print('seu peso ideal é de ', pesoideal)

    if sexo == 'masc':
        pesoideal = 72.7 * altura - 58
        print('seu peso ideal é de ', pesoideal)

peso_ideal(altura, sexo)