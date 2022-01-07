ano = int(input('Insira seu ano de nascimento:  '))
idade = 2022 - ano

resposta = str(input('você já fez aniversário esse ano? (responda apenas com sim ou não, precisamente.)  '))

if resposta == 'sim' and idade <= 18:
    print (f'você tem {idade} anos. você é maior de idade.')

if resposta == 'não' and idade == 18:
        print(f'você tem {idade-1} anos. Você não é maior de idade.')

if resposta == 'não' and idade < 18:
            print(f'você tem {idade} anos. você é maior de idade.')