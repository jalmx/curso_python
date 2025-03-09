---
title: 17. GUI con QT
---

![banner](assets/banner.png)

# 17. GUI con QT

Las **interfaces gráficas de usuario** (GUI, por sus siglas en inglés) son esenciales en el desarrollo de aplicaciones modernas. A diferencia de las aplicaciones de línea de comandos, las GUI proporcionan una experiencia más interactiva, intuitiva y accesible para los usuarios, lo que las convierte en la elección ideal para aplicaciones que buscan un público amplio.

## ¿Qué es una GUI?

Una `GUI` es el medio visual e interactivo a través del cual los usuarios se comunican con un sistema o aplicación. Utiliza elementos como ventanas, botones, menús, y cuadros de texto para que los usuarios puedan interactuar sin necesidad de conocer comandos específicos. Por ejemplo, aplicaciones como navegadores web, editores de texto y reproductores multimedia son ejemplos de programas que utilizan interfaces gráficas.

## Ventajas y Desventajas de las GUI

### Ventajas

- Facilidad de uso
    - Las interfaces gráficas son más intuitivas, especialmente para usuarios sin experiencia técnica.
- Experiencia interactiva
    - Permiten arrastrar, soltar, hacer clic y otras acciones directas que enriquecen la interacción.
- Atractivo visual
    - Una GUI bien diseñada puede ser estéticamente agradable y reforzar la identidad de una marca.
- Accesibilidad
    - Las GUI hacen que las aplicaciones sean accesibles a una audiencia más amplia.

### Desventajas

- Mayor complejidad en el desarrollo
    - Diseñar y programar una GUI requiere más tiempo y recursos que desarrollar una aplicación de línea de comandos.
- Uso de recursos
    - Las GUI suelen consumir más memoria y potencia de procesamiento.
- Mantenimiento complicado
    - Modificar o actualizar una GUI puede ser más difícil si no está bien diseñada desde el principio.

## PyQt y Qt: Diseño de Interfaces Gráficas en Python

**Qt** es un framework muy popular para el desarrollo de interfaces gráficas multiplataforma. Ofrece un conjunto completo de herramientas para crear aplicaciones con una apariencia profesional y moderna. PyQt es una biblioteca de Python que actúa como un puente para interactuar con el framework Qt, permitiendo a los desarrolladores trabajar en Python en lugar de C++ (el lenguaje nativo de Qt).

### ¿Por qué usar PyQt?

- Multiplataforma
    - Las aplicaciones creadas con PyQt pueden ejecutarse en Windows, macOS y Linux sin cambios en el código.
- Potencia y flexibilidad
    - Combina las capacidades de Qt con la simplicidad de Python.
- Documentación robusta
    - Qt y PyQt cuentan con una amplia documentación y una comunidad activa.
- Diseño visual
    - Incluye herramientas como Qt Designer, que permiten crear interfaces gráficas mediante un editor visual.

### Qt Designer y PyQt

Qt Designer es una herramienta gráfica que facilita el diseño de interfaces gráficas sin necesidad de escribir código. La interfaz se diseña visualmente y se guarda en archivos `.ui`, que luego pueden ser integrados con código Python utilizando herramientas como `pyuic`.

#### Ventajas de PyQt

- Reducción del tiempo de desarrollo gracias a las herramientas visuales.
- Soporte para una amplia variedad de elementos de interfaz.
- Integración con otros módulos de Python para tareas complejas.

#### Desventajas de PyQt

- La licencia de PyQt puede ser restrictiva para proyectos comerciales, a diferencia de PySide, que también utiliza Qt.
- Dependencia de bibliotecas externas, lo que puede incrementar el tamaño de la aplicación.

## Preparando entorno para crear GUI

### Instalando `PySide6`

Se debe instalar el modulo de `PySide6` o `PyQt6`, pero nos enfocaremos en el primero.

```bash
pip install PySide6
```

`PySide6` es un tipo de meta paquete que contiene todo lo necesario para trabar interfaz gráfica de QT.

> Nota: Lo recomendable es crear un entorno virtual

### QT Designer

Una vez se tiene instalado el metapaquete de PySide6, se descarga la aplicación que podemos usar para la creación y edición de nuestra interfaz gráfica; el cual es `Qt Designer`.
El comando para ejecutarlo es;
nos lanzara en automático la aplicación para crear nuestra aplicación.:

```bash
pyside6-designer
```

![qt designer](assets/qt_designer_1.png)

Elegimos la opción de `Main Window` o `Ventana principal`, se creara una ventana base:

![qt designer](assets/qt_designer_2.png)

En ella ya podremos construir la interfaz que queramos para nuestra aplicación.

### Convertir un archivo `ui` a `py`

Podemos trabar con los archivo `.ui` que genera `Qt Designer`, sin embargo; es mas recomendable hacer la conversion del archivo, para ello se usa el comando `pyside6-uic` el cual viene dentro del mega paquete de PySide6.

La forma de implementarlo es la siguiente:

```bash
pyside6-uic your_file.ui -o ui_your_file.py
```

### Ejecutando nuestra ventana

Tenemos que crear nuestro archivo principal donde mandamos a llamar a la ventana que hicimos.

`main.py`

```python
import sys  # importo el modulo del sistema para pasar los argumentos a la aplicación
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)  # se deben traer los módulos para crear el contexto de la aplicación

from ui_main_window import Ui_MainWindow


class MiVentanaPrincipal(QMainWindow, Ui_MainWindow):

    # Esta clase me sirve para crear toda la interacción con la ventana, las acciones de los botones, textos, todos los widgets, también se pueden agregar por código lo que sea necesario

    def __init__(self):
        super().__init__()  # inicializo el constructor padre QMainWindow
        self.setupUi(self)  # inicializo mi ventana que viene de Ui_MainWindow


if __name__ == "__main__":

    app = QApplication(sys.argv)    # creo el contexto de la aplicación
    window = MiVentanaPrincipal()   # creo la instancia de mi ventana
    window.show()                   # muestro la ventana
    app.exec()                      # ejecuto la aplicación
```

Archivo `py` generado a partir del archivo `ui`, usando `pyside6-uic`;

> Nota: Este código es autogenerado, no se debe editar, lo que se modifica es el archivo ui.

Archivo: `ui_main.py`

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
```

## Widgets

## Label (Etiquetas) QLabel

La etiqueta nos ayuda a mostrar texto en la GUI.
La etiqueta se encuentra en la sección de `Display Widgets`, como se ve en la imagen

![label 1](assets/label_0.png)

Aquí podemos encontrar las etiquetas que nos sirven para colocar texto dentro de la aplicación.

![label 1](assets/label_1.png)

Damos click sobre el `widget` y lo colocamos sobre la ventana.

![label 1](assets/label_2.png)

### Código

Con botones podemos dar interactividad al usuario para realizar acciones.
La etiqueta se encuentra en la sección de `Buttons`, como se ve en la imagen:

![btn](assets/btn_1.png)

Aquí podemos varios tipos de botones, por el momento nos enfocamos en el primero.

![btn](assets/btn_2.png)

Damos click sobre el `widget` y lo colocamos sobre la ventana.

![btn](assets/btn_3.png)

```python
from PySide6.QtWidgets import QLabel # importación de modulo que contiene la clase QLabel

label = QLabel('This is a QLabel widget') # Se crea una instancia de QLabel
```

![editline](assets/lineedit_1.png)

![editline](assets/lineedit_2.png)

![editline](assets/lineedit_3.png)

### Métodos

- `setAlignment()`: Aligns the text as per alignment constants
  - `Qt.AlignLeft`
  - `Qt.AlignRight`
  - `Qt.AlignCenter`
  - `Qt.AlignJustify`
- `setIndent()`: Sets the labels text indent
- `setPixmap()`: Displays an image
- `Text()`: Displays the caption of the label
- `setText()`: Programmatically sets the caption
- `selectedText()`: Displays the selected text from the label (The textInteractionFlag must be set to TextSelectableByMouse)
- `setBuddy()`: Associates the label with any input widget
- `setWordWrap()`: Enables or disables wrapping text in the label

Mas información en <https://doc.qt.io/qt-6/qlabel.html>

## Buttons (Botones) QPushButton

### Código

```python
from PySide6.QtWidgets import QPushButton # importación de modulo que contiene la clase QPushButton

button = QPushButton("Download", self) # Se crea una instancia de QPushButton
```

### Métodos

- `setCheckable()`: Recognizes pressed and released states of button if set to true
- `toggle()`: Toggles between checkable states
- `setIcon()`: Shows an icon formed out of pixmap of an image file
- `setEnabled()`: When set to false, the button becomes disabled, hence clicking it doesn't emit a signal
- `isChecked()`: Returns Boolean state of button
- `setDefault()`: Sets the button as default
- `setText()`: Programmatically sets buttons caption
- `text()`: Retrieves buttons caption

## Entra de texto (Line Edit) QLineEdit

Este widget es un elemento para ingresar datos y nosotros podamos tomar ese contenido y procesarlo.

### Código

```python
from PySide6.QtWidgets import QLineEdit # importación de modulo que contiene la clase QLineEdit

line_edit = QLineEdit('Default Value', parent_widget) # Se crea una instancia de QLineEdit
```

### Métodos

- `setAlignment()`: Aligns the text as per alignment Constants
  - `Qt.AlignLeft`
  - `Qt.AlignRight`
  - `Qt.AlignCenter`
  - `Qt.AlignJustify`
- `clear()`: Erases the contents
- `setEchoMode()`: Controls the appearance of the text inside the box. Echomode values are
  - `QLineEdit.`
  - `NormalQLineEdit.`
  - `NoEchoQLineEdit.`
  - `PasswordQLineEdit.`
  - `PasswordEchoOnEdit`
- `setMaxLength()`:Sets the maximum number of characters for input
- `setReadOnly()`: Makes the text box non-editable
- `setText()`: Programmatically sets the text
- `text()`: Retrieves text in the field
- `setValidator()`: Sets the validation rules. Available validators are
  - `QIntValidator`: Restricts input to integer
  - `QDoubleValidator`: Fraction part of number limited to specified decimals
  - `QRegexpValidator`: Checks input against a Regex expression
- `setInputMask()`: Applies mask of combination of characters for input
- `setFont()`: Displays the contents QFont object

## Layouts

- `QHBoxLayout`: Linear horizontal layout
- `QVBoxLayout`: Linear vertical layout
- `QGridLayout`: In indexable grid XxY
- `QStackedLayout`:  Stacked (z) in front of one another

## Signal & Slots (Eventos y Callbacks)

Los `Signal` son la manera de conectar los eventos que se disparan cuando sucede algo con el widget; ejemplo, dar click sobre el elemento, si esto pasa se agrega un `Slot`, que es una función o método en la cual se realizara la acción que hayamos asignado al widget cuando pase este evento.

## Ventanas

### Main Window (Ventana principal)

### Dialog (Ventanas de dialog)

### Ventana genérica (Widget)

## Ejemplos GUI

### Generador de contraseñas

![pass ui](assets/pass_ui.png)

### Segunda ley de Newton

![2a law](assets/app_2a_ley.png)
