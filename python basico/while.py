#1 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite um nome de usuario: ")
    senha = input("Digite uma senha: ")
    if usuario != senha:
        print("Seja bem vindo, seu cadastro foi finalizado! ")
        break
    else:
         print("Continue tentando, a senha não pode ser igual ao nome de usuário. ")

# Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input("Digite um valor entre 0 e 10: "))
    if (nota >= 0 and nota <= 10):
        print("Parabéns, o valor está entre 0 e 10: ")
        break
    else:
         print("Continue tentando, valor não está entre 0 e 10: ")

#2 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50


