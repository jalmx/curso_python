---
title: 12 Funciones
---

![banner](assets/banner.png)

# 12. Funciones

Bloque de código reutilizable que puede ser llamado n cantidad de veces, debe ser corta,  hacer una sola cosa (resuelve un problema) y hacerla bien.

## Como se nombran las funciones (Buenas practicas)

- El nombre es una `acción` es decir un verbo
- El nombre debe ser en minúsculas
- No tiene espacios el nombre, por lo tanto, son `separados por guion bajo(_)`

## Como escribo una función y como la utilizo

**Sintaxis**

```python
def name_function():
    #body function
    #code block
    #code block
    #code block
    #code block
```

Cómo la llamo a la función:

```python
name_function()
```

```python
def elevar_cuadrado():
    '''Esta función eleva al cuadrado el numero 2'''
    cuadrado = 2 ** 2
    print(cuadrado)


def saludar():
    '''
    Esta función manda un saludo
    '''
    print('Hola a todos!!! xD')

saludar()
elevar_cuadrado()
```

```text
    Hola a todos!!! xD
    4
```

### Ejercicios

1. Realizar una función que en su cuerpo realice la suma de dos números (estos están dados por ustedes), e imprimir el resultado, es decir, cuando se invoque

2. Realizar una función que en su cuerpo realice la impresión de 3 mensajes, los que ustedes quieran, y al invocarla que salgan esos mensajes

## Funciones con parámetros

Las funciones en ocasiones necesitan parámetros para funcionar y poder realizar la acción.

Parámetro = Argumento = variable

### Cómo escribo una función y cómo la utilizo

#### Sintaxis

```python
def name_function(argumeto1, argumentos2, ..., argumentosN):
    #body function
    #code block
    #code block
    #code block
    #code block
```

Como la llamo a la función, coloco su nombre, abro parentesis y coloco los argumentos que necesita:

```python
name_function(arg1, arg2...)
```

```python
# base ^ potencia   -> 2^3 = 8

def potencia(base:float, potencia:int):
    resultado = base ** potencia
    print(f'{base} elevado a la {potencia} es: {resultado}')


def saludo2(nombre:str):
    '''Función que imprime un mensaje personalizado'''
    print(f'Hola {nombre}, que chido es conocerte!!!')

saludo2('Axel')
saludo2('Melani')
saludo2('David')
saludo2('Raul')

potencia(2,3)
potencia(3,3)

```

```text
Hola Axel, que chido es conocerte!!!
Hola Melani, que chido es conocerte!!!
Hola David, que chido es conocerte!!!
Hola Raul, que chido es conocerte!!!
2 elevado a la 3 es: 8
3 elevado a la 3 es: 27
```

**Ejercicios:**

1. Realizar una función que realice el calculo del area del circulo, la función recibe el radio. Ocupando las funciones de la libreria `math`.

2. Realizar una función que reciba el nombre y la edad, y que imprima un mensaje con estos datos, ejemplo: "Hola 'alejandro'  que buena onda que tengas '20' anios"

## Funciones con parámetros por default u opcionales

Las funciones en ocasiones necesitan parámetros para funcionar, pero no es necesario pasarle todos los parámetros requeridos, dado que pueden ser opcionales y poder realizar la acción.

Parametro = Argumento = variable

### Como escribo una función y como la utilizo

#### Sintaxis

```python
def name_function(argumeto1=valor, argumentos2=valor, ..., argumentosN=valorN):
    #body function
    #code block
    #code block
    #code block
    #code block
```

*Como la llamo a la funcion, coloco su nombre, abro parentesis y coloco los argumentos que necesita:*

```python
name_function(arg1, ... [arg2])
```

```python
def saludo3(nombre:str = 'Desconocido'):
    '''Función que imprime un mensaje personalizado'''
    print(f'Hola {nombre}, que chido es conocerte!!!')

def potencia2(base=1, potencia = 2):
    '''Por default eleva al cuadrado la base'''
    resultado = pow(base, potencia)
    print(resultado)

def imprimir_0_10(tope=10):
    print('--------------------')
    for i in range(tope+1):
        print(i)
    print('--------------------')

saludo3()
saludo3('Ricardo')

potencia2()
potencia2(3)
potencia2(3,3)
potencia2(3,4)

imprimir_0_10(1)
```

```text
Hola Desconocido, que chido es conocerte!!!
Hola Ricardo, que chido es conocerte!!!
1
9
27
81
--------------------
0
1
--------------------
```

**Ejercicios:**

1. Crear una función que reciba la edad, pero la edad es opcion, por default que tenga el valor de 15, y que mande a imprimir si es menor o mayor de edad, pero si es 15, que imprima también, la frase "Creo que no me pasaste la edad, tramposo!"
2. Crear una función que calcule el area de cuadrados y rectangulos, la función recibe 2 parámetros, la base y la altura, pero cuando es cuadrado solo recibe uno, por lo tanto, el segundo parámetros es opcional, el segundo parámetros por default es 0.

## Retornado valores de una funcion

En ocasiones necesitamos que la función nos devuelva informacion, es decir, que realice la operacion y nos devuelva ese resultado, para ello ocupamos la palabra reservada `return`. El valor que devuelve normalmente lo debemos guardar.

**Como escribo una función y como la utilizo**

**Sintaxis**

```python
def name_function([argumeto1, argumentos2=valor, ..., argumentosN]):
    #body function
    #code block
    #code block
    #code block
    #code block
    return valor
```

*Como la llamo a la función, coloco su nombre, abro parentesis y coloco los argumentos que necesita y ese resultado lo guardamos en una variable:*

```python
resultado = name_function([arg1, ... arg2])
```

```python
from math import pi

def mensaje_perzonalizado(nombre:str):
    mensaje = f'Que onda {nombre}!!, la estamos pasando chido!!!'

    return mensaje

def area_triangulo(base, altura):
    area = (base * altura) /2
    return area

mensaje = mensaje_perzonalizado('Pricila')

print(mensaje)

mensaje += ' vamos por la coca'
print(mensaje)

area_t = area_triangulo(3,7)
print(f'El area del triangulo es: {area_t}')
```

    Que onda Pricila!!, la estamos pasando chido!!!
    Que onda Pricila!!, la estamos pasando chido!!! vamos por la coca
    El area del triangulo es: 10.5

```python
def operaciones_circulo(radio, area='area'):
    '''
    Esta función realiza la operación del area o perímetro
    en función de la variable area
    '''
    if area == 'area':
        return pi * pow(radio,2)
    else:
        return 2 * pi * radio

print(f"El area es {operaciones_circulo(5,'area')}")
print(f'El perimetro es {operaciones_circulo(5,"perimetro")}')
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipykernel_24695/2679705058.py in <module>
          9         return 2 * pi * radio
         10
    ---> 11 print(f"El area es {operaciones_circulo(5,'area')}")
         12 print(f'El perimetro es {operaciones_circulo(5,"perimetro")}')


    /tmp/ipykernel_24695/2679705058.py in operaciones_circulo(radio, area)
          5     '''
          6     if area == 'area':
    ----> 7         return pi * pow(radio,2)
          8     else:
          9         return 2 * pi * radio


    NameError: name 'pi' is not defined

**Ejercicios:**

1. Crear una función que calcule el promedio, pasandole los 3 parciales y te devuelve el resultado. Despues indicar si aprobo o esta en recursa.
2. Crear las funciones de ley de ohm, una que calcule resistencia, corriente y otra voltaje, pasando el parametro necesario: Ejemplo de aplicacion:
    - r = resistencia(10, 0.5)
    - i = corriente(10, 1000)
    - r = voltaje(10, 5)

## Funciones con parámetros nombrados

Normalmente pasamos argumentos a las funciones con un orden orden establecido, y el orden que le coloco el programador, pero hay una forma de poder los argumentos en un orden cual sea, pero se debe especificar que argumento es.

*Nota: Los parámetros nombrados y también con valores por default van al final se colocan al final*

Como escribo una función y como la utilizo.

**Sintaxis**

```python
def name_function(variable1, variable2 = 'str'):
    #body function
    #code block
    #code block
    #code block
    #code block
    return valor
```

Como la llamo a la funcion, coloco su nombre, abro parentesis y coloco los argumentos que necesita indicando su nombre con su valor, sin importar el orden:

```python
name_function(variable2='pokemon', variable1=10)
```

```python
def create_pokemon(name = 'unknown', power=0):
    pokemon = f'Mi pokemo se llama {name} con un poder de {power}'
    return pokemon

print( create_pokemon(power=25, name='pikachu'))
```

    Mi pokemo se llama pikachu con un poder de 25

## Recibiendo n argumentos

### Argumentos Posicionales Variables `*args`

El operador `*args` (el asterisco es lo importante, "args" es solo una convención de nombre) permite que una función acepte cualquier número de argumentos posicionales.

Cuando usas `*args` en la definición de una función:

- Python recolecta todos los argumentos posicionales extra que se pasan en la llamada.
- Los empaqueta en una tupla.
- Asigna esa tupla al nombre de la variable que sigue al asterisco (args).

**Sintaxis:**

```python
def name_funcion(*arg):
    # code

def name_funcion(arg1, *arg):
    # code
```

**Ejemplo**

```python
def sumar_todos(*numeros):
    """Suma una cantidad variable de números."""
    total = 0
    for num in numeros:
        total += num
    return total

# Llamadas con diferentes números de argumentos
resultado1 = sumar_todos(10, 5, 2)
resultado2 = sumar_todos(1, 1, 1, 1, 1, 10)
resultado3 = sumar_todos() # También funciona con cero argumentos

print(f"Suma 1: {resultado1}") # Output: Suma 1: 17
print(f"Suma 2: {resultado2}") # Output: Suma 2: 15
```

### Argumentos de Palabra Clave Variables: `**kwargs`

El operador `**kwargs` (los dos asteriscos son lo importante, "kwargs" viene de *keyword arguments*) permite que una función acepte cualquier número de argumentos de palabra clave.

Cuando usas `**kwargs` en la definición de una función:

- Python recolecta todos los argumentos de palabra clave extra (los que tienen la forma clave=valor) que se pasan en la llamada.
- Los empaqueta en un diccionario.
- Asigna ese diccionario al nombre de la variable que sigue a los dos asteriscos (kwargs).

**Sintaxis:**

```python
def name_funcion(**kwarg):
    # code

def name_funcion(arg1, **kwarg):
    # code
```

**Ejemplo**

```python
def crear_perfil(nombre, **opciones):
    """Crea un perfil, aceptando datos adicionales opcionales."""
    perfil = {'Nombre': nombre}
    perfil.update(opciones)
    return perfil

# Llamadas con diferentes argumentos de palabra clave
perfil1 = crear_perfil("Elena", edad=30, ciudad="Bogotá")
perfil2 = crear_perfil("Javier", idioma="Inglés")
perfil3 = crear_perfil("Sofía")

print("\n--- Perfil 1 ---")
print(perfil1) # Output: {'Nombre': 'Elena', 'edad': 30, 'ciudad': 'Bogotá'}

print("\n--- Perfil 2 ---")
print(perfil2) # Output: {'Nombre': 'Javier', 'idioma': 'Inglés'}
```

### Combinando `*args` y `**kwargs`

Puedes combinar argumentos fijos, `*args`, y `**kwargs` en la misma función, pero el orden es **estricto y muy importante**:

- Argumentos Posicionales Fijos (requeridos)
- `*args` (argumentos posicionales variables)
- Argumentos de Palabra Clave Fijos (opcionales o con valor por defecto)
- `**kwargs` (argumentos de palabra clave variables)

**Sintaxis:**

```python
def name_function(arg_fijo, *args, arg_clave='default', **kwargs):
    pass
```

**Ejemplo**

```python
def configurar_juego(nombre_juego, *jugadores, dificultad='Normal', **opciones_extra):
    print(f"Juego: {nombre_juego}")
    print(f"Jugadores: {jugadores}") # Tupla
    print(f"Dificultad Fija: {dificultad}")
    print(f"Opciones Extra: {opciones_extra}") # Diccionario

configurar_juego(
    "D&D",
    "Pedro", "Laura", "Marta",           # -> *jugadores (tupla)
    dificultad="Difícil",               # -> argumento de palabra clave fijo
    mapa="Bosque", música=True, dados=20  # -> **opciones_extra (diccionario)
)
```

## Devolviendo *n* valores

En Python, cuando una función usa múltiples expresiones de retorno separadas por comas, realmente está devolviendo una tupla que contiene todos esos valores. Esto permite que la función actúe como si estuviera retornando varios resultados individuales.

**Sintaxis:**

```python
def my_funcion(*arg):
    # code
    #
    return valueA, valueB,...

# Recibiendo los datos

a, b = my_funcion() # se colocan las variables separadas por coma y en el orden que seran recibidas
_, b = my_funcion() # en este caso el primer valor no lo usaramos, pero el segundo si lo guardamos en `b`, el guion bajo se usa para indicar que ese valor no lo guardaremos
a = my_funcion()  # si solo coloco una variable, solo guardamos ese valor, los demas que esten adelante se pierden
```

**Ejemplo**

```python
def calcular_operaciones(a, b):
    """Devuelve la suma, la resta y la multiplicación de dos números."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    return suma, resta, multiplicacion

# Desempaquetado: Se asigna cada elemento de la tupla de retorno a su variable correspondiente.
s, r, m = calcular_operaciones(10, 5)

print(f"Suma: {s}")             # Output: Suma: 15
print(f"Resta: {r}")            # Output: Resta: 5
print(f"Multiplicación: {m}")   # Output: Multiplicación: 50
```

---

Realizado por el Instructor: [Alejandro Leyva](https://www.alejandro-leyva.com/)
