---
title: 13 Archivos
---

![banner](assets/banner.png)

# 13. Archivos

El manejo de archivos en Python es algo nativo, es decir, por default te da una utileria para comenzar a trabajar con ellos. Esto significa que podemos abrir y leer el contenido de un archivo plano de una manera muy sencilla y rapida.

## Función `open()`

Con solo abrir un archivo de Python podemos llamar a la función `open` la cual le indicamos la ruta del archivo que queremos abrir y cargar su información, junto con el modo en que lo vamos a utilizar.

**Sintaxis:**

```python
    open(nombre_archivo,modo,encoding)
```

**parámetros:**

- `nombre_archivo`: Es la ruta del archivo que se va a carga, la ruta puede ser relativa o absoluta
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
- `writelines(lista)`: Escribe varias líneas
- `seek(position)`: Coloca el cursor en esa posicion dentro del archivo.
- `close()`: Cierra el archivo. Esto siempre se debe hacer si se usa el metodo `open()` solo.

> Nota: Contiene mas metodos, ir a la documentacion oficial de [IO](https://docs.python.org/3/library/io.html)

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
mi_archivo.writes(["java\n", "C\n", "JavaScript\n"])

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

```text
    estoy escribiendo el archivo plano

    esto es el manejo de archivos en python
```

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
        # código para manipular el archivo

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

## Ejemplos

1. Crea una función que escriba una lista de nombres en un archivo de texto, uno por línea. Solicitar al usuario uno por uno.
2. Crear archivos dummy con el formato `pdf`, `docx`, `png`. 10 de cada uno.
3. Solicitar las cafificaciones al usuario de la materia de matematica, guardarlos en un archivo con su promedio al final.
4. Crear un archivo CSV con datos dummy, la cantidad es random. ["elemento x", "valor int", "valor float]
5. Crea un archivo HTML, solicita el titulo del sitio. Template base HTML:

## Módulo `os`

El módulo `os` permite administrar archivos y carpetas (verificar, eliminar, mover, etc.).

```python
import os

os.remove("archivo.txt")           # Eliminar archivo
os.listdir("carpeta/")             # Listar archivos
os.mkdir("nueva_carpeta")          # Crear carpeta
os.makedirs("documentos/proyectos/python")                      # se usa para crear carpetas (directorios) en el sistema de archivos, incluyendo todas las subcarpetas intermedias necesarias.
os.rename(viejo, nuevo)            # Renombrar archivo
os.getcwd()                        # Obtener directorio actual
os.path.exists(ruta)               # Verifica si existe
os.path.isfile(ruta)               # Verifica si es archivo
os.path.isdir(ruta)                # Verifica si es directorio
os.path.join(ruta1, ruta2, ...)  # Une rutas correctamente
os.path.basename(ruta)            # Nombre del archivo
os.path.dirname(ruta)             # Directorio contenedor
os.path.split(ruta)               # Divide en directorio y archivo
os.path.splitext(ruta)            # Divide nombre y extensión
os.path.abspath(ruta)             # Ruta absoluta
```

**Ejemplos**

```python
import os
## verificar si existe el archivo
if os.path.exists('saludo.txt'):
    print("El archivo existe.")
else:
    print("El archivo no existe.")

# Crea un nuevo directorio. Lanza un error si ya existe.
if not os.path.exists('mi_carpeta'):
    os.mkdir('mi_carpeta')

# Elimina un archivo. Lanza un FileNotFoundError si no existe.
os.remove('archivo_a_eliminar.txt')

# Elimina un directorio vacío. Lanza un OSError si no está vacío.
os.rmdir('carpeta_vacia')

# Obtener información del archivo
if os.path.isfile('documento.txt'):
    tamaño = os.path.getsize('documento.txt')
    print(f"Tamaño: {tamaño} bytes")

# Listar archivos en un directorio
archivos = os.listdir('.')
for archivo in archivos:
    if archivo.endswith('.txt'):
        print(archivo)

# Renombrar un archivo
if os.path.exists('viejo.txt'):
    os.rename('viejo.txt', 'nuevo.txt')

# Eliminar un archivo
if os.path.exists('temporal.txt'):
    os.remove('temporal.txt')

# Construir rutas de forma segura
ruta = os.path.join('carpeta', 'subcarpeta', 'archivo.txt')
print(ruta)  # carpeta/subcarpeta/archivo.txt (o \ en Windows)

# Extraer componentes de una ruta
ruta_completa = '/home/usuario/documentos/informe.txt'
directorio = os.path.dirname(ruta_completa)
nombre_archivo = os.path.basename(ruta_completa)
print(f"Directorio: {directorio}")
print(f"Archivo: {nombre_archivo}")

# Separar nombre y extensión
nombre, extension = os.path.splitext('documento.txt')
print(f"Nombre: {nombre}, Extensión: {extension}")

# Obtener ruta absoluta
ruta_relativa = 'datos.txt'
ruta_absoluta = os.path.abspath(ruta_relativa)
print(f"Ruta absoluta: {ruta_absoluta}")

# No lanza error si las carpetas ya existen
os.makedirs("proyectos/python/ejemplo", exist_ok=True)
```

## Módulo `pathlib`

`pathlib` es una forma más moderna y orientada a objetos de trabajar con rutas de archivos. Es más intuitiva que os.path y se recomienda para código nuevo.

**Sintaxis**

```python
from pathlib import Path

Path(ruta)                  # Crear objeto Path
path.exists()               # Verificar existencia
path.is_file()              # Es archivo?
path.is_dir()               # Es directorio?
path.read_text()            # Leer texto
path.write_text(texto)      # Escribir texto
path.name                   # Nombre del archivo
path.stem                   # Nombre sin extensión
path.suffix                 # Extensión
path.parent                 # Directorio padre
```

**Ejemplos**

```python
from pathlib import Path

# Crear objeto Path
archivo = Path('datos.txt')

# Verificar existencia
if archivo.exists():
    print("El archivo existe")

# Leer archivo (forma simple)
contenido = archivo.read_text(encoding='utf-8')
print(contenido)

# Escribir archivo (forma simple)
archivo.write_text("Hola mundo\n", encoding='utf-8')

# Trabajar con componentes de ruta
archivo = Path('carpeta/subcarpeta/documento.txt')
print(f"Nombre completo: {archivo.name}")
print(f"Nombre sin extensión: {archivo.stem}")
print(f"Extensión: {archivo.suffix}")
print(f"Directorio padre: {archivo.parent}")

# Construir rutas
carpeta = Path('documentos')
archivo = carpeta / 'informe.txt'  # Operador / para unir rutas
print(archivo)

# Iterar sobre archivos en un directorio
directorio = Path('.')
for archivo in directorio.iterdir():
    if archivo.is_file() and archivo.suffix == '.txt':
        print(archivo.name)

# Crear directorios
nueva_carpeta = Path('nueva/carpeta/anidada')
nueva_carpeta.mkdir(parents=True, exist_ok=True)

# Renombrar
viejo = Path('viejo.txt')
if viejo.exists():
    viejo.rename('nuevo.txt')

# Eliminar archivo
archivo = Path('temporal.txt')
if archivo.exists():
    archivo.unlink()

# Obtener todos los archivos .txt recursivamente
for archivo_txt in Path('.').rglob('*.txt'):
    print(archivo_txt)
```

## Módulo `shutil`

Proporciona operaciones de alto nivel para copiar y mover archivos y directorios completos.

**Sintaxis**

```python
import shutil

shutil.copy(origen, destino)      # Copiar archivo
shutil.copy2(origen, destino)     # Copiar con metadatos
shutil.move(origen, destino)      # Mover/renombrar
shutil.copytree(origen, destino)  # Copiar directorio completo
shutil.rmtree(directorio)         # Eliminar directorio y contenido
```

Ejemplo

```python
import shutil
import os

# Copiar un archivo
if os.path.exists('original.txt'):
    shutil.copy('original.txt', 'copia.txt')
    print("Archivo copiado")

# Copiar preservando metadatos (fecha de modificación, etc.)
shutil.copy2('original.txt', 'copia_con_metadatos.txt')

# Mover un archivo
shutil.move('archivo.txt', 'nueva_carpeta/archivo.txt')

# Copiar un directorio completo
if os.path.isdir('carpeta_origen'):
    shutil.copytree('carpeta_origen', 'carpeta_destino')

# Eliminar un directorio y todo su contenido
if os.path.isdir('carpeta_temporal'):
    shutil.rmtree('carpeta_temporal')

# Crear un backup
shutil.copy('importante.txt', 'importante_backup.txt')
```

## Módulo `csv`

El formato CSV (Comma-Separated Values) se usa para almacenar datos tabulares (como hojas de cálculo).
El módulo `csv` simplifica la lectura y escritura de archivos en formato de valores separados por comas. Te ahorra la molestia de parsear las cadenas de texto manualmente.

**Sintaxis**

```python
import csv

# Leer CSV
csv.reader(archivo, delimiter=',')
csv.DictReader(archivo)

# Escribir CSV
csv.writer(archivo, delimiter=',')
csv.DictWriter(archivo, fieldnames)
```
**Ejemplo**

```python
import csv

# Escribir
with open("datos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Ana", 25])

# Leer
with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

```python
import csv

# Leer CSV como lista de listas
with open('datos.csv', 'r', encoding='utf-8') as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)  # Cada fila es una lista

# Leer CSV como lista de diccionarios
with open('datos.csv', 'r', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila)  # Cada fila es un diccionario
        print(f"Nombre: {fila['nombre']}, Edad: {fila['edad']}")

# Escribir CSV desde listas
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', 25, 'Madrid'],
    ['Luis', 30, 'Barcelona']
]
with open('salida.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerows(datos)

# Escribir CSV desde diccionarios
datos_dict = [
    {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'},
    {'nombre': 'Luis', 'edad': 30, 'ciudad': 'Barcelona'}
]
with open('salida_dict.csv', 'w', newline='', encoding='utf-8') as f:
    campos = ['nombre', 'edad', 'ciudad']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()  # Escribir encabezados
    escritor.writerows(datos_dict)

# Leer CSV con delimitador diferente
with open('datos.tsv', 'r', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter='\t')
    for fila in lector:
        print(fila)
```

## Módulo `json`

El formato JSON (JavaScript Object Notation) se usa para intercambiar datos entre programas.
El módulo `json` (JavaScript Object Notation) es la forma estándar de intercambiar datos estructurados. Te permite convertir diccionarios y listas de Python a cadenas de texto JSON y viceversa, lo que es ideal para guardar y cargar configuraciones o información compleja.

**Sintaxis**

```python
import json

json.dump(diccionario, archivo)   # Escribir objeto a archivo
json.dumps(objeto)                # Convertir objeto a string JSON
json.load(archivo)                # Leer archivo JSON a objeto
json.loads(string)                # Convertir string JSON a objeto
```

**Ejemplo**

```python
import json

# Escribir datos a JSON
datos = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'México',
    'hobbies': ['lectura', 'música', 'deportes']
}

with open('datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)

# Leer datos desde JSON
with open('datos.json', 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)
    print(datos_leidos)
    print(f"Nombre: {datos_leidos['nombre']}")

# Convertir objeto Python a string JSON
persona = {'nombre': 'María', 'edad': 25}
json_string = json.dumps(persona, indent=2)
print(json_string)

# Convertir string JSON a objeto Python
json_texto = '{"nombre": "Pedro", "edad": 35}'
objeto = json.loads(json_texto)
print(objeto['nombre'])

# Escribir lista de diccionarios
usuarios = [
    {'id': 1, 'nombre': 'Ana'},
    {'id': 2, 'nombre': 'Luis'},
    {'id': 3, 'nombre': 'Carmen'}
]

with open('usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(usuarios, f, indent=2, ensure_ascii=False)
```

---
Realizado por el Instructor: [Alejandro Leyva](https://www.alejandro-leyva.com/)
