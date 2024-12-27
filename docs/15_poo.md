---
title: 15. Programación Orientada a Objetos
---

![banner](assets/banner.png)

# 15. Programación Orientada a Objetos

## Introducción a la Programación Orientada a Objetos

La programación orienta a objetos es un paradigma de programación, lo cual esta enfocado en la abstracción del mundo real a código de programación; es decir, es una representación de las cosas del mundo en un archivo con código, el cual tiene los atributos y comportamientos.

>Los programas se construyen a partir de definiciones de objetos y definiciones de funciones; la mayoría de los cómputos se hacen con base en objetos.
>Cada definición de objetos corresponde a algún concepto o cosa del mundo real, y las funciones que operan sobre esos objetos corresponden a las maneras en que los conceptos o cosas reales interactúan

### Clase

**Clase** se le denomina a un archivo que tiene la definición de nuestro objeto o clase.

>La clase es donde se declaran los atributos y métodos.

![objetos](assets/objetos.png)

### Atributos y Comportamientos

Las clases contienen sus atributos y sus métodos (*no siempre es necesario que los tenga*).

![objetos](assets/atributos_comportamiento.png)

### ¿Qué es un atributo?

Es un **campo** o **propiedad** que se declara en la clase; es decir, que tiene el objeto, por ejemplo, `cantidadPuertas = 4`, indicamos el numero de puertas de nuestra clase `Carro`.

### ¿Qué es un método?

- Es un **comportamiento** (acción) que realiza un objeto (cosa).
- Una secuencia de pasos ordenados.s
- Es un bloque o secuencia de código que se repite continuamente.
- Hace una sola tarea, y lo hace muy bien.
- Su nombre se define con un verbo (acción).
- Funciones de un objeto.
- Modifica estados.

**Los métodos son como las funciones**, pero con dos diferencias:

- Los métodos se definen adentro de una definición de clase, a fin de marcar explícitamente la relación entre la clase y éstos.
- La sintaxis para llamar o invocar un método es distinta que para las funciones.

### Instancia

Una instancia es la creación o invocación de un objeto; es decir, después de crear la clase podemos crear una instancia (objeto) para después, ser usado. Es como en el ejemplo del auto, primer fue diseñado y después, fue construido en una fabrica para ser usado.

![instancia](assets/instancias.png)

### *self*

Al momento de crear una clase se debe ocupar la palabra reservada `self`, la cual indica o hace referencia a la propia clase; indica que el método o campo de la propia clase. Siempre se debe usar dentro de una clase, fuera de ella no funciona.

## Codeando

### Creando una clase

**Creando una clase vacía.** Se usa una palabra reservada `class` el nombre de la clase (*usando la convención CamelCase*) y termina con dos puntos; colocamos `pass` con su respectiva indentation, para que la clase quede vacía sin declaración de métodos y campos.

```python
class MyCar:
    pass
```

### Agregando campos a la clase

La declaración de campos globales, es lo mismo que estuviéramos declarando variables convencionales, sin embargo, estas solo pertenecen a la clase.

```python
class MyCar:

    color = "Blue"
    on = False

```

### Agregando métodos a la clase

Se declara con la palabra reservada `def`, al igual que cualquier funcional, pero dentro de una clase los métodos deben recibir como primer argumento **siempre** la palabra `self`, esto indica que pertenece a la clase.

```python
class Car:
    color = "Blue"
    on = False

    def sayName(self):
        print("A car")
```

### Creando una instancia (objeto)

Para crear una instancia se debe escribir el mismo nombre de la clase y agregar paréntesis (muy similar a llamar una función)

Para acceder a los campos y métodos de una clase se hace con la notación de punto; `<instancia>`**.**`<campo>` o `<instancia>`**.**`<método>()`

```python
class Car:
    color = "Blue"
    on = False

    def sayName(self):
        print("A car")



car = Car()         # se crea la instancia
print(car.color)    # se invoca un campo de la instancia
print(car.on)       # se invoca un campo de la instancia
car.sayName()       # se invoca un método de la instancia
```

```text
    Blue
    False
    A car
```

### Utilizando los campos dentro de la clase

Si queremos utilizar los campos o métodos de la propia clase, dentro de un método, se debe llamar, colocando primero la palabra `<self>`**.**`<campo>` o `<self>`**.**`<método>()`

```python
class Car:
    color = "Blue"
    on = False

    def sayName(self):
        print("A car")

    def description(self):
        message = f"A car with a color: {self.color} and is turn on: {self.on}"
        return message

    def message(self):
        print("+" * 10)
        print(self.description())
        print("+" * 10)


car = Car()
print(car.color)
print(car.on)
car.sayName()
print(car.description())
car.message()
```

```text
    Blue
    False
    A car
    A car with a color: Blue and is turn on: False
    ++++++++++
    A car with a color: Blue and is turn on: False
    ++++++++++
```

### Ejemplos

### Ejercicios

---

Referencia: <https://docs.python.org/es/3/tutorial/classes.html>
