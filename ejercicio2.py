import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
                            
from PyQt5 import uic, QtWidgets
"""
Construir un programa que muestre una 
ventana y que lea una clave secreta sin 
mostrar los caracteres que la componen
"""
class ventanaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ej2GUI.ui",self)
        self.boton = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.contratxt = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.etiquetaN= self.findChild(QtWidgets.QLabel,"label_2")
        self.boton.clicked.connect(self.pasarContra)
    
    def pasarContra(self):
        contra =self.contratxt.text()
        if contra == "HolaMundo":
            self.etiquetaN.setText("Contraseña Correcta")
        else:
            self.etiquetaN.setText("Contraseña Incorrecta")
        


app =QApplication(sys.argv)
ventana = ventanaMain()
ventana.show()
app.exec_()