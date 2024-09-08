---
title: 8 Estructuras de repetición
---

![banner](assets/banner.png)

# 8 Estructuras de repetición

## 8.1 Estructura de repetición `while`

Dentro de la programación tenemos estructuras de control para repetir acciones. Hay 2 estructuras que podemos utilizar, los ciclos son `while`,  `for`; este ultimo se verá en otro capitulo.

### 8.1.1 Estructura `while`

La sintaxis de la estructura `while` es muy sencilla; es la siguiente:

```python
while condicion_verdadera:
    línea de código
    línea de código
    línea de código
    ...
```

La forma de leerla es: **mientras la condición se cumpla seguirá dentro del ciclo**.

*Lo que tiene esta estructura es que al momento de preguntar por primera vez, sino cumple la condición no entra al ciclo.*

#### Ejemplos

1. **Vamos a imprimir 10 números, desde el 0 al 9, en cada vuelta del ciclo debemos tener una variable que nos ayude a saber cuando hayamos terminado.**

```python
contador = 0 # declaro mi variable auxiliar "contador"

while contador < 10:
    print(contador)         # imprimir el valor del contador
    contador = contador + 1 # incremento al contador

print("El ciclo termino")

```

```text
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    El ciclo termino
```

2. **Imprimir la tabla del 7, que vaya desde el 1 al 10.**

```python
tabla = 7
contador = 1

while contador <= 10:
    print(tabla * contador)
    contador += 1
```

```text
    7
    14
    21
    28
    35
    42
    49
    56
    63
    70
```

3. **solicitar al usuario 10 números e indicar si es par o impar**

```python
contador = 1

print("Par o Impar")

while contador <= 10:
    numero = int(input("Dar valor " + str(contador) + ": "))

    if numero % 2 == 0:
        print("El valor " + str(numero) + " es par")
    else:
        print("El valor " + str(numero) + " es impar")
    print("-------------------------------------------")

    contador +=1
```

```text
    Par o Impar
    Dar valor 1: 5
    El valor 5 es impar
    -------------------------------------------
    Dar valor 2: 6
    El valor 6 es par
    -------------------------------------------
    Dar valor 3: 5
    El valor 5 es impar
    -------------------------------------------
    Dar valor 4: 5
    El valor 5 es impar
    -------------------------------------------
    Dar valor 5: 6
    El valor 6 es par
    -------------------------------------------
    Dar valor 6: 5
    El valor 5 es impar
    -------------------------------------------
    Dar valor 7: 5
    El valor 5 es impar
    -------------------------------------------
    Dar valor 8: 8
    El valor 8 es par
    -------------------------------------------
    Dar valor 9: 6
    El valor 6 es par
    -------------------------------------------
    Dar valor 10: 6
    El valor 6 es par
    -------------------------------------------
```

4. **Solicitar las 3 calificaciones de materia e imprimir su promedio con la frase de "Aprobo" o "Reprobo" dependiendo el caso**

```python
print("Calculadora de promedio final")

suma = 0 # guarda la suma de los parciales
calificaciones = 1 # variable que lleva el coteo

while calificaciones <= 3:
    calificacion = int( input("Dar calificacion " + str(calificaciones) + ": ") )
    suma += calificacion
    calificaciones += 1

promedio = suma / 3

if(promedio < 6 ):
    print("No has aprobado, tu promedio es " + str(promedio))
else:
    print("Has aprobado, tu promedio es " + str(promedio))
```

5. **Reaizar una calculadora para sumar y restar, pero hasta que el usuario de la opcion de salir el programa terminará**

```python
opcion = 0

while opcion != 3:
    print("-------------------------------------")
    print("Calculadora Suma y Resta")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La suma es: " + str(valor1 + valor2))
    elif opcion == 2:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La resta es: " + str(valor1 - valor2))
    elif opcion > 3 or opcion < 1:
        print("La opcion no existe")

print("Programa a finalizado")

```

```text
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    3
    Programa a finalizado
```

#### Ejercicios

1. Imprimir la tabla del 8, del 1 al 10, con el siguiente formato "8 x 1 = 8"
2. Realizar un programa que solicite 10 números e imprima si es par o impar y si es mayor a 10 que lo indique, de lo contrario solo dice "es impar"
5. Realizar un programa solicite los 3 parciales de Matemáticas, e imprimir el promedio, pero si reprueba, ahora tendrá que pedir el resultado de su extra, en caso que haya pasado el extra, le dará su calificación final y le dirá "aprobado". En caso que no apruebe su extra, solo le dirá "estas en recursamiento"

### 8.1.2 Continue y Break

Existen 2 palabras reservadas que nos ayudan a un control mas complejo dentro de los ciclos, que son `break` y `continue`.

- La palabra reservada `break` me sirve para romper un ciclo cuando yo no necesite, muy util en ciclos infinitos que necesitemos `romper`.
- La palabra reservada `continue` me sirve para ignorar el código restante e iniciar la siguiente vuelta del ciclo.

```python
# Vamos a hacer un ciclo infinito el cual vamos a romper cuando una condicion se cumpla

contador = 0

while True: # ciclo infinito
    print('El valor del contador es: ' + str(contador))
    contador+=1

    if contador == 5: # en el momento que esta condicion se cumple entra y encuentra break
        print("Se rompe el ciclo en el valor " + str(contador))
        break   # cuando se ejecute esta linea el ciclo termina
```

```text
    El valor del contador es: 0
    El valor del contador es: 1
    El valor del contador es: 2
    El valor del contador es: 3
    El valor del contador es: 4
    Se rompe el ciclo en el valor 5
```

```python
# vamos a hacer que el ciclo ignore todo el código que tiene por debajo cuando encuentre la palabra continue

contador = 0

while contador < 5:
    contador+=1

    if contador == 3:
        continue
    print(f"El valor del contador es: {contador}")

```

```text
    El valor del contador es: 1
    El valor del contador es: 2
    El valor del contador es: 4
    El valor del contador es: 5
```

```python
# Realizar una calculadora que sume y reste, mostrando un menu indicando las opciones,
# Debe tener la opcion de salir, en caso que ingrese una opcion que no existe,
# mandar el mensaje de que la opcion no es valida. El programa termina cuando el usuario
# ingresa la opcion de salir, de lo contrario debe seguir mostrando el menu con las opciones
while True:
    print("-------------------------------------")
    print("Calculadora Suma y Resta")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        suma = valor1 + valo2
        print("La suma es: " + str(suma))
    elif opcion == 2:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La resta es: " + str(valor1 - valor2))
    elif opcion == 3:
        print("Programa a finalizado")
        break
    else:
        print("La opcion no existe")
```

```text
    -------------------------------------
    Calculadora Suma y Resta
    1. Suma
    2. Resta
    3. Salir
    3
    Programa a finalizado
```

## 8.2 Estructura de repetición `for`

La siguiente estructura de control se llama `for`. Esta estructura tiene un comportamiento similar a `while`. En esencial hace lo mismo, repite hasta un limite pero este se da distinto. `For each`.

**Sintaxis:**

```python
for variable in iterador :
    código a ejecutar
    código a ejecutar
    código a ejecutar
    ...
```

### Función `range()`

La función `range()` retorna un secuencia de números, comenzando por default en 0 e incrementando en 1, y se detiene antes del número especificado.

#### Sintaxis

```python
range(start, stop, step)
```

#### Parámetros

- `start`: (*opcional*). Un numero entero específicamente para la posición inicial, por default es 0
- `stop`: (Requerido). Un numero entero que especifica en donde se detendrá.
- `step`: (*opcional*). Un numero entero que especifica el incremento. Por default es 1.

Esta función se utiliza con el ciclo `for`

```python
#Vamos a imprimir 10 números, del 0 al 9, recordemos que el número que le pasamos es el tope y ese no se imprime,
#y el valor inicial por default es 0, el incremento es de 1 en 1

for valor in range(10):
    print(f'el valor actual es: "{valor}"')

```

```text
    el valor actual es: "0"
    el valor actual es: "1"
    el valor actual es: "2"
    el valor actual es: "3"
    el valor actual es: "4"
    el valor actual es: "5"
    el valor actual es: "6"
    el valor actual es: "7"
    el valor actual es: "8"
    el valor actual es: "9"
```

```python
# Ahora vamos a imprimir en un rango, entonces se le pasa el inicio y el fin,
# comenzando en 2 y terminando en 11

for valor in range(2,12):
    print(f'el valor actual es: "{valor}"')
```

```text
    el valor actual es: "2"
    el valor actual es: "3"
    el valor actual es: "4"
    el valor actual es: "5"
    el valor actual es: "6"
    el valor actual es: "7"
    el valor actual es: "8"
    el valor actual es: "9"
    el valor actual es: "10"
    el valor actual es: "11"
```

```python
# Ahora vamos a imprimir en un rango, entonces se le pasa el inicio y el fin,
# comenzando en 1 y terminando en 20, de 2 en 2

for valor in range(3,22,2):
    print(valor)
```

```text
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
```

> 📝 Nota: Cuando queramos ya sea comenzar en un numero distinto, o cero con un incremento diferente se tiene que pasar el valor de incremento forzosamente*

#### Ejemplos

##### 1. Solicitar 3 calificaciones del parcial y calcular el promedio**

```python
suma = 0.0

for calificacion in range(3):
    suma += float(input(f"Dar el parcial {calificacion + 1}: "))

print(f"El promedio es {suma / 3}")
```

```text
    Dar el parcial 1: 10
    Dar el parcial 2: 8
    Dar el parcial 3: 7
    El promedio es 8.333333333333334
```

**2. Imprimir la tabla del 7 con el formato "7 x 10 = 70", comenzando en 7x1 y terminando ene 7x10. Utilizando la estructura for y la función range()**

```python
tabla = 7

for contador in range(1,11):
    resultado = tabla * contador
    print( str(tabla) + " x " + str(contador) + " = " +  str(resultado) )

```

```text
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70
```

### Break y Continue

La palabra reservada **break** y **continue** también sirve en el ciclo *for*

```python
for v in range(10):
    print(v)

    if v == 3:
        break
```

```text
    0
    1
    2
    3
```

```python
mensaje = "Lo mejor del mundo es saber programar"

for letra in mensaje:
    print(letra)
```

```text
    L
    o

    m
    e
    j
    o
    r

    d
    e
    l

    m
    u
    n
    d
    o

    e
    s

    s
    a
    b
    e
    r

    p
    r
    o
    g
    r
    a
    m
    a
    r
```

```python
#Comparativa entre el for vs while
# imprimir del  0 al 9

print('Con FOR')

for contador in range(0,10):
    print(contador)

print('---------------')

print('Con WHILE')

contador = 0

while contador < 10:
    print(contador)
    contador += 1
```
```text
    Con FOR
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    ---------------
    Con WHILE
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
```

**Ejercicio:**

1. Recorre un rango del 0 al 10 e indicar cuales son par e impar
2. Recorre un rango del 5 al 32 e indicar los que sean múltiplos de 5
3. Solicitarle al usuario que tabla desea imprimir, indicando desde donde comienza y donde termina
4. Calcular el promedio de la sumatoria de los números pares desde el 2 hasta el 200

---

Realizado por el Instructor: [Alejandro Leyva](https://www.alejandro-leyva.com/)
