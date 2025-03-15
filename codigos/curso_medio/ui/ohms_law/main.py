import sys
from PySide6.QtWidgets import QWidget, QApplication

from ui_ohm_law import Ui_OhmsLawApp
from ohm_law import *


class AppOhmLaw(QWidget, Ui_OhmsLawApp):

    ONE = 11
    TWO = 22

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        self.buttonGroup_calculate.buttonToggled.connect(self.calculate)
        self.btn_calculate.clicked.connect(self.calculate)

    def get_value_edit(self, edit_number):
        value = (
            self.input_one.text() if edit_number == self.ONE else self.input_two.text()
        )

        return float(value)

    def calculate(self):
        radio = self.buttonGroup_calculate.checkedButton().objectName()
        result = 0
        unit = ""

        if Voltage(0).name() in radio:
            result = (
                Current(self.get_value_edit(self.ONE)).value
                * Resistance(self.get_value_edit(self.TWO)).value
            )
            unit = Voltage(0).unit_letter
        elif Current(0).name() in radio:
            result = (
                Voltage(self.get_value_edit(self.ONE)).value
                / Resistance(self.get_value_edit(self.TWO)).value
            )
            unit = Current(0).unit_letter
        elif Resistance(0).name() in radio:
            result = (
                Voltage(self.get_value_edit(self.ONE)).value
                / Current(self.get_value_edit(self.TWO)).value
            )
            unit = Resistance(0).unit_letter

        self.lbl_result.setText(f"{result}{unit}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppOhmLaw()
    window.show()

    sys.exit(app.exec())
