# 1. Faça um Programa que leia 5 números inteiros, insira em uma lista emostre-os.

g = 5
lista_numeros = []
for x in range(g):
    numero = int(input("Digite um  numero inteiro: "))
    novos_numeros = [numero]
    lista_numeros.append(novos_numeros)

print(f'os numeros escolhidos foram {lista_numeros}')

# 2. Faça um Programa que leia 10 números reais, insira em uma lista e
# mostre-os na ordem crescente (use a função sort()).


h = 10

lista_n_reais = []
for x in range(h):
    numero_real = float(input("Digite um  numero real: "))
    novos_numeros_reais = [numero_real]
    lista_n_reais.append(novos_numeros_reais)
    lista_n_reais.sort()

print(f'Em ordem crescente, os numeros reais escolhidos foram {lista_n_reais}')

# 3. Faça um Programa que leia N (peça pro usuário informar o valor de N) notas
# e insira em uma lista, depois percorra a lista e calcule a soma das notas, por
# fim calcule a média (soma dividido por N) e mostre na tela.

n = int(input('insira quantas notas deseja cadastrar:  '))

lista_notas = []
for notas in range(n):
    nota = float(input("insira a nota: "))
    
    lista_notas.append(nota)


#...depois percorra a lista e calcule a soma das notas - COMO SOMAR

soma = 0
for nota in lista_notas:
    soma += nota


media = soma / n                                                                #!!!!!!!!!!!!!!!!!!!

print (f'a sua média é de {media}')

# 4. Faça um Programa que peça o nome, a idade e a altura de N pessoas,
# armazene cada informação em uma lista e depois insira em uma lista maior
# chamada lista_pessoas. Por fim, imprima o nome e peso de cada pessoa, e
# diga se ela é maior ou menor de idade.

n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    altura = input("Digite a altura da pessoa, em cm: ")
    nova_pessoa = [nome, idade, altura]
    lista_pessoas.append(nova_pessoa)


for pessoa in lista_pessoas:
    print(f"Bem-vindo(a)! Olá, {nova_pessoa[0]}. Você tem {nova_pessoa[1]} anos, e mede {nova_pessoa [2]} cm")

if idade >= 18:
    print('você é maior de idade')

if idade < 18:
    print('você é menor de idade')


# 5. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do
# outro.(usar for com range)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numeros in range(len(numbers)):
  print(numbers[numeros])

# 6. Faça um programa que leia 5 números e informe o maior número.(Dica: Use
# lista, função .sort() e indexação negativa (pegar i item [-1]))

a = 5
num = []
for i in range(a):
    n1 = float(input("Digite o número: "))
    n1_list = [n1]
    num.append(n1_list)


num.sort()

print (num[-1])



# 7. Faça um programa que imprima na tela apenas os números ímpares entre 1
# e 50.(Use range de intervalos (range(x, y)))


q = 0
for q in range(1, 51):
    if q % 2 != 0:
        print(q)


# 8. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.(Use range de
# intervalos (range(x, y)))

v1 = int(input('Digite um numero: '))
v2 = int(input('Digite um outro numero: '))

b = range (v1, v2)
print (b)

# 9. Faça um programa que, dado um conjunto de N números, determine o menor
# valor, o maior valor e a soma dos valores.

p = int(input ('insira quantos números quer adicionar: '))
n3 = []
for i in range(p):
    n9 = float(input("Digite o número: "))
    n3_lista = n9
    n3.append(n3_lista)


n3.sort()

soma = n3[-1] + n3[0]

print(n3)
print (f'o maior valor é{n3[-1]}')
print (f'o menor valor é{n3[0]}')
print (f'a soma dos valores é {soma}')

# 10.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
# número inteiro entre 1 a 10. O usuário deve informar de qual número ele
# deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input("Digite o número para gerar a tabuada: "))
if numero >= 1 and numero <= 10:
    print("Tabuada de ", numero)
    for indice in range(1, 11):
        print(f"{numero} X {indice} == {numero * indice}")
else:
    print("Número inválido. Digite entre 1 e 10! ") 
