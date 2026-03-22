import sys

from PySide6.QtWidgets import ( QApplication,QMainWindow )

from ui_suma import Ui_MainWindow

class MiVentanaPrincipal(QMainWindow, Ui_MainWindow):
    
    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.init() ## arrancan las config

    def init(self):
        """Inicializar los elementos al arrancar la app
        """
        self.btn_sumar.clicked.connect(self.sumar)

    def sumar(self):
        """acciones a realizar cuando se presiona el boton
        """
        numero1 = float(self.input1.text()) # traigo el contenido del widget
        numero2 = float(self.input2.text()) 
        suma = numero1 + numero2
        self.lbl_result.setText(f"{suma}")


if __name__ == "__main__":
    app = QApplication(sys.argv) # esto siempre se pone, se crea el context de una aplicacion
    window = MiVentanaPrincipal()
    window.show() # mostar la ventana
    app.exec()  # ejecuta la aplicacion