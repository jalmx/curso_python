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

Como la llamo a la función:

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

    Hola a todos!!! xD
    4

**Ejercicios:**

1. Realizar una función que en su cuerpo realice la suma de dos números (estos están dados por ustedes), e imprimir el resultado, es decir, cuando se invoque

2. Realizar una función que en su cuerpo realice la impresión de 3 mensajes, los que ustedes quieran, y al invocarla que salgan esos mensajes

## Funciones con parámetros

Las funciones en ocasiones necesitan parámetros para funcionar y poder realizar la acción.

Parámetro = Argumento = variable

**Como escribo una función y como la utilizo**

**Sintaxis**

```python
def name_function(argumeto1, argumentos2, ..., argumentosN):
    #body function
    #code block
    #code block
    #code block
    #code block
```

*Como la llamo a la funcion, coloco su nombre, abro parentesis y coloco los argumentos que necesita:*

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

    Hola Axel, que chido es conocerte!!!
    Hola Melani, que chido es conocerte!!!
    Hola David, que chido es conocerte!!!
    Hola Raul, que chido es conocerte!!!
    2 elevado a la 3 es: 8
    3 elevado a la 3 es: 27

**Ejercicios:**

1. Realizar una función que realice el calculo del area del circulo, la función recibe el radio. Ocupando las funciones de la libreria `math`.

2. Realizar una función que reciba el nombre y la edad, y que imprima un mensaje con estos datos, ejemplo: "Hola 'alejandro'  que buena onda que tengas '20' anios"

## Funciones con parametros por default u opcionales

Las funciones en ocasiones necesitan parametros para funcionar, pero no es necesario pasarle todos los parametros requeridos, dado que pueden ser opcionales y poder realizar la acción.

Parametro = Argumento = variable

**Como escribo una función y como la utilizo**

**Sintaxis**

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

**Ejercicios:**

1. Crear una función que reciba la edad, pero la edad es opcion, por default que tenga el valor de 15, y que mande a imprimir si es menor o mayor de edad, pero si es 15, que imprima también, la frase "Creo que no me pasaste la edad, tramposo!"
2. Crear una función que calcule el area de cuadrados y rectangulos, la función recibe 2 parametros, la base y la altura, pero cuando es cuadrado solo recibe uno, por lo tanto, el segundo parametros es opcional, el segundo parametros por default es 0.

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

## Funciones con parametros nombrados

Normalmente pasamos argumentos a las funciones con un orden orden establecido, y el orden que le coloco el programador, pero hay una forma de poder los argumentos en un orden cual sea, pero se debe especificar que argumento es.

*Nota: Los parametros nombrados y también con valores por default van al final se colocan al final*

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

## Devolviendo varios valores

<!-- TODO: pendiente -->

---

Realizado por el Instructor: [Alejandro Leyva](https://www.alejandro-leyva.com/)
