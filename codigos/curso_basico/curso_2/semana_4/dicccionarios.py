alumno1 = {
    "name": "Adrian",
    "especialidad": ["torno", "programador", "fiestas"],
    "edad": 22
}

alumno2 = {
    "name": "Miguel",
    "especialidad": ["Cncista", "programar"],
    "edad": 28
    }

nombre1 = alumno2["name"] # pasamos key
edad = alumno2["edad"]
especialidades = alumno2["especialidad"]
especialidad = especialidades[1]

print(nombre1)
print(edad)
print(especialidad)

for especialidad in alumno1["especialidad"]:
    print(f'El alumno {alumno1["name"]} es especialista en {especialidad}')

print(alumno1)


nombre2 = alumno1.get("name")##me devuelve el valor con esa llave
nombre3 = alumno1["name"]
print(nombre2)
print(nombre3)

for llave in alumno1.keys():
    #print(llave)
    print(f"La llave: '{llave}' tiene el valor: {alumno1[llave]}")
    
for llave in alumno2.keys():
    #print(llave)
    print(f"La llave: '{llave}' tiene el valor: {alumno2[llave]}")

print( type([1,2]) == list )

name = ""
edad = 0
especialidades = "especialista en "
for llave in alumno1.keys():
    if type(alumno1[llave]) == list: 
        for  esp in alumno1[llave]:
            especialidades += esp +", "

print(especialidades[:-2])

## sacando todo los datos

for linea in alumno2.items():
    print(linea)

for llave,_ in alumno2.items():
    print(f"{llave} - ")
    
for valor in alumno1.values():
    print(valor)

completo_alumno = {
    "materias": {
        "materia_1": "Matematicas",
        "materia_2": "fisica"
        }
    }
print(completo_alumno)

alumno1.update(completo_alumno)
print(alumno1)