# 4. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

l = input('digite F ou M:  ')

if l == 'f' or 'F':
    print('F - Feminino')

elif l == 'm' or 'M':
        print('M - Masculino')

else:
        print('Sexo inválido')