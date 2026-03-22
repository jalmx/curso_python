import sys

from PySide6.QtWidgets import ( QApplication,QMainWindow, QMessageBox )

from password_generator import PasswordGenerator
from ui_password import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__() ##siempre se hace
        self.setupUi(self) # esta tambien
        self.init()

    def init(self):
        """asigno los eventos a los botones
        """
        self.btn_generator.clicked.connect(self.generate_password)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_copy.clicked.connect(self.copy)

    def generate_password(self):
        try:
            long_pwd = int(self.input.text()) or 8
            pwd = PasswordGenerator().generate_password(length=long_pwd)
            print(pwd)
            self.txt_pwd.setPlainText(pwd)
        except:
            self.message("Error", "Solo se aceptan numeros", QMessageBox.Icon.Critical)
    
    def clear(self):
        self.txt_pwd.setPlainText("")
        self.input.setText("")
        self.message("Limpiar", "Se limpiaron los campos", QMessageBox.Icon.Information)

    def copy(self):
        txt = self.txt_pwd.toPlainText()
        print("pwd copiado", txt)
        if txt:
            QApplication.clipboard().setText(txt)
            self.message("Copiar", "Se copio el password", QMessageBox.Icon.Information)
        else:
            self.message("Copiar", "No hay password", QMessageBox.Icon.Critical)

    def message(self, title, text, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)   
        msg.setWindowTitle(title)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv) # esto siempre se pone, se crea el context de una aplicacion
    window = MyApp()
    window.show() # mostar la ventana
    app.exec()  # ejecuta la aplicacion