# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ohm.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(431, 412)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")
        font = QFont()
        font.setPointSize(25)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.Panel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_voltage = QRadioButton(self.widget_4)
        self.buttonGroup_calculate = QButtonGroup(Form)
        self.buttonGroup_calculate.setObjectName(u"buttonGroup_calculate")
        self.buttonGroup_calculate.addButton(self.radio_voltage)
        self.radio_voltage.setObjectName(u"radio_voltage")
        self.radio_voltage.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radio_voltage)

        self.radio_current = QRadioButton(self.widget_4)
        self.buttonGroup_calculate.addButton(self.radio_current)
        self.radio_current.setObjectName(u"radio_current")

        self.horizontalLayout_4.addWidget(self.radio_current)

        self.radio_resistence = QRadioButton(self.widget_4)
        self.buttonGroup_calculate.addButton(self.radio_resistence)
        self.radio_resistence.setObjectName(u"radio_resistence")

        self.horizontalLayout_4.addWidget(self.radio_resistence)


        self.verticalLayout.addWidget(self.widget_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.linea_one = QWidget(Form)
        self.linea_one.setObjectName(u"linea_one")
        self.horizontalLayout_2 = QHBoxLayout(self.linea_one)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_one = QLabel(self.linea_one)
        self.lbl_one.setObjectName(u"lbl_one")

        self.horizontalLayout_2.addWidget(self.lbl_one)

        self.input_one = QLineEdit(self.linea_one)
        self.input_one.setObjectName(u"input_one")

        self.horizontalLayout_2.addWidget(self.input_one)

        self.unit_one = QLabel(self.linea_one)
        self.unit_one.setObjectName(u"unit_one")

        self.horizontalLayout_2.addWidget(self.unit_one)


        self.verticalLayout_2.addWidget(self.linea_one)

        self.line_two = QWidget(Form)
        self.line_two.setObjectName(u"line_two")
        self.horizontalLayout_3 = QHBoxLayout(self.line_two)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_two = QLabel(self.line_two)
        self.lbl_two.setObjectName(u"lbl_two")

        self.horizontalLayout_3.addWidget(self.lbl_two)

        self.input_two = QLineEdit(self.line_two)
        self.input_two.setObjectName(u"input_two")

        self.horizontalLayout_3.addWidget(self.input_two)

        self.unit_two = QLabel(self.line_two)
        self.unit_two.setObjectName(u"unit_two")

        self.horizontalLayout_3.addWidget(self.unit_two)


        self.verticalLayout_2.addWidget(self.line_two)

        self.btn_calculate = QPushButton(Form)
        self.btn_calculate.setObjectName(u"btn_calculate")
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_calculate.setFont(font1)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.btn_calculate.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_calculate)

        self.lbl_result = QLabel(Form)
        self.lbl_result.setObjectName(u"lbl_result")
        font2 = QFont()
        font2.setPointSize(20)
        self.lbl_result.setFont(font2)
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_result)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label1.setText(QCoreApplication.translate("Form", u"Ley de Ohm", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"A calcular", None))
        self.radio_voltage.setText(QCoreApplication.translate("Form", u"Voltaje", None))
        self.radio_current.setText(QCoreApplication.translate("Form", u"Corriente", None))
        self.radio_resistence.setText(QCoreApplication.translate("Form", u"Resistencia", None))
        self.lbl_one.setText(QCoreApplication.translate("Form", u"Corriente", None))
        self.unit_one.setText(QCoreApplication.translate("Form", u"A", None))
        self.lbl_two.setText(QCoreApplication.translate("Form", u"Resistencia", None))
        self.unit_two.setText(QCoreApplication.translate("Form", u"\u03a9", None))
        self.btn_calculate.setText(QCoreApplication.translate("Form", u"CALCULAR", None))
        self.lbl_result.setText(QCoreApplication.translate("Form", u"resultado", None))
    # retranslateUi

