from PySide6.QtWidgets import QApplication
from main_window_controller import MainWindow

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
