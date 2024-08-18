![banner](logo/banner.png)

# Archivos

El manejo de archivos en Python es algo nativo, es decir, por default te da una utileria para comenzar a trabajar con ellos. Esto significa que podemos abrir y leer el contenido de un archivo plano de una manera muy sencilla y rapida.


## Funcion `open()`

Con solo abrir un archivo de Python podemos llamar a la funcion `open` la cual le indicamos la ruta del archivo que queremos abrir y cargar su informacion, junto con el modo en que lo vamos a utilizar.

**Sintaxis:**

```python
    open(ruta_archivo,modo,encoding)
```

**Parametros:**

- `ruta_archivo`: Es la ruta del archivo que se va a carga, la ruta puede ser relativa o absoluta
- `modo`: El modo es como se manejara el archivo, los modos son:
    - `r`: Read - Valor por default. Abre el archivo para leerlo. Lanza error en caso que no exista.
    - `w`: Write - Abre el archivo para leerlo, en caso que no exista lo creara.
    - `a`: Append - Abre el archivo y todo lo que vayamos a escribir se lo agregara.
    - `x`: Create - Crear el archivo, lanza error en caso que exista.
    - `+`: Read-Write - Indica que tenemos el modo lectura y que podemos escribir en él.
    - Modos adicionales:
        - `t`: text (Valor por default)- Indica que el archivo es un texto plano.
        - `b`: binario - Indica que es otro tipo de archivo, ejemplo: imagenes, archivos de word, excel, etc.
- `encoding`: Formato de codificacion de caracteres. Por default no tiene, pero en nuestro caso que hablamos español, es combeniente colocar `utf-8`, con esto identifica acentos y todo lo relacionado al lenguaje.
- **return** `file`: Regresa un Objeto tipo archivo.

[Documentacion open()](https://docs.python.org/3/library/functions.html#open)

### Metodos de los arhivos

Los archivos tiene diversos metodos para manipular su contenido

- `read([count])`: Lee todo el contenido del archivo y lo carga en memoria. Si indicamos el contador, solo lee esa cantidad de caracteres.
- `readline()`: Lee una sola linea del archivo. Por default comienza en la primera.
- `readlines()`: Crea una lista con el contenido de cada linea del archivo.
- `write(data)`: Escribe lo que le pasamos como argumento.
- `seek(position)`: Coloca el cursor en esa posicion dentro del archivo.
- `close()`: Cierra el archivo. Esto siempre se debe hacer si se usa el metodo `open()` solo.

*Nota: Contiene mas metodos, ir a la documentacion oficial de [IO](https://docs.python.org/3/library/io.html)*


```python
# Creando un archivo vacio
file_name = 'archivo.txt'

mi_archivo = open(file_name,'w') #aqui el archivo se crea y esta listo para escribir en él

mi_archivo.close() # tenemos que cerrar el archivo
```


```python
mi_archivo = open(file_name, mode='w+', encoding='utf-8')

mi_archivo.write("estoy escribiendo el archivo plano\n")
mi_archivo.write("esto es el manejo de archivos en python\n")

mi_archivo.close()
```


```python
csv = open('datos.csv', mode='w+', encoding='utf-8')

csv.write('dato1,dato2,dato3\n')
csv.write('dato1,dato2,dato3\n')
csv.write('dato1,dato2,dato3\n')
csv.write('dato1,dato2,dato3\n')

csv.close()
```


```python
archivo = open('archivo.txt', mode='r', encoding='utf-8')

print(archivo.readline())
print(archivo.readline())
```

    estoy escribiendo el archivo plano
    
    esto es el manejo de archivos en python
    


## Bloque `with`

Tenemos una palabra reservada `with` la cual nos facilita abrir un archivo y lo cierra en automatico al salir del bloque. Es decir, `with` toma la gestion de los archivos y nosotros nos enfocamos en utilizar la informacion obtenida de él. Lo mas recomendable es usar la palabra `with` con los archivos.

**Sintaxis:**
```python
    with EXPRESSION as TARGET:
        SUITE
```

```python
    # Aplicado a archivos
    with open('ruta','modo') as nombre_variable:
        # codigo para manipular el archivo

```

Documentacion de [The with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)


```python
with open('datos.csv', mode='r', encoding='utf-8') as archivo_csv:
    for line in archivo_csv.readlines():
        print(line)

```

    dato1,dato2,dato3
    
    dato10,dato20,dato30
    
    dato11,dato21,dato31
    
    dato12,dato22,dato32
    


---
Realizado por Docente: [Alejandro Leyva](https://www.alejandro-leyva.com/)
