import math
from PyQt6 import uic, QtWidgets
app = QtWidgets.QApplication([])
Form, Window  = uic.loadUiType("equacao_2_grau/layout.ui")
janela = Window()
formulario = Form()
formulario.setupUi(janela)
janela.show()
#----------------------------------------------------------------------

def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)

    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))

#----------------------------------------------------------------------
def calcular():
    a = float(formulario.txt_a.text())
    b = float(formulario.txt_b.text())
    c = float(formulario.txt_c.text())
    formulario.lbl_equacao.setText(f"{a}x² + {b}x - {c}")
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    formulario.lbl_delta.setText(f"Δ = {D}")
    formulario.lbl_x1.setText(f"x¹ = {x1}")
    formulario.lbl_x2.setText(f"x² = {x2}")

        
formulario.btn_calcular.clicked.connect(calcular)
app.exec()
