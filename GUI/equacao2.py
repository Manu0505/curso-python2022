import formulas
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1["padx"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container1["padx"] = 10
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 2
        self.container4.pack()

        #-----------------------------

        self.titulo = Label(self.container1, text="CALCULADORA DE EQUAÇÃO DO 2 GRAU", foreground='#483D8B') #
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.titulo = Label(self.container1, text="ax² + bx - c = 0", foreground='#483D8B') #
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_A = Label(self.container1, text=" ↓ Digite o valor de 'a' ↓ ", foreground='#483D8B') #
        self.lbl_A["font"] = ("Arial", "10", "bold")
        self.lbl_A.pack(side=TOP)

        self.txt_A = Entry(self.container1, background='#836FFF', foreground='white')
        self.txt_A["width"] = 20
        self.txt_A["font"] = ("Arial", "10", "bold")
        self.txt_A.pack(side=TOP)

        self.lbl_B = Label(self.container1, text="↓ Digite o valor de 'b' ↓", foreground='#483D8B') #
        self.lbl_B["font"] = ("Arial", "10", "bold")
        self.lbl_B.pack(side=TOP)

        self.txt_B = Entry(self.container1, background='#836FFF', foreground='white')
        self.txt_B["width"] = 20
        self.txt_B["font"] = ("Arial", "10", "bold")
        self.txt_B.pack(side=TOP)

        self.lbl_C = Label(self.container1, text="↓ Digite o valor de 'c' ↓", foreground='#483D8B') #
        self.lbl_C["font"] = ("Arial", "10", "bold")
        self.lbl_C.pack(side=TOP)

        self.txt_C = Entry(self.container1, background='#836FFF', foreground='white')
        self.txt_C["width"] = 20
        self.txt_C["font"] = ("Arial", "10", "bold")
        self.txt_C.pack(side=BOTTOM)

        self.btn_calcular = Button(self.container2, background='#836FFF', foreground='white')
        self.btn_calcular["text"] = "calcular"
        self.btn_calcular["font"] = ("Calibri", "10", 'bold')
        self.btn_calcular["width"] = 5
        self.btn_calcular["command"] = self.calcular
        self.btn_calcular.pack(side=LEFT)
        self.lbl_delta = Label(self.container3, text="Δ =  ", foreground='#483D8B')
        self.lbl_delta["font"] = ("Arial", "10", "bold")
        self.lbl_delta.pack()
        self.lbl_x1 = Label(self.container3, text="X¹ = ", foreground='#483D8B')
        self.lbl_x1["font"] = ("Arial", "10", "bold")
        self.lbl_x1.pack()
        self.lbl_x2 = Label(self.container3, text="X² = ", foreground='#483D8B')
        self.lbl_x2["font"] = ("Arial", "10", "bold")
        self.lbl_x2.pack()
    def calcular(self):
        a = float(self.txt_A.get())
        b = float(self.txt_B.get())
        c = float(self.txt_C.get())
        delta = formulas.delta(a, b, c)
        self.lbl_delta["text"] = f"Δ = {delta}"
        if delta >= 0:
            x1 = formulas.x1(a, b, delta)
            x2 = formulas.x2(a, b, delta)
            self.lbl_x1["text"] = f"X¹ = {x1}"
            self.lbl_x1["foreground"] = '#483D8B'
            self.lbl_x2["text"] = f"X² = {x2}"
        else:
            self.lbl_x1["text"] = f"Não existem raízes reais"
            self.lbl_x2["text"] = ""

        

#

root = Tk()
root.title ('equação de 2° grau')
Application(root)
root.mainloop()