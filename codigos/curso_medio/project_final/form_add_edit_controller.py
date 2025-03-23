from PySide6.QtWidgets import QWidget

from ui_form_add_edit import Ui_Form


class Form(QWidget, Ui_Form):

    def __init__(self, title: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.label.setText(title)
