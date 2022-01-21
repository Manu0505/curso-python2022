from tkinter import *
#https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

#__init__ = construtor padrão
class Tela:
    #receber a master root do tkinter
    def __init__(self, master=None):
        #criação de um conteiner
        self.widget1 = Frame(master)
        #registro do conteiner
        self.widget1.pack()
        #criar um widget e adicionar ao conteiner
        self.msg = Label(self.widget1, text="Olá mundo")
        #registro do conteiner
        self.msg.pack ()
        pass

#criar uma variavel/objeto do tipo Tk()
root = Tk()
#passando o root para a mknha classe
Tela(root)
# event loop -  verifica constantemente se outro evento foi acionado
root.mainloop()