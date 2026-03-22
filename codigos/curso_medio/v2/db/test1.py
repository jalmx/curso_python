from peewee import SqliteDatabase, Model, CharField, IntegerField

# crea un coneccion a mi db
db = SqliteDatabase("base_datos.db")

#Tabla

class Usuario(Model):
    nombre = CharField(max_length=255) #string 
    email = CharField(max_length=20, unique=True)
    edad = IntegerField()

    class Meta:
        database = db


#crear la tabla
db.connect()
# db.create_tables([Usuario])

# for i in range(5):
#     Usuario.create(nombre=f"Rafa{i}", email=f"rafa{i}@email.com")

usuarios = Usuario.select() ## trae los registros de la db

for u in usuarios:
    print(f"{u.nombre} - {u.email}")

print("*********************************")

user = Usuario.get(Usuario.nombre == "RaIntegerFieldfa3")
user.email = "nuevo@email.com"
user.save()

usuarios = Usuario.select() ## trae los registros de la db

for u in usuarios:
    print(f"{u.nombre} - {u.email}")

print("*********************************")

user = Usuario.get(Usuario.email == "rafa1@email.com")
print(user.nombre)
user.delete_instance()

usuarios = Usuario.select() ## trae los registros de la db

for u in usuarios:
    print(f"{u.nombre} - {u.email}")


## CREAR UNA DB de "mascotas"

## nombre de tabla "mascota"
## campos nombre, raza, edad (IntegerField)

# van a agregar 5 mascostas
# van a mostrar las mascotas

# van a cambiarle la edad a la 4a mascota
# volver a mostar las mascostas

# van a eliminar a la mascota 2 
# volver a mostar las mascostas