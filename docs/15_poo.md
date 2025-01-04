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

## POO

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

![call method](assets/call_method.png)

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

Crear una clase, con las siguientes indicaciones, después crear una instancia, llamar sus campos y métodos

#### Ejemplo 1

- **Clase:** Auto
- **Atributos**:
    - noPuertas: int
    - kilometraje: float
- **Comportamientos**:
  - acelerar(): void
  - arrancar(): void

### Ejercicios

Crear una clase, con las siguientes indicaciones, después crear una instancia, llamar sus campos y métodos

#### Ejercicio 1

- **Clase:** Persona
- **Atributos:**
    - nombre: String
    - edad: int
- **Métodos:**
    - saludar(): void
    - decir_edad(): void

#### Ejercicio 2

- **Clase:** Perro
- **Atributos:**
    - nombre  : String
    - raza : String
- **Métodos:**
    - ladrar():  void
    - correr(int velocidad):  void
    - jugar():  String : (pelota, hueso, chancla)

### Niveles de acceso (Encapsulamiento)

En Python, los niveles de acceso no son tan estrictos como en otros lenguajes orientados a objetos como Java o C#. Python implementa un sistema basado en **convenciones** y no en **restricciones estrictas**.

Los niveles de acceso son:

- **public**
- **protected**
- **private**

#### Público (public)

Los atributos y métodos públicos son accesibles desde cualquier parte del código. En Python, por defecto, todo es público.

```python
class Persona:

    nombre = "Juan"

    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")


persona = Persona()
print(persona.nombre)  # Acceso directo
persona.saludar()      # Acceso directo
```

#### Protegido (\_) (protected)

Los atributos y métodos protegidos se indican con un guion bajo al principio del nombre (`_nombre`). Esto es solo una convención, y se espera que los desarrolladores no accedan a ellos directamente fuera de la clase o de sus subclases. Sin embargo, técnicamente siguen siendo accesibles.

```python
class Persona:

    _nombre = "Mario"  # Protegido

    def _saludar(self):  # Método protegido
        print(f"Hola, soy {self._nombre} (protegido)")


persona = Persona()
print(persona._nombre)  # Accesible, aunque no recomendado
persona._saludar()      # Accesible, aunque no recomendado

```

#### Privado (__doble_guion_bajo)

Los atributos y métodos privados se indican con dos guiones bajos al principio del nombre (`__nombre`).

```python
class Persona:

    __nombre = "Juan"  # Privado

    def __saludar(self):  # Método privado
        print(f"Hola, soy {self.__nombre} (privado)")

    def mostrar_nombre(self):  # Método público para acceder a __nombre
        print(self.__nombre)



persona = Persona()
persona.mostrar_nombre()  # Acceso indirecto
print(persona.__nombre)  # Error: AttributeError
persona.__saludar()     # Error: AttributeError

```

- **Convención vs Restricción**: En Python, `_` y `__` son más sobre cómo comunicar la intención de acceso que sobre evitarlo estrictamente.
- Usa `__` para datos que realmente necesitan ser privados y protegidos contra modificaciones accidentales.
- Usa `_` para señalar que un atributo o método es solo para uso interno.

### Constructor

Un constructor es un método especial en una clase que se llama automáticamente cuando se crea una nueva instancia de esa clase. En Python, el constructor se define mediante el método especial `__init__`.

El Constructor en Python

Un constructor es un método especial en una clase que se llama automáticamente cuando se crea una nueva instancia de esa clase. En Python, el constructor se define mediante el método especial **init**.

#### Características del Constructor

- **Inicialización Automática**: Se ejecuta al crear una instancia de la clase.
- **Propósito principal**: Inicializar atributos de la instancia con valores específicos o predeterminados.

```python
class Clase:
    def __init__(self, parametros):
        # Inicialización de atributos

```

- Es un método mágico (o dunder, por "double underscore").
- Se utiliza para inicializar atributos de la clase.
- Es opcional. Si no defines un constructor, Python utiliza un constructor por defecto que no realiza ninguna acción específica.
- Parámetro `self`:
    - Representa la instancia actual de la clase.
    - Es obligatorio en los métodos de instancia, incluyendo `__init__`.
    - Permite acceder y modificar los atributos de la instancia.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear una instancia
persona = Persona("Juan", 30)
persona.mostrar_informacion()  # Salida: Nombre: Juan, Edad: 30

```

#### Tipos de Constructores

**Constructor por Defecto**: No acepta parámetros más allá de `self`.

```python
class Persona:
    def __init__(self):
        self.nombre = "Desconocido"
        self.edad = 0


persona = Persona()
print(persona.nombre)  # Desconocido

```

**Constructor con Parámetros:** Acepta parámetros para inicializar atributos.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Persona("María", 25)
print(persona.nombre)  #  María
```

Constructor Flexible (con **valores predeterminados**):

```python
class Persona:
    def __init__(self, nombre="Anónimo", edad=18):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona()
persona2 = Persona("Luis", 40)
print(persona1.nombre)  # Anónimo
print(persona2.nombre)  # Luis

```

**Sobrecarga de Constructores**: Python no soporta sobrecarga de constructores directamente. Puedes simularla utilizando valores predeterminados o lógica dentro del constructor.

```python
class Persona:

    def __init__(self, nombre=None, edad=None):
        if nombre is None and (edad is None or edad == 0):
            self.nombre = "Desconocido"
            self.edad = 0
        elif edad is None:
            self.nombre = nombre
            self.edad = 0
        elif nombre is None:
            self.nombre = "Desconocido"
            self.edad = edad
        else:
            self.nombre = nombre
            self.edad = edad


persona1 = Persona()
persona2 = Persona("Luis")
persona3 = Persona("Ana", 30)
persona4 = Persona(edad=30)
print(persona1.nombre, persona1.edad)  # Desconocido 0
print(persona2.nombre, persona2.edad)  # Luis 0
print(persona3.nombre, persona3.edad)  # Ana 30
print(persona4.nombre, persona4.edad)  # Desconocido 30

```

##### Buenas Prácticas

- Define los atributos claramente dentro del constructor.
- Valida los parámetros para evitar inconsistencias en los objetos.
- Utiliza `__init__` únicamente para inicializar atributos. Evita realizar lógica compleja.
- Documenta el constructor con docstrings para explicar los parámetros.

#### Ejemplo 2

- Un constructor que inicializa los atributos `nombre` y `edad` de una clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")



persona = Persona("Carlos", 25)
persona.mostrar_informacion()

```

#### Ejemplo 3

- El constructor asigna valores predeterminados si no se pasan argumentos.

- **Clase:** Auto
- **Constructor**: tipo: str, marca: str
- **Atributos**:
    - tipo: -str
    - marca: -str
- **Comportamientos**:
  - mostrar_informacion(): void

```python
class Auto:
    def __init__(self, tipo="Coche", marca="Genérica"):
        self.tipo = tipo
        self.marca = marca

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}, Marca: {self.marca}")


auto1 = Auto()
auto2 = Auto("Moto", "Yamaha")
auto1.mostrar_informacion()
auto2.mostrar_informacion()

```

#### Ejercicio 3

- **Clase:** Libro
- **Constructor**: titulo, auto, publicacion
- **Atributos**:
    Título : -str
    Autor : -str
    Año de publicación: -str
- **Comportamientos**:
  - mostrar_informacion():+ void

#### Ejercicio 4

- **Clase:** Circulo
- **Constructor**: radio
- **Atributos**:
    radio : -float
- **Comportamientos**:
  - get_area(): + float
  - get_perimetro(): + float
  - mostrar_datos(): + void

<!-- TODO: SETTER Y GETTER PENDIENTES -->

## Mini proyecto


---

Referencia: <https://docs.python.org/es/3/tutorial/classes.html>
