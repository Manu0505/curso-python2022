g1 = float(input('insira a primeira nota:  '))
g2 = float(input('insira a segunda nota:  '))

med = (g1+g2) / 2

if 9 <= med <= 10:
    print ('Você recebeu um A')

elif 7.5 <= med < 9:
    print ('Você recebeu um B')

elif 6 <= med < 7.5:
    print ('Você recebeu um C')

elif 4 <= med < 6:
    print ('Você recebeu um D')

elif 4 <= med < 0:
    print ('Você recebeu um E')