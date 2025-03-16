import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QClipboard

from ui_window import Ui_Form
from password_generator import PasswordGenerator


class App(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.pwd = ""

    def init(self):
        """assign the signals to slots"""
        self.btn_clear.clicked.connect(self.clear_password)
        self.btn_generate.clicked.connect(self.generate_password)
        self.btn_copy.clicked.connect(self.copy_password)

    def generate_password(self):

        try:
            length = int(self.edit_length.text())
            self.pwd = PasswordGenerator().generate_password(length=length)
            self.lbl_password.setText(self.pwd)
        except:
            self.message("Error", "JUST NUMBERSS", QMessageBox.Icon.Critical)

    def clear_password(self):
        self.lbl_password.setText("-")
        self.pwd = ""

    def copy_password(self):
        if self.pwd:
            QClipboard().setText(self.pwd)
            self.message("Copied", "The password was copied to clipboard. You can paste", QMessageBox.Icon.Information)
        else:
            self.message("No password", "PASSWORD NOT SETTED", QMessageBox.Icon.Warning)

    def message(self, title, text, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
