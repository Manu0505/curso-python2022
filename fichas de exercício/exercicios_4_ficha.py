
# 1. Faça um programa que leia números reais. Quando o número digitado for o número zero o programa
# deverá apresentar uma lista com todos os números que foram digitados e sair do laço while.Use while.

lista = []
while True:
    real = float(input('digite um numero real: '))
    if real != 0:
        lista.append(real)

    if real == 0:
        print(lista)
        break


# 2. Faça um programa que receba um usuário e senha. Se a senha de entrada for igual ao usuário,
# deverá ser apresentada a mensagem “Senha Inválida”, e pedir pro usuário inserir a senha novamente.
# Quando forem diferentes imprimir a mensagem “Senha aceita” e sair do laço while. DICA (Use while True e break).
#  Use while.

while True:
    senha = input('digite uma senha: ')
    usuario = input('digite um usuario: ')
    if usuario == senha:
        print('senha invalida. tente novamente')

    else:
        print('senha aceita')
        break


# 3. Faça um programa que lê um número inteiro n. Escrever a soma de todos os números de 1 até n. Use while.

while True:
    n = int(input("Digite o valor de n: "))
    soma = n * (n + 1) // 2
    print("A soma dos", n, "primeiros inteiros positivos é", soma)
    break


# 4. Faça um programa para ler um número inteiro n. Escrever a soma de todos os números pares de 2 até n. Use while.

n = int(input("Digite o valor de n: "))


soma = 0


i = 1
while i % 2 == 2 and i <= n:
    soma = soma + i
    i = i + 1


print("A soma dos", n, "primeiros inteiros positivos é", soma)

# 5. Faça um programa que lê um número inteiro n. E verifique se n é um número par, se não for pedir para inserir
# outro número até que seja par. Use while.

while True:
    num = int(input('digite um numero par inteiro: '))
    if num % 2 != 0:
        print('o numero não é par, tente novamente')
    else:
        break


# 6. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares.

n = 1
P = 0
I = 0
while n <= 10:
    a = int(input("a:  "))
    n = n + 1
    if a % 2 == 0:
        a = P
        P = P + 1
    else:
        a = I
        I = I + 1

print("A qtd de números pares é: ", P)
print("A qtd de números ímpares é: ", I) 
