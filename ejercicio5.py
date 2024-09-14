import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QDateEdit,
                             QPushButton,QVBoxLayout,QWidget,QLabel)
                              
                            
from PyQt5 import uic

"""
Construir un programa que muestre una ventana a traves
de la cual se puedan leer 10 datos caracteristicos
de una persona
"""
class ventanaPrin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ej5GUI.ui", self)
        self.nombres = self.findChild(QLineEdit,"lineEnom")
        self.apellidos = self.findChild(QLineEdit,"lineEap")
        self.nacionalidad = self.findChild(QLineEdit,"lineEnac")
        self.nacimiento = self.findChild(QDateEdit,"dateEdit")
        self.telefono = self.findChild(QLineEdit,"lineEtel")
        self.dui = self.findChild(QLineEdit,"lineEdui")
        self.email = self.findChild(QLineEdit,"lineEmail")
        self.locacion = self.findChild(QLineEdit,"lineEloc")
        self.estadoC = self.findChild(QLineEdit,"lineEcivil")
        self.genero = self.findChild(QLineEdit,"lineEgen")
        self.boton = self.findChild(QPushButton,"pushButton")
        self.boton.clicked.connect(self.mostrasDatos)
    
    def mostrasDatos(self):
        nom = self.nombres.text()
        ape = self.apellidos.text()
        nacio = self.nacionalidad.text()
        naci = self.nacimiento.text()
        tel = self.telefono.text()
        dui = self.dui.text()
        email = self.email.text()
        loca = self.locacion.text()
        esciv = self.estadoC.text()
        gen = self.genero.text()

        self.vdatos = ventanaDatos(nom,ape,nacio,naci,tel,
                                   dui, email, loca, esciv,gen)
        self.vdatos.show()

class ventanaDatos(QWidget):
    def __init__(self,nom, ape, nacio,naci,tel,
                 dui,email,loca,esciv,gen ):
        super().__init__()
        #se hace manual la 2da ventana o en designer, elegimos manual siguiendo la misma lógica
        self.setWindowTitle("Datos de la Persona")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Nombres: {nom}"))
        layout.addWidget(QLabel(f"Apellidos: {ape}"))
        layout.addWidget(QLabel(f"Nacionalidad: {nacio}"))
        layout.addWidget(QLabel(f"Nacimiento: {naci}"))
        layout.addWidget(QLabel(f"Teléfono: {tel}"))
        layout.addWidget(QLabel(f"DUI: {dui}"))
        layout.addWidget(QLabel(f"Correo Eléctronico: {email}"))
        layout.addWidget(QLabel(f"Locación: {loca}"))
        layout.addWidget(QLabel(f"Estado Civil: {esciv}"))
        layout.addWidget(QLabel(f"Género: {gen}"))

        self.setLayout(layout)

#para que no haya conflicto con las dos ventanas se usa este tipo de built-in
if __name__ == "__main__":
    app=QApplication(sys.argv)
    ventana = ventanaPrin()
    ventana.show()
    sys.exit(app.exec_())







