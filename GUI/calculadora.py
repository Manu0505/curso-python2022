# Importação da lib tkinter
from tkinter import *

from matplotlib.pyplot import pink
class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.container3_1 = Frame(master)
        self.container3_1["pady"] = 2
        self.container3_1.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()
        
        self.container5 = Frame(master)
        #self.container5["pady"] = 5
        self.container5.pack()
    

        self.titulo = Label(self.container1, text="CALCULADORA", foreground='#483D8B') #
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_num1 = Label(self.container1, text="Número 1: ", foreground='#483D8B') #
        self.lbl_num1["font"] = ("Arial", "10", "bold")
        self.lbl_num1.pack(side=LEFT)

        self.txt_num1 = Entry(self.container1, background='#836FFF', foreground='white')
        self.txt_num1["width"] = 25
        self.txt_num1["font"] = ("Arial", "10", "bold")
        self.txt_num1.pack(side=LEFT)

        self.lbl_num2 = Label(self.container2, text="Número 2: ", foreground='#483D8B') #
        self.lbl_num2["font"] = ("Arial", "10", "bold")
        self.lbl_num2.pack(side=LEFT)

        self.txt_num2 = Entry(self.container2, background='#836FFF', foreground='white')
        self.txt_num2["width"] = 25
        self.txt_num2["font"] = ("Arial", "10", "bold")
        self.txt_num2.pack(side=LEFT)

        self.autenticar = Button(self.container3, background='#836FFF', foreground='white')
        self.autenticar["text"] = "+"
        self.autenticar["font"] = ("Calibri", "10", 'bold')
        self.autenticar["width"] = 5
        self.autenticar["command"] = self.soma
        self.autenticar.pack(side=LEFT)

        self.autenticar = Button(self.container3, background='#836FFF', foreground='white')
        self.autenticar["text"] = "-"
        self.autenticar["font"] = ("Calibri", "10", 'bold')
        self.autenticar["width"] = 5
        self.autenticar["command"] = self.subtração
        self.autenticar.pack(side=LEFT)

        self.autenticar = Button(self.container3_1, background='#836FFF', foreground='white')
        self.autenticar["text"] = "x"
        self.autenticar["font"] = ("Calibri", "10", 'bold')
        self.autenticar["width"] = 5
        self.autenticar["command"] = self.multiplicação
        self.autenticar.pack(side=LEFT)

        self.autenticar = Button(self.container3_1, background='#836FFF', foreground='white')
        self.autenticar["text"] = "÷"
        self.autenticar["font"] = ("Calibri", "10", 'bold')
        self.autenticar["width"] = 5
        self.autenticar["command"] = self.divisão
        self.autenticar.pack(side=LEFT)

        self.lbl_resultado = Label(self.container4, text="", foreground='#483D8B')
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

        self.sair = Button(self.container5, text="Sair", background='#836FFF', foreground='white')
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", "10")
        self.sair["width"] = 5
        # PEgando o click
        self.sair["command"] = self.container5.quit
        self.sair.pack ()

    def soma(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        soma = num1 + num2
        self.lbl_resultado["text"] = f"{num1} + {num2} = {soma}"

    def subtração(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        sub = num1 - num2
        self.lbl_resultado["text"] = f"{num1} - {num2} = {sub}"

    def multiplicação(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        mult = num1 * num2
        self.lbl_resultado["text"] = f"{num1} x {num2} = {mult}"

    def divisão(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        div = num1 / num2
        self.lbl_resultado["text"] = f"{num1} ÷ {num2} = {div}"

    

root = Tk()
root.title ('calculadora')
Application(root)
root.mainloop()