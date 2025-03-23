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
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(858, 732)
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
        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")

        self.verticalLayout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.verticalLayout.addWidget(self.btn_delete)


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
        if (self.table_components.rowCount() < 3):
            self.table_components.setRowCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_components.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_components.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_components.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_components.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_components.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_components.setItem(0, 5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_components.setItem(0, 6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_components.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_components.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_components.setItem(1, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_components.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_components.setItem(1, 4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_components.setItem(1, 5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_components.setItem(1, 6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_components.setItem(2, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_components.setItem(2, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_components.setItem(2, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_components.setItem(2, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_components.setItem(2, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_components.setItem(2, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_components.setItem(2, 6, __qtablewidgetitem27)
        self.table_components.setObjectName(u"table_components")
        self.table_components.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_components.setRowCount(3)
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

        self.verticalLayout_7.addWidget(self.lbl_info)


        self.verticalLayout_6.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 858, 30))
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
        self.actionAgregar_componente.setText(QCoreApplication.translate("MainWindow", u"Exportar componente", None))
        self.actionEditar_componente.setText(QCoreApplication.translate("MainWindow", u"Exportar todos", None))
        self.actionAdegar_componente.setText(QCoreApplication.translate("MainWindow", u"Adegar componente", None))
        self.actionEditar_componente_2.setText(QCoreApplication.translate("MainWindow", u"Editar componente", None))
        self.actionEliminar_componente.setText(QCoreApplication.translate("MainWindow", u"Eliminar componente", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionotro.setText(QCoreApplication.translate("MainWindow", u"otro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Store Components", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Agrgear", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.input_search_table.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre, C\u00f3digo", None))
        self.btn_search_table.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.table_components.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_components.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_components.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem3 = self.table_components.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem4 = self.table_components.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem5 = self.table_components.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ubicaci\u00f3n", None));
        ___qtablewidgetitem6 = self.table_components.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));

        __sortingEnabled = self.table_components.isSortingEnabled()
        self.table_components.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.table_components.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem8 = self.table_components.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"R10", None));
        ___qtablewidgetitem9 = self.table_components.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"r10", None));
        ___qtablewidgetitem10 = self.table_components.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem11 = self.table_components.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Resistencia de 10 ohms", None));
        ___qtablewidgetitem12 = self.table_components.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"NA", None));
        ___qtablewidgetitem13 = self.table_components.item(0, 6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Disponible", None));
        ___qtablewidgetitem14 = self.table_components.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"324", None));
        ___qtablewidgetitem15 = self.table_components.item(1, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"bobina 10uH", None));
        ___qtablewidgetitem16 = self.table_components.item(1, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"L10u", None));
        ___qtablewidgetitem17 = self.table_components.item(1, 3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem18 = self.table_components.item(1, 4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Bobina de 10uH", None));
        ___qtablewidgetitem19 = self.table_components.item(1, 5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"NA", None));
        ___qtablewidgetitem20 = self.table_components.item(1, 6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"No disponible", None));
        ___qtablewidgetitem21 = self.table_components.item(2, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"322", None));
        ___qtablewidgetitem22 = self.table_components.item(2, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"PIC16F84A", None));
        ___qtablewidgetitem23 = self.table_components.item(2, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"PIC16F84A", None));
        ___qtablewidgetitem24 = self.table_components.item(2, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem25 = self.table_components.item(2, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Microcontrolador", None));
        ___qtablewidgetitem26 = self.table_components.item(2, 5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Desconocida", None));
        ___qtablewidgetitem27 = self.table_components.item(2, 6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Disponible", None));
        self.table_components.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Listado", None))
        self.input_search_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id / Codigo", None))
        self.btn_search_id.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.edit_name.setText(QCoreApplication.translate("MainWindow", u"PIC", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo:", None))
        self.edit_code.setText(QCoreApplication.translate("MainWindow", u"PIC16F84A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.edit_count.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.edit_description.setPlainText(QCoreApplication.translate("MainWindow", u"descripcion del component", None))
        self.lbl_info.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Componente", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEdici_n.setTitle(QCoreApplication.translate("MainWindow", u"Edici\u00f3n", None))
    # retranslateUi

