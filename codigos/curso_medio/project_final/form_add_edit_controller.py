from PySide6.QtWidgets import QWidget

from ui_form_add_edit import Ui_Form
from component import Component


class Form(QWidget, Ui_Form):

    def __init__(self, title: str, component: Component = None, callback=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.callback = callback  # callback to exec to close
        self.component = component  # el componente a editar
        self.label.setText(title)
        self.init()
        self.component = component
        self.load_data_ui()


    def init(self):
        self.btn_cancel.clicked.connect(self.close_dialog)
        self.btn_save.clicked.connect(self.save)

    def load_data_ui(self):
        if self.component and self.callback:
            self.__load_component_to_ui(component=self.component)

    def __load_component_to_ui(self, component: Component):
        self.input_code.setText(component.code)
        self.input_name.setText(component.name)
        self.input_count.setValue(component.count)
        self.input_description.setPlainText(component.description)

    def get_component_from_ui(self):
        name = self.input_name.text()
        count = int(self.input_count.text())
        description = self.input_description.toPlainText()
        code = self.input_code.text()
        return Component(name=name, count=count, description=description, code=code)

    def save(self):
        if self.component and self.callback:
            component_updated = self.get_component_from_ui()
            component_updated.id = self.component.id
            self.callback(component_updated)
            self.close_dialog()
        elif self.callback:
            self.callback(self.get_component_from_ui())
            self.close_dialog()

    def close_dialog(self):
        self.close()
