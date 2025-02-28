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
