# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    endereco = input("Digite o endereço da pessoa: ")
    peso = input("Digite o peso da pessoa: ")
    nova_pessoa = [nome, idade, endereco, peso]
    lista_pessoas.append(nova_pessoa)
else:
    print("O cadastro de pessoas foi finalizado!")


for pessoa in lista_pessoas:
    print(f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos, mora em {pessoa[2]} e pesa {pessoa [3]} kg")

if idade >= 18:
    print('você é maior de idade')

if idade < 18:
    print('você é menor de idade')

else:
    print("A listagem de pessoas foi finalizado!")

print("Quantidade de pessoas cadastradas: ", len(lista_pessoas))



# adicionar endereço, peso
#2 - Verifiquem se a pessoa é maior de idade:
    #MAIOR DE IDADE: Você é maior de idade.
    #MENOR DE IDADE: Você é menor de idade. 