# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_add_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.ApplicationModal)
        Form.resize(507, 687)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.input_name = QLineEdit(self.widget)
        self.input_name.setObjectName(u"input_name")

        self.gridLayout.addWidget(self.input_name, 0, 1, 2, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 2, 1)

        self.input_code = QLineEdit(self.widget)
        self.input_code.setObjectName(u"input_code")

        self.gridLayout.addWidget(self.input_code, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.input_count = QSpinBox(self.widget)
        self.input_count.setObjectName(u"input_count")

        self.gridLayout.addWidget(self.input_count, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout.addWidget(self.label_5)

        self.input_description = QPlainTextEdit(self.widget)
        self.input_description.setObjectName(u"input_description")

        self.verticalLayout.addWidget(self.input_description)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Add/Edit", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Code:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Quantity: ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Description", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

