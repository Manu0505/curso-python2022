import numpy as np
import matplotlib.pyplot as plt

#Crie um gráfico pizza em Python para 
# mostrar por dia da semana o número de
#  frutas que uma pessoa comprou:

y = np.array([35, 25, 25, 15, 34, 21, 2])
mylabels = ["Segunda", "Terça", 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
plt.pie(y, labels = mylabels)
plt.show()


#Crie um gráfico linha em Python para 
# mostrar a relação da quantidade de 
# litros de agua ingerido por calorias. 

y = np.array([4,5,6,4,7,8,7])
x = np.array([140,120,122,150, 330, 211, 90])
plt.plot(x, y)
#plt.show()