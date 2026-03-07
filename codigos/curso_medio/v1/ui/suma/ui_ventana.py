# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Sumador(object):
    def setupUi(self, Sumador):
        if not Sumador.objectName():
            Sumador.setObjectName(u"Sumador")
        Sumador.resize(413, 332)
        self.verticalLayout = QVBoxLayout(Sumador)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Sumador)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.input_1 = QLineEdit(Sumador)
        self.input_1.setObjectName(u"input_1")

        self.verticalLayout.addWidget(self.input_1)

        self.input_2 = QLineEdit(Sumador)
        self.input_2.setObjectName(u"input_2")

        self.verticalLayout.addWidget(self.input_2)

        self.btn_sumar = QPushButton(Sumador)
        self.btn_sumar.setObjectName(u"btn_sumar")
        font1 = QFont()
        font1.setPointSize(18)
        self.btn_sumar.setFont(font1)

        self.verticalLayout.addWidget(self.btn_sumar)

        self.lbl_resultado = QLabel(Sumador)
        self.lbl_resultado.setObjectName(u"lbl_resultado")
        font2 = QFont()
        font2.setPointSize(20)
        self.lbl_resultado.setFont(font2)
        self.lbl_resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_resultado)


        self.retranslateUi(Sumador)

        QMetaObject.connectSlotsByName(Sumador)
    # setupUi

    def retranslateUi(self, Sumador):
        Sumador.setWindowTitle(QCoreApplication.translate("Sumador", u"Form", None))
        self.label.setText(QCoreApplication.translate("Sumador", u"Calculadora", None))
        self.btn_sumar.setText(QCoreApplication.translate("Sumador", u"Sumar", None))
        self.lbl_resultado.setText(QCoreApplication.translate("Sumador", u"resultado", None))
    # retranslateUi

