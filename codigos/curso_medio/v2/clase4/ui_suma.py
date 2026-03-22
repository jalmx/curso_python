# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suma.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(457, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Serif"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"JetBrainsMono Nerd Font"])
        font1.setPointSize(20)
        font1.setKerning(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.input1 = QLineEdit(self.centralwidget)
        self.input1.setObjectName(u"input1")
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(12)
        self.input1.setFont(font2)

        self.verticalLayout.addWidget(self.input1)

        self.input2 = QLineEdit(self.centralwidget)
        self.input2.setObjectName(u"input2")
        self.input2.setFont(font2)

        self.verticalLayout.addWidget(self.input2)

        self.btn_sumar = QPushButton(self.centralwidget)
        self.btn_sumar.setObjectName(u"btn_sumar")
        self.btn_sumar.setFont(font2)

        self.verticalLayout.addWidget(self.btn_sumar)

        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        font3 = QFont()
        font3.setFamilies([u"Ubuntu Nerd Font Light"])
        font3.setPointSize(15)
        self.lbl_result.setFont(font3)
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_result)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CALCULADORA", None))
        self.btn_sumar.setText(QCoreApplication.translate("MainWindow", u"SUMAR", None))
        self.lbl_result.setText(QCoreApplication.translate("MainWindow", u"RESULTADO", None))
    # retranslateUi

