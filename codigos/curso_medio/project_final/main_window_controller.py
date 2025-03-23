from PySide6.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow
from form_add_edit_controller import Form


class MainWindow(QMainWindow, Ui_MainWindow):

    form = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_events()

    def init_events(self):
        self.btn_add.clicked.connect(self.add_componente)
        self.btn_edit.clicked.connect(self.edit_component)

    def add_componente(self):

        self.form = Form("Agregar componente")
        self.form.show()

    def edit_component(self):
        self.form = Form("Editar componente")
        self.form.show()
