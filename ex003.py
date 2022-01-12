

#3 - Faça uma função que receba uma lista, percorra a lista e some a quantidade dos números pares dessa lista e 
#retorne a soma. Imprimir a lista e o resultado da soma ao final do código.

lista = [1,2,3,2,1,2,3,4,5,6,5,4,3,2,1,8,10,12]


def func(lista):
    c = 0
    for q in lista:
      if q % 2 == 0:
          c = c+1 
    return c

        

print ('lista:', lista)
print ('a quantidade de números pares é', func (lista))