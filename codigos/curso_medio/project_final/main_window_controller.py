from PySide6.QtWidgets import QMainWindow
from ui_main_window import Ui_MainWindow
from form_add_edit_controller import Form

from componente_controller import ComponentController
from component import Component


class MainWindow(QMainWindow, Ui_MainWindow):

    dialog = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_events()
        self.db = ComponentController()
        self.load_data_table()

    def init_events(self):
        self.btn_add.clicked.connect(self.add_componente)
        self.btn_edit.clicked.connect(self.edit_component)
        self.btn_delete.clicked.connect(self.delete_element)
        self.btn_edit.clicked.connect(self.edit_component)
        self.btn_search_table.clicked.connect(self.search_table)
        self.btn_search_id.clicked.connect(self.search_one)

    def load_data_table(self):
        if self.db:
            components = self.db.get_all()
            for c in components:
                print(c)

    def delete_element(self):
        pass

    def edit_component(self):
        pass

    def add_component(self):
        pass

    def search_table(self):
        pass

    def search_one(self):
        pass

    def add_componente(self):
        self.dialog = Form("Agregar componente")
        self.dialog.show()

    def edit_component(self):
        self.dialog = Form("Editar componente")
        self.dialog.show()
