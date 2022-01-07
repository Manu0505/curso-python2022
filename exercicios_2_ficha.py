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
        print(f'seu IMC é de {imc}. Isso significa que você está com Obesidade I.')

# 4. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

l = str(input('digite F ou M:  '))

if l == 'f':
    print('F - Feminino')

    if l == 'm':
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
    print(f'Sua média é de {media}. Parabéns, você foi aprovado(a) com distinção!.')

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
