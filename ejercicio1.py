import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
"""
Contruir un programa que muestre una ventana en la cual
aparezca su nombre completo y su edad centrados
"""
class mainventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1")
        uic.loadUi("ej1GUI.ui",self)

app =QApplication(sys.argv)
ventana = mainventana()
ventana.show()
app.exec_()