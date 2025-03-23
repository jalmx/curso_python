import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_ventana import Ui_Sumador


class Ventana(QWidget, Ui_Sumador):
    """docstring for Ventana."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # la configuracion o creacion de la ventana
        self.init()

    def init(self):
        # voy asignar los eventos
        self.btn_sumar.clicked.connect(self.sumar)

    def sumar(self):
        numero1 = float(self.input_1.text())
        numero2 = float(self.input_2.text())
        print(numero1 + numero2)
        resultado = numero1 + numero2
        self.lbl_resultado.setText(str(resultado))


if __name__ == "__main__":
    app = QApplication(sys.argv)  # creo una instancia de una aplicacion QT
    ventana = Ventana()  # creo una instancia de mi ventana
    ventana.show()  # muetro mi ventana
    sys.exit(app.exec())  # ejecuto mi aplicacion
