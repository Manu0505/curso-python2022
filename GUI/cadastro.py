from tkinter import *

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

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        #-------------------------

        self.titulo = Label(self.container1, text="LOGIN NO SISTEMA", foreground='#483D8B') #
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.lbl_user = Label(self.container2, text="USUÁRIO: ", foreground='#483D8B') #
        self.lbl_user["font"] = ("Arial", "10", "bold")
        self.lbl_user.pack(side=LEFT)

        self.txt_user = Entry(self.container2, foreground='#483D8B')
        self.txt_user["width"] = 10
        self.txt_user["font"] = ("Arial", "10", "bold")
        self.txt_user.pack(side=LEFT)

        self.lbl_senha = Label(self.container2, text="SENHA: ", foreground='#483D8B') #
        self.lbl_senha["font"] = ("Arial", "10", "bold")
        self.lbl_senha.pack(side=LEFT)

        self.txt_senha = Entry(self.container2, foreground='#483D8B')
        self.txt_senha["width"] = 10
        self.txt_senha["font"] = ("Arial", "10", "bold")
        self.txt_senha.pack(side=LEFT)

        
        self.btn_sair = Button(self.container3, background='#836FFF', foreground='white')
        self.btn_sair["text"] = "Sair"
        self.btn_sair["font"] = ("Calibri", "15")
        self.btn_sair["width"] = 5
        self.btn_sair["command"] = self.container3.quit
        self.btn_sair.pack(side=LEFT)

        self.btn_login = Button(self.container3, background='#836FFF', foreground='white')
        self.btn_login["text"] = "Login"
        self.btn_login["font"] = ("Calibri", "15")
        self.btn_login["width"] = 5
        self.btn_login["command"] = self.login
        self.btn_login.pack(side=LEFT)

        self.lbl_login = Label(self.container4, text=" ", foreground='#483D8B')
        self.lbl_login["font"] = ("Arial", "10", "bold")
        self.lbl_login.pack()

    def login(self):
     user = (self.txt_user.get())
     senha = (self.txt_senha.get())

     if user == senha:
        self.lbl_login["text"] = f"Não foi possivel fazer login"

     elif user != senha:
        self.lbl_login["text"] = f"Seja bem-vindo(a)!"

        



    
root = Tk()
root.title ('cadastro')
Application(root)
root.mainloop()