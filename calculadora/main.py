
from PyQt6 import uic, QtWidgets

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window  = uic.loadUiType("calculadora/tela.ui")

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

janela.show()


#----------------------------------------------------------------------

def soma():
    n1 = float(formulario.txt_n1.text())
    n2 = float(formulario.txt_n2.text())
    soma = n1 + n2
    formulario.lbl_result.setText(f"Resultado: {n1} + {n2} = {soma}")
def sub():
    n1 = float(formulario.txt_n1.text())
    n2 = float(formulario.txt_n2.text())
    sub = n1 - n2
    formulario.lbl_result.setText(f"Resultado: {n1} - {n2} = {sub}")
def mult():
    n1 = float(formulario.txt_n1.text())
    n2 = float(formulario.txt_n2.text())
    mult = n1 * n2
    formulario.lbl_result.setText(f"Resultado: {n1} x {n2} = {mult}")
def div():
    n1 = float(formulario.txt_n1.text())
    n2 = float(formulario.txt_n2.text())
    div = n1 / n2
    formulario.lbl_result.setText(f"Resultado: {n1} ÷ {n2} = {div}")
    

'''
sub = matematica.subt(num1, num2)
soma = matematica.soma(num1, num2)
mult = matematica.mult(num1, num2)
div = matematica.div(num1, num2)

print(f"{num1} + {num2} == {soma}")
print(f"{num1} - {num2} == {sub}")
print(f"{num1} * {num2} == {mult}")
print(f"{num1} / {num2} == {div}")
'''


formulario.btn_soma.clicked.connect(soma)
formulario.btn_sub.clicked.connect(sub)
formulario.btn_mult.clicked.connect(mult)
formulario.btn_div.clicked.connect(div)

#formulario.btn_limpar.clicked.connect(limpar)

app.exec()