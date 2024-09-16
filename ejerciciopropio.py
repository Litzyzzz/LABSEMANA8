import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

"""
La problemática que queremos plantear con este programa es que un restaurante x necesita registrar
y organizar los diferentes platillos junto con sus precios, así que planteamos esta solución en donde 
ese restaurante puede registrar los distintos platillos que el cliente elige y asi de manera más eficiente obtener la informacion de 
cada plato.
"""
class VentanaPlatos(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("platosGUI.ui", self)  

        self.pushButtonRegistrar.clicked.connect(self.mostrarPlatos)

    def mostrarPlatos(self):
  
        nombre1 = self.lineEditNombre1.text()
        ingredientes1 = self.lineEditIngredientes1.text()
        tipo1 = self.comboBoxTipoPlato1.currentText() 
        precio1 = self.lineEditPrecio1.text()

        nombre2 = self.lineEditNombre2.text()
        ingredientes2 = self.lineEditIngredientes2.text()
        tipo2 = self.comboBoxTipoPlato2.currentText()  
        precio2 = self.lineEditPrecio2.text()

        nombre3 = self.lineEditNombre3.text()
        ingredientes3 = self.lineEditIngredientes3.text()
        tipo3 = self.comboBoxTipoPlato3.currentText()  
        precio3 = self.lineEditPrecio3.text()

        try:
         
            precio1 = float(precio1)
            precio2 = float(precio2)
            precio3 = float(precio3)
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese precios válidos")
            return


        total_precio = precio1 + precio2 + precio3
        resultado = (f"Plato 1: {nombre1}, Ingredientes: {ingredientes1}, Tipo: {tipo1}, Precio: ${precio1}\n"
                     f"Plato 2: {nombre2}, Ingredientes: {ingredientes2}, Tipo: {tipo2}, Precio: ${precio2}\n"
                     f"Plato 3: {nombre3}, Ingredientes: {ingredientes3}, Tipo: {tipo3}, Precio: ${precio3}\n\n"
                     f"Precio total de los platos: ${total_precio}")

        self.labelResultado.setText(resultado)


app = QApplication(sys.argv)
ventana = VentanaPlatos()
ventana.show()
app.exec_()
