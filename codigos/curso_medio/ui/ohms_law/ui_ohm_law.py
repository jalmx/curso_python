# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ohm_law.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_OhmsLawApp(object):
    def setupUi(self, OhmsLawApp):
        if not OhmsLawApp.objectName():
            OhmsLawApp.setObjectName(u"OhmsLawApp")
        OhmsLawApp.resize(471, 408)
        self.verticalLayout = QVBoxLayout(OhmsLawApp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(OhmsLawApp)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(OhmsLawApp)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_voltage = QRadioButton(self.groupBox)
        self.buttonGroup_calculate = QButtonGroup(OhmsLawApp)
        self.buttonGroup_calculate.setObjectName(u"buttonGroup_calculate")
        self.buttonGroup_calculate.addButton(self.radio_voltage)
        self.radio_voltage.setObjectName(u"radio_voltage")
        self.radio_voltage.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_voltage)

        self.radio_current = QRadioButton(self.groupBox)
        self.buttonGroup_calculate.addButton(self.radio_current)
        self.radio_current.setObjectName(u"radio_current")

        self.horizontalLayout.addWidget(self.radio_current)

        self.radio_resistance = QRadioButton(self.groupBox)
        self.buttonGroup_calculate.addButton(self.radio_resistance)
        self.radio_resistance.setObjectName(u"radio_resistance")

        self.horizontalLayout.addWidget(self.radio_resistance)


        self.verticalLayout.addWidget(self.groupBox)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_one = QLabel(OhmsLawApp)
        self.lbl_one.setObjectName(u"lbl_one")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_one)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_one = QLineEdit(OhmsLawApp)
        self.input_one.setObjectName(u"input_one")

        self.horizontalLayout_2.addWidget(self.input_one)

        self.unit_one = QLabel(OhmsLawApp)
        self.unit_one.setObjectName(u"unit_one")
        font1 = QFont()
        font1.setBold(True)
        self.unit_one.setFont(font1)
        self.unit_one.setMargin(4)

        self.horizontalLayout_2.addWidget(self.unit_one)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.lbl_two = QLabel(OhmsLawApp)
        self.lbl_two.setObjectName(u"lbl_two")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_two)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.input_two = QLineEdit(OhmsLawApp)
        self.input_two.setObjectName(u"input_two")

        self.horizontalLayout_3.addWidget(self.input_two)

        self.unit_two = QLabel(OhmsLawApp)
        self.unit_two.setObjectName(u"unit_two")
        self.unit_two.setFont(font1)
        self.unit_two.setMargin(4)

        self.horizontalLayout_3.addWidget(self.unit_two)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.btn_calculate = QPushButton(OhmsLawApp)
        self.btn_calculate.setObjectName(u"btn_calculate")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btn_calculate)


        self.verticalLayout.addLayout(self.formLayout)

        self.lbl_result = QLabel(OhmsLawApp)
        self.lbl_result.setObjectName(u"lbl_result")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.lbl_result.setFont(font2)
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_result)


        self.retranslateUi(OhmsLawApp)

        QMetaObject.connectSlotsByName(OhmsLawApp)
    # setupUi

    def retranslateUi(self, OhmsLawApp):
        OhmsLawApp.setWindowTitle(QCoreApplication.translate("OhmsLawApp", u"App Ohms Law", None))
        self.label.setText(QCoreApplication.translate("OhmsLawApp", u"Ohm Law", None))
        self.groupBox.setTitle(QCoreApplication.translate("OhmsLawApp", u"To calculate", None))
        self.radio_voltage.setText(QCoreApplication.translate("OhmsLawApp", u"Voltage", None))
        self.radio_current.setText(QCoreApplication.translate("OhmsLawApp", u"Current", None))
        self.radio_resistance.setText(QCoreApplication.translate("OhmsLawApp", u"Resistance", None))
        self.lbl_one.setText(QCoreApplication.translate("OhmsLawApp", u"Current", None))
        self.unit_one.setText(QCoreApplication.translate("OhmsLawApp", u"A", None))
        self.lbl_two.setText(QCoreApplication.translate("OhmsLawApp", u"Resistace", None))
        self.unit_two.setText(QCoreApplication.translate("OhmsLawApp", u"O", None))
        self.btn_calculate.setText(QCoreApplication.translate("OhmsLawApp", u"Calculate", None))
        self.lbl_result.setText(QCoreApplication.translate("OhmsLawApp", u"-", None))
    # retranslateUi

