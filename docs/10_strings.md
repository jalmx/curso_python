---
title: 10 Strings
---

![banner](assets/banner.png)

# 10. Strings `str`

En esta sección veremos con mas detalle la manipulación de [strings](https://www.w3schools.com/python/python_ref_string.asp).
La manipulación de string a detalle es sumamente util para separarlo, saber si contiene alguna letra, palabra u oración. Recordemos que todo en python es un objeto y al ser un objeto contienen por default muchos métodos con los cuales podemos operar ese `string`.

## 10.1 Convertir a minúsculas (lower)

Una función que nos facilita es convertir todo el string a minúsculas. Ignora simbolos y números.

- lower(): Converts a string into lower case

```python
# Todas la letras las pasara a minúsculas

mensaje = "Hola Como ESTAS"
minuscula = mensaje.lower()

print(mensaje)
print(minuscula)
```

```text
    Hola Como ESTAS
    hola como estas
```

## 10.2 Convertir a Mayúsculas (upper)

Una función que nos facilita es convertir todo el string a mayúsculas. Ignora símbolos y números.

- upper(): Converts a string into upper case

```python
# Todas la letras las pasara a mayúsculas

mensaje = "Hola Como ESTAS"
upper = mensaje.upper()

print(mensaje)
print(upper)
```

```text
    Hola Como ESTAS
    HOLA COMO ESTAS
```

## 10.3 Convertir a Mayúsculas (capitalize)

Una función que nos facilita es convertir solo la primer letra a mayúsculas, el resto a minúsculas. Esto es útil para cuando queremos que una oración inicie en mayúsculas o palabra. Ignora símbolos y números.

- `capitalize()`: Converts the first character to upper case

```python
# Todas la letras las pasara a mayúsculas

mensaje = "hola cOMO ESTAS"
capital = mensaje.capitalize()

print(mensaje)
print(capital)
```

```text
    hola cOMO ESTAS
    Hola como estas
```

## 10.4 Contador de palabras (count)

Los string cuenta con método el cual nos ayuda directamente a saber cuantas veces se encuentra una palabra dentro de ese string, debe ser igual la palabra a la que se le paso.

- count(value, start, end): method returns the number of times a specified value appears in the string

**parámetros:**

- `value`: Required. A String. The string to value to search for
- `start`: Optional. An Integer. The position to start the search. Default is 0
- `end`: Optional. An Integer. The position to end the search. Default is the end of the string

```python
phrase = "Ingeniería en Sistemas es lo mejor del mundo, tienes el mundo en tus manos"
count = phrase.count("mundo")
print(f'Veces que sale la palabra \"mundo\" es: {count}')
```

```text
    Veces que sale la palabra "mundo" es: 2
```

## 10.5 Es o no es un

En ocasiones queremos conocer si un string es o esta en cierta forma.

- `isdigit()`: Returns True if all characters in the string are digits
- `islower()`: Returns True if all characters in the string are lower case
- `isnumeric()`: Returns True if all characters in the string are numeric
- `isspace()`: Returns True if all characters in the string are whitespaces
- `isupper()`: Returns True if all characters in the string are upper case

```python
print(f'Es un número: {"4".isdigit()}')
print(f'Es un número: {"4".isnumeric()}')
print(f'Esta en minúsculas: {"hola".islower()}')
print(f'Esta en mayúsculas: {"HOLA".isupper()}')
print(f'Son espacios: {" ".isspace()}')
```

```text
    Es un número: True
    Es un número: True
    Esta en minúsculas: True
    Esta en mayúsculas: True
    Son espacios: True
```

- `endswith(value)` Returns true if the string ends with the specified value
- `title()` Converts the first character of each word to upper case
- `find()` Searches the string for a specified value and returns the position of where it was found
- `index()` Searches the string for a specified value and returns the position of where it was found
- `format()` Formats specified values in a string
- `join()` Joins the elements of an iterable to the end of the string
- `lstrip()` Returns a left trim version of the string
- `replace()` Returns a string where a specified value is replaced with a specified value
- `rfind()` Searches the string for a specified value and returns the last position of where it was found
- `rindex()` Searches the string for a specified value and returns the last position of where it was found
- `rsplit()` Splits the string at the specified separator, and returns a list
- `rstrip()` Returns a right trim version of the string
- `split()` Splits the string at the specified separator, and returns a list
- `splitlines()` Splits the string at line breaks and returns a list
- `startswith()` Returns true if the string starts with the specified value
- `strip()` Returns a trimmed version of the string

<https://www.w3schools.com/python/python_ref_string.asp>

---

Realizado por el Instructor: [Alejandro Leyva](https://www.alejandro-leyva.com/)
