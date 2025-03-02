import sys  # importo el modulo del sistema para pasar los argumentos a la aplicacion
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)  # se deben traer los modulos para crear el contexto de la aplicacion
from ui_main_window import Ui_MainWindow


class MiVentanaPrincipal(QMainWindow, Ui_MainWindow):

    # Esta clase me sirve para crear toda la interaccion con la ventana, las acciones de los botones, textos, todos los widgets, tambien se pueden agregar por codigo lo que sea necesario

    def __init__(self):
        super().__init__()  # inicializo el constructor padre QMainWindow
        self.setupUi(self)  # inicializo mi ventana que viene de Ui_MainWindow


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MiVentanaPrincipal()
    window.show()
    app.exec()
