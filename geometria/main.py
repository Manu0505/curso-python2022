# pedir se quer calcular a area do circ ou do quadr (if)
import geometria

escolha = input('\nvocê deseja calcular a area do quadrado ou do circulo? \n 1 - quadrado \n 2 - circulo\n \nopção: \n')

if escolha == '1':
    l = float(input('\ndigite o lado do quadrado: \n'))
    geometria.quadrado(l)
    print(f'\na area do quadrado de lado {l} é igual a {geometria.quadrado(l)}')

elif escolha == '2':
    r = float(input('digite o raio do circulo: \n'))
    geometria.circulo(r)
    print(f'a area do circulo de raio {r} é igual a {geometria.circulo(r)}')

else:
    print('opção inválida')