ano = int(input('Insira seu ano de nascimento:  '))
idade = 2022 - ano

if idade <= 18:
    print(f'você tem {idade} anos.')
    print('você é maior de idade')

if idade > 18:
    print(f'você tem {idade} anos.')
    print('você é menor de idade')