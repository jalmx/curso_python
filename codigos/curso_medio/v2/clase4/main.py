import sys

from PySide6.QtWidgets import ( QApplication,QMainWindow )

from ui_ventana import Ui_MainWindow

class MiVentanaPrincipal(QMainWindow, Ui_MainWindow):
    
    def __init__(self): 
        super().__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv) # esto siempre se pone, se crea el context de una aplicacion
    window = MiVentanaPrincipal()
    window.show() # mostar la ventana
    app.exec()  # ejecuta la aplicacion