import math
from PyQt6 import uic, QtWidgets
app = QtWidgets.QApplication([])
Form, Window  = uic.loadUiType("equacao_2_grau/layout.ui")
janela = Window()
formulario = Form()
formulario.setupUi(janela)
janela.show()
#----------------------------------------------------------------------
def calcular():
    a = float(formulario.txt_a.text())
    b = float(formulario.txt_b.text())
    c = float(formulario.txt_c.text())
    formulario.lbl_equacao.setText(f"{a}x² + {b}x - {c}")
    delta = math.pow (b, 2) - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        formulario.lbl_delta.setText(f"Δ = {delta}")
        formulario.lbl_x1.setText(f"x¹ = {x1}")
        formulario.lbl_x2.setText(f"x² = {x2}")
    elif delta < 0:
        formulario.lbl_delta.setText(f"Δ = {delta}")
        formulario.lbl_x1.setText(f"x¹ = não existem raízes reais")
        formulario.lbl_x2.setText(f"x² = não existem raízes reais")
        
formulario.btn_calcular.clicked.connect(calcular)
app.exec()
