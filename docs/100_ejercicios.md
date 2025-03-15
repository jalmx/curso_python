---
title: Ejercicios
---

![banner](assets/banner.png)

# Ejercicios

## Básicos

1. Realizar el cálculo del perímetro de un cuadrado, con datos en memoria, e imprimir el resultado
2. Realizar el cálculo del perímetro y area de un rectángulo, solicitando el lado de la figura al usuario, e imprimir el resultado, primero perímetro, y después el area.
3. Realizar el cálculo del area de un cuadrado, solicitando el lado de la figura al usuario, e imprimir el resultado
4. Realizar un programa que realice el cálculo de Fuerza en la segunda Ley de Newton. La formula es ==$Fuerza = masa * aceleración$==. Solicitando al usuario las variables necesarias.
5. Realizar una calculadora que convierta de centímetros a pulgadas, solicitando el dato al usuario, e imprimir el resultado. ==_1 In = 2.54cm_==
6. Convertidor de temperatura de Fahrenheit a Celsius. $C=\frac{5}{9}(F - 32)$

## Decisiones

1. Realizar una calculadora básica, que realice la operación de sumar, restar, multiplicar, dividir. Al comenzar muestre un menu y el usuario elija la opción deseada. Se debe pedir el primer valor y el segundo, con ello realizar la operación
2. Solicitar un número entero al usuario, e imprimir por pantalla si es valor par o impar
3. Hacer una calculadora de áreas geométricas, las opciones son:
    - Área del cuadrado
    - Área del círculo
    - Área del triángulo
    - Con opción de salir del programa y al final imprimir el resultado con la frase "El área del figura nombre de la figura elegida es resultado"

4. Hacer una calculadora de ley de ohms, las opciones son:
    - Calcular resistencia
    - Calcular corriente
    - Calcular voltaje
    - Calcular potencia
    - Con opción de salir del programa y al final debe imprimir el resultado con la frase "El resultado es: XX"

5. Que resuelva una ecuación de segundo orden, aplicando la fórmula general; recuerda que no existen las raíces negativas. Debe entregarle los valores de las raíces o en caso que alguna o ninguna raíz exista, indicarlo. _==Nota: Debes usar las funciones matemáticas que vienen en el lenguaje==_
6. Realizar una calculadora del Teorema de Pitágoras, el usuario debe elegir, cateto opuesto, adyacente o hipotenusa, salir, que desear calcular. _==Nota: Debes usar las funciones matemáticas que vienen en el lenguaje==_
7. Hacer una caja registradora, que reciba el valor del producto y al final entregue el costo total con IVA y sin IVA; es decir, En total es _\$18.35_ y con IVA son _\$21.28_, recordar que el IVA es del _16%_

## Operadores lógicos

1. Solicitar al usuario su promedio actual, en valor entero, el algoritmo debe tomar la decisión con basé al número ingresado, y dar un mensaje (ver la tabla)

      | Rango de calificación  | Mensaje a imprimir                        |
      | ---------------------- | ----------------------------------------- |
      | 0 a menor que 6        | "lastima margarito"                       |
      | 6 a menor que 7        | "Aplícate"                                |
      | 7 a menor que 8        | "Apenitas y la libraste, metele papí"     |
      | 8 a menor que 9        | "Bastante bien, puedes mejorar"           |
      | 9 a menor que 10       | "muy bien amiguito, te ganaste la cheve!" |
      | Igual a 10             | "Excelente, tu muy bien"                  |
      | Menor a 0 y mayor a 10 | "Calificación no posible"                 |

2. Cálculo de BMI (Indice de Masa Corporal) para peso y altura, indicando cual es tu BMI y en que nivel de obesidad te encuentras (_Ver tabla_). La formula es $BMI = peso (kg) * estatura^2 (cm)$

      | IMC                | Nivel de peso |
      | ------------------ | ------------- |
      | Por debajo de 18.5 | Bajo peso     |
      | 18.5 – 24.9        | Normal        |
      | 25.0 – 29.9        | Sobrepeso     |
      | 30.0 o más         | Obesidad      |

3. Mandar la letra del múltiplo o submultiple correspondiente, es decir, si el usuario ingresa el valor de 1,000, el valor que se debe desplegar por pantalla es la letra "K", si el usuario ingresa el valor de 0.02, se debe desplegar por pantalla la letra "m"

      | Unidad | Símbolo | Rango       |
      | ------ | ------- | ----------- |
      | pico   | p       | $x10^{-12}$ |
      | nano   | n       | $x10^{-}$   |
      | micro  | u       | $x10^{-6}$  |
      | mili   | m       | $x10^{-3}$  |
      | unidad |         |       1     |
      | kilo   | K       | $x10^{3}$   |
      | mega   | M       | $x10^{6}$   |
      | giga   | G       | $x10^{9}$   |

## Ciclos `while` y con `for`

Todos estos ejercicios se debe implementar un ciclo `while` y otro con la version del `for` . No esta permitido hacer uso de las funciones propias del lenguaje que pueden resolver algún problema o alguna parte de el, a menos que lo indique en la instrucción.

1. Imprimir del 1 al 99.
2. Imprimir una tabla de equivalencia de temperaturas de Celsius y Fahrenheit. Desde 0ºC hasta 100ºC. Es decir, 0C -> 32F, 1C -> 33.8F, 2C -> 35.6F ..... 99C -> 210.2, 100C -> 212F
3. Calcular el promedio final, solicita al usuario sus calificaciones parciales una a una, y al final da el mensaje "Aprobado", en caso que haya pasado arriba de 6 y "Estas en repite" si es menor. Considerando que son 3 parciales.
4. Imprimir la tabla del 8, desde ==_8x1=8 hasta 8x10=80_==.
5. Realizar un programa para visualizar la tabla de multiplicar que desee el usuario, el usuario dará el valor para la tabla, la tabla debe de ir desde el 1 hasta el 10, es decir, por ejemplo si da el numero 3, la tabla comienza en _==3x1=3 ... hasta 3x10=30==_
6. Realizar un programa para visualizar la tabla de multiplicar que desee el usuario, el usuario dará el valor para la tabla, también debe dar el limite donde comienza hasta donde termina, es decir, por ejemplo si da el numero 5, comenzando desde _==el 3 hasta el 25, comenzara la tabla 5x3 = 15 ... 5x25=125==_
7. Leer 10 números enteros, solicitando uno a uno al usuario, e imprimir al final cuántos fueron par y cuántos impar.
8. Calcular el factorial de un número entero. Se le solicita al usuario que ingrese un número entero el cuál quiere calcular el factorial del mismo. ==Ejemplo: 5! = 120==
9. Calcular la potencia de un número, solicita al usuario el número que desea elevar y después la base a la cuál lo elevara. Ejemplo: _==2^2= 4, 2^3=8==_
10. Leer 10 números, solicitando uno a uno al usuario, y al final se imprime por pantalla el número más alto ingresado de los 10.
11. Calculadora de la segunda ley de newton. Sale el menú indicando que desea calcular y la opción de salir. Después solicita al usuario los valores que conoce e imprimir el resultado, una vez termina de hacer todas las operaciones, debe regresar al menú inicial, debe existir una opción para terminal el programa, en caso que coloque una opción no existen, debe volver a mostrar el mensaje.
12. Cálculo de la media de un conjunto de datos. Se le pregunta al usuario cuantos números son, comienza a pedirlos uno a uno y al final imprime el resultado de la media de todos los datos.
13. Cálculo de la media de un conjunto de datos positivos. En cada iteración pregunta al usuario si quiere terminar para conocer el resultado o ingresar otro valor. Cuando elija terminar, imprimir el valor total del promedio o media.
14. Realizar un programa que solicite las calificaciones del parcial; es decir, irá pidiendo una a una las calificaciones, y al final que diga si te vas a _recursamiento o no_
15. Algoritmo para convertir número decimal a binario, debe ir mostrando el numero en binario uno a uno, no es todo el numero binario completo, comenzando por el bit mas significativo. Por ejemplo el usuario ingresa el valor de 5, debe imprimir 101. Dado que 5 en binario es 101.
16. Una pastelería nos solicita realizar un programa para una maquina de pastelitos, las opciones son las siguientes

      ![esquema](https://www.alejandro-leyva.com/algoritmos/img/diagra1.svg)

    - Debe ir sumando las opciones que elije que elija el usuario. Pero cada vez que termine de elegir, debe volver a mostrar el menú, hasta que el usuario elija terminar debe imprimir la cantidad total a pagar. El usuario en cualquier momento puede terminar la orden y la maquina debe darle la cantidad a pagar.
    - Por ejemplo, al inicio muestra el menu de pastel, cupcake y salir. Si elije, pastel, ahora le muestra las opciones de chocolate, vainilla, natural y salir, el usuario elije vainilla, y por ultimo elije chispas, debe preguntar si añade algo mas, si es asi, vuelve a mostrar el menu inicial. En caso que elija que ya termino, debe imprimir la cantidad que debe pagar, es decir, (5+1+0.5) "Cantidad a pagar \$6.5".
    - Recuerda el usuario puede salir en cualquier momento y debe recibir la cantidad que debe pagar.
    - Extra:
      - Generar un listado de todo lo que solicito, es decir, generar una especie de ticket y al final dar el valor a pagar

17. Realizar una calculadora de ley de Ohm, al inicio te da el menú para seleccionar que se desea calcular; para terminar el programa se debe dar la opción de salida, si no el programa sigue mostrando el menu inicial, si el usuario ingresa un valor y "no existe en el menu", manda mensaje que la opción no existe y vuelve a mostrar el menu. El resultado lo debe lanzar en el mejor formato, es decir, si el resultado es 1,000 ohms, en pantalla debe salir 1k, si es posible agregar el símbolo de Omega ($\Omega$) para resistencias, de lo contrario colocar la palabra **"Ohms"**. Si el resultado es 0.005A en pantalla debe salir 5mA. El usuario debe ingresar el valor sin redondear, es decir, si son 10mA debe ingresar -> 0.01A, si el valor es 10k$\Omega$ debe ingresar -> 10000.

## POO

### 1. Clase Persona

```text
-------------------
|     Persona     |
-------------------
| - nombre: str   |
| - edad: int     |
-------------------
| + __init__()    |
| + mostrar_info()|
-------------------
```

**Descripción:**

- Crea una clase `Persona` con atributos privados `nombre (str)` y `edad (int)`.
- Implementa un método `__init__` para inicializar los atributos.
- Añade un método `mostrar_info` que imprima el nombre y la edad de la persona.

### 2. Clase Coche

```text
-------------------
|     Coche       |
-------------------
| - marca: str    |
| - modelo: str   |
| - año: int      |
-------------------
| + __init__()    |
| + arrancar()    |
| + detener()     |
-------------------
```

**Descripción:**

- Crea una clase `Coche` con atributos privados marca, modelo y año.
- Implementa un método `__init__` para inicializar los atributos.
- Añade métodos `arrancar` y `detener` que impriman mensajes como "El coche ha arrancado" y "El coche se ha detenido".

### 3. CuentaBancaria

```text
----------------------------
|     CuentaBancaria       |
----------------------------
| - titular: str           |
| - saldo: float           |
----------------------------
| + __init__()             |
| + depositar(monto: float)|
| + retirar(monto: float)  |
| + mostrar_saldo()        |
----------------------------
```

**Descripción:**

- Crea una clase `CuentaBancaria` con atributos privados titular (str) y saldo (float).
- Implementa un método `__init__` para inicializar los atributos.
- Añade métodos `depositar` y `retirar` para modificar el saldo.
- Implementa un método `mostrar_saldo` que imprima el saldo actual.

### 4. Rectángulo

```text
----------------------------
|     Rectangulo           |
----------------------------
| - ancho: float           |
| - alto: float            |
----------------------------
| + __init__()             |
| + calcular_area()        |
| + calcular_perimetro()   |
----------------------------
```

**Descripción:**

- Crea una clase `Rectangulo` con atributos privados ancho y alto.
- Implementa un método `__init__` para inicializar los atributos.
- Añade métodos `calcular_area` y `calcular_perimetro` que devuelvan el área y el perímetro del rectángulo, respectivamente.

### 5. Estudiante

```text
----------------------------
|     Estudiante           |
----------------------------
| - nombre: str            |
| - edad: int              |
| - cursos: list[str]      |
----------------------------
| + __init__()             |
| + inscribir_curso(curso: str)|
| + mostrar_cursos()       |
----------------------------
```

**Descripción:**

- Crea una clase `Estudiante` con atributos privados nombre, edad y cursos (una lista de strings).
- Implementa un método `__init__` para inicializar los atributos.
- Añade un método `inscribir_curso` que permita añadir un curso a la lista.
- Implementa un método `mostrar_cursos` que imprima todos los cursos en los que está inscrito el estudiante.

### Herencia

1. Crea una clase base Animal con un método `hacer_sonido()`, y luego crea dos subclases `Perro` y `Gato` que sobrescriban ese método con sonidos específicos.
2. Define una clase `Vehiculo` con atributos `marca` y `modelo` (son pasados al constructor), y un método `mostrar_info()`. Luego, crea una subclase `Coche` que agregue el atributo puertas. Usa super() para reutilizar el constructor de Vehiculo.
3. Crea una clase `Persona` con atributos `nombre` y `edad`, y un método `saludar()`. Luego, crea una subclase `Empleado` que agregue un atributo `salario` y un método `trabajar()`.
4. Crea una clase `Figura` con un método `area()`. Luego, crea subclases `Cuadrado` y `Círculo` que sobrescriban el método `area()` con las fórmulas correspondientes.
5. Crea una clase `Motor` y una clase `Coche` que contenga un Motor (es decir, que reciba como argumento el constructor). Luego, crea otra clase `Motocicleta` que herede de `Coche` y usa composición para evitar repetir código.

## GUI (Qt)

### Calculadora de la Segunda ley de Newton

Realizar una aplicación visual para el calculo de la segunda ley de Newton.

![2a law](assets/app_2a_ley.png)

### Divisor de tensión

En esta aplicación el objetivo es obtener el voltaje de salida, se debe colocar

- voltaje de entrada
- El valor de R1 en ohms
- El valor de R2 en ohms

![divisor de tension](assets/divisor_app.png)

#### Extras

- **Poder elegir que se desea calcular**, es decir, quiero calcular R1, por ende, los demás datos se deben colocar. Se puede colocar algún widget en el elijamos cual es el datos a calcular, es a libre elección.

### Código de colores

Se debe obtener el valor de la resistencia con base a los colores que se elijan, cada vez que cambien un valor se actualice el resultado de la resistencia.

![código de colores](assets/app_codde_color.png)

#### Extras

- Agregar la opción para que sea elija si es de 4 o 5 bandas
- Crear una app para resistencias SMD
- Indica si al resistencia formada es comercial o no

### Ley de Ohms

Aplicación de calculo de ley de ohms.

![ohm law](assets/ohm_law.png)

![app ohms law](assets/app_ohms_law.png)

#### Extras

- Agregar que se elija el submúltiplo (mili, micro) y múltiplo (kilo, mega) a cada unidad, es decir, `mA`, `kΩ`, `mV`.

### Convertidor de Temperaturas

Celsius - Fahrenheit - Kelvin

### To-do

Un gestor de tareas por hacer,

- Agregar tarea
- Eliminar tarea
- Editar el contenido de la tarea
- Cambiar de estado la tarea
- **Usar una base de datos**

### Estadística inferencial

Se deben poder leer n numero de datos, y generar una salida con los siguientes datos:

- Media
- Moda
- Mediana
- Desviación estándar
- Varianza
