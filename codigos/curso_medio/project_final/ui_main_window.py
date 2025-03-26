# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 732)
        self.actionAgregar_componente = QAction(MainWindow)
        self.actionAgregar_componente.setObjectName(u"actionAgregar_componente")
        self.actionEditar_componente = QAction(MainWindow)
        self.actionEditar_componente.setObjectName(u"actionEditar_componente")
        self.actionAdegar_componente = QAction(MainWindow)
        self.actionAdegar_componente.setObjectName(u"actionAdegar_componente")
        self.actionEditar_componente_2 = QAction(MainWindow)
        self.actionEditar_componente_2.setObjectName(u"actionEditar_componente_2")
        self.actionEliminar_componente = QAction(MainWindow)
        self.actionEliminar_componente.setObjectName(u"actionEliminar_componente")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionotro = QAction(MainWindow)
        self.actionotro.setObjectName(u"actionotro")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")

        self.verticalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout.addWidget(self.btn_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_search_table = QLineEdit(self.tab)
        self.input_search_table.setObjectName(u"input_search_table")

        self.horizontalLayout.addWidget(self.input_search_table)

        self.btn_search_table = QPushButton(self.tab)
        self.btn_search_table.setObjectName(u"btn_search_table")

        self.horizontalLayout.addWidget(self.btn_search_table)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.table_components = QTableWidget(self.tab)
        if (self.table_components.columnCount() < 7):
            self.table_components.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_components.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_components.setObjectName(u"table_components")
        self.table_components.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_components.setRowCount(0)
        self.table_components.setColumnCount(7)

        self.verticalLayout_3.addWidget(self.table_components)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_search_id = QLineEdit(self.tab_2)
        self.input_search_id.setObjectName(u"input_search_id")

        self.horizontalLayout_2.addWidget(self.input_search_id)

        self.btn_search_id = QPushButton(self.tab_2)
        self.btn_search_id.setObjectName(u"btn_search_id")

        self.horizontalLayout_2.addWidget(self.btn_search_id)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.edit_name = QLineEdit(self.frame)
        self.edit_name.setObjectName(u"edit_name")
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono"])
        self.edit_name.setFont(font2)
        self.edit_name.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edit_name, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.edit_code = QLineEdit(self.frame)
        self.edit_code.setObjectName(u"edit_code")
        self.edit_code.setFont(font2)
        self.edit_code.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edit_code, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.edit_count = QLineEdit(self.frame)
        self.edit_count.setObjectName(u"edit_count")
        self.edit_count.setFont(font2)
        self.edit_count.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edit_count, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_5)

        self.edit_description = QPlainTextEdit(self.frame)
        self.edit_description.setObjectName(u"edit_description")
        self.edit_description.setFont(font2)
        self.edit_description.setReadOnly(True)
        self.edit_description.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.edit_description)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_info = QLabel(self.widget_2)
        self.lbl_info.setObjectName(u"lbl_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_info.sizePolicy().hasHeightForWidth())
        self.lbl_info.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.lbl_info)


        self.verticalLayout_6.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 893, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuEdici_n = QMenu(self.menubar)
        self.menuEdici_n.setObjectName(u"menuEdici_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.input_search_table, self.btn_search_table)
        QWidget.setTabOrder(self.btn_search_table, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.btn_edit)
        QWidget.setTabOrder(self.btn_edit, self.btn_delete)
        QWidget.setTabOrder(self.btn_delete, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.input_search_id)
        QWidget.setTabOrder(self.input_search_id, self.btn_search_id)
        QWidget.setTabOrder(self.btn_search_id, self.edit_code)
        QWidget.setTabOrder(self.edit_code, self.edit_count)
        QWidget.setTabOrder(self.edit_count, self.table_components)
        QWidget.setTabOrder(self.table_components, self.edit_name)
        QWidget.setTabOrder(self.edit_name, self.edit_description)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEdici_n.menuAction())
        self.menuArchivo.addAction(self.actionAgregar_componente)
        self.menuArchivo.addAction(self.actionEditar_componente)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEdici_n.addAction(self.actionAdegar_componente)
        self.menuEdici_n.addAction(self.actionEditar_componente_2)
        self.menuEdici_n.addAction(self.actionEliminar_componente)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App Store Components", None))
        self.actionAgregar_componente.setText(QCoreApplication.translate("MainWindow", u"Export components", None))
        self.actionEditar_componente.setText(QCoreApplication.translate("MainWindow", u"Export all components", None))
        self.actionAdegar_componente.setText(QCoreApplication.translate("MainWindow", u"Add component", None))
        self.actionEditar_componente_2.setText(QCoreApplication.translate("MainWindow", u"Edit component", None))
        self.actionEliminar_componente.setText(QCoreApplication.translate("MainWindow", u"Delete component", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionotro.setText(QCoreApplication.translate("MainWindow", u"otro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Store Components", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.input_search_table.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name, code", None))
        self.btn_search_table.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.table_components.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_components.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table_components.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem3 = self.table_components.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem4 = self.table_components.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem5 = self.table_components.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem6 = self.table_components.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"List", None))
        self.input_search_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id / Code", None))
        self.btn_search_id.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.edit_name.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Code:", None))
        self.edit_code.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.edit_count.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.edit_description.setPlainText("")
        self.lbl_info.setText(QCoreApplication.translate("MainWindow", u"Information:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Component", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdici_n.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

