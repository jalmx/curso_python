from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_main_window import Ui_MainWindow
from form_add_edit_controller import Form

from componente_controller import ComponentController
from component import Component


class MainWindow(QMainWindow, Ui_MainWindow):

    dialog = None
    components = None
    TAB_TABLE = 0
    TAB_ONE = 1
    component = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_events()
        self.db = ComponentController()
        self.build_data_table()

    def init_events(self):
        self.btn_add.clicked.connect(self.add_componente)
        self.btn_edit.clicked.connect(self.edit_component)
        self.btn_delete.clicked.connect(self.delete_element)
        self.btn_search_table.clicked.connect(self.search_table)
        self.input_search_table.returnPressed.connect(self.search_table)
        self.btn_search_id.clicked.connect(self.search_one)
        self.input_search_id.returnPressed.connect(self.search_one)

    def build_data_table(self):
        if self.db:
            components = self.db.get_all()
            self.components = components
            size = self.db.get_size()
            self.__load_data_table(components=components, size=size)

    def __load_data_table(self, components: list[Component], size: int):

        self.table_components.setRowCount(size)

        for i, component in enumerate(components):
            self.table_components.setItem(i, 0, QTableWidgetItem(str(component.id)))
            self.table_components.setItem(i, 1, QTableWidgetItem(component.name))
            self.table_components.setItem(i, 2, QTableWidgetItem(component.code))
            self.table_components.setItem(i, 3, QTableWidgetItem(str(component.count)))
            self.table_components.setItem(i, 4, QTableWidgetItem(component.description))
            self.table_components.setItem(i, 5, QTableWidgetItem(component.location))
            self.table_components.setItem(i, 6, QTableWidgetItem(str(component.status)))

    def __build_message(self, component: Component):
        message = QMessageBox(self)
        message.setWindowTitle("Delete Component")
        message.setText(
            f"You're going to delete:<br><strong>[Component: {component.name} with Code: {component.code}]</strong>"
        )
        message.setIcon(QMessageBox.Icon.Warning)
        message.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        return message.exec()

    def message_error(self):
        QMessageBox.information(self, "Error", "No component selected")

    def delete_element(self):

        component_to_delete = None
        if self.__get_current_tab() == self.TAB_TABLE:
            component = self.__get_component()
            if component:
                component_to_delete = component

        elif self.__get_current_tab() == self.TAB_ONE:
            if self.component:
                component_to_delete = self.component
        if not component_to_delete:
            self.message_error()

        if component_to_delete:
            answer = self.__build_message(component=component_to_delete)
            if answer == QMessageBox.StandardButton.Ok:
                self.db.delete(component_to_delete.id)

                QMessageBox.information(
                    self, "Deleted", "Componente Deleted Successfully"
                )
            else:
                self.message_error()

            self.build_data_table()
            self.component = None
            self.clear_one()

    def search_table(self):
        word = self.input_search_table.text()
        components_dict = self.db.search(word)
        self.__load_data_table(
            components=components_dict["components"], size=components_dict["size"]
        )

    def search_one(self):
        word = self.input_search_id.text()
        components = self.db.search_by_code(word)
        if components["size"] and word:
            self.component = components["components"][0]
            self.__load_one(self.component)
        else:
            self.clear_one()

    def clear_one(self):
        edits = [
            self.edit_code,
            self.edit_count,
            self.edit_name,
            self.edit_description,
            self.lbl_info,
        ]
        for e in edits:
            e.clear()
        self.component = None

    def __load_one(self, component: Component):

        def text():
            return f"ID: {component.id}\nLocation: {component.location}\nStatus: {component.status}"

        if component:
            self.edit_code.setText(component.code)
            self.edit_count.setText(str(component.count))
            self.edit_name.setText(component.name)
            self.edit_description.setPlainText(component.description)
            self.lbl_info.setText(text())

    def __get_current_tab(self):
        return self.tabWidget.currentIndex()

    def add_componente(self):
        self.dialog = Form("Add component", callback=self.__save_data)
        self.dialog.show()

    def __save_data(self, component: Component):
        self.db.insert(component=component)
        self.build_data_table()

    def edit_component(self):
        title_window = "Edit component"
        if self.__get_current_tab() == self.TAB_TABLE and self.__get_component():
            component = self.__get_component()

            self.dialog = Form(
                title_window,
                callback=self.__update_component,
                component=component,
            )
            self.dialog.show()

        elif self.__get_current_tab() == self.TAB_ONE and self.component:

            self.dialog = Form(
                title_window,
                callback=self.__update_component,
                component=self.component,
            )
            self.dialog.show()
            return
        else:
            self.message_error()

    def __get_component(self):
        i = self.table_components.currentRow()
        if i != -1:
            return self.components[i]

        return None

    def __update_component(self, component):
        self.db.update(component=component)
        self.build_data_table()
