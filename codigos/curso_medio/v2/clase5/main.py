import sys
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox

from ui_ohm import Ui_Form

from ohm_lay import *

class App(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        """inicializar los eventos de los widgets
        """
        self.buttonGroup_calculate.buttonToggled.connect(self.calculate)
        self.btn_calculate.clicked.connect(self.calculate)
    
    def calculate(self):
        """ metodo para obtener los datos y calcular el resultado """
        radio = self.buttonGroup_calculate.checkedButton().objectName()
        
        resultado = None
        valor1 = float(self.input_one.text() or 0) 
        valor2 = float(self.input_two.text() or 0) 

        if radio.find("voltage") >= 0:
            resultado = OhmsLaw.calculateVoltage(current=Voltage(value=valor1), resistance= Resistance(value=valor2))
            
        elif radio.find("current") >= 0:
            print("corriente")
            try:
                resultado = OhmsLaw.calculateCurrent(voltage=Voltage(value=valor1), resistance=Resistance(value=valor2))
            except :
                msg = QMessageBox()
                msg.setText("Error con la resistencia, no puede ser 0")
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.exec()

        elif radio.find("resistence") >= 0:
            print("resistenc")
            resultado = OhmsLaw.calculateResistance(voltage=Voltage(value=valor1), current=Current(value=valor2))

        self.lbl_result.setText(str(resultado) if resultado else "No valido")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())