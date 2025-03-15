from peewee import SqliteDatabase, Model, CharField

#crea la conexion a la db
db = SqliteDatabase("usuarios.db")

class Usuario(Model):
    nombre = CharField(max_length=100)
    email = CharField(unique=True)

    # Meta clase que sirve para metadatos
    class Meta:
        database = db

if __name__ == "__main__":
    db.connect()
    #db.create_tables([Usuario])
    # print("inicio a insertar")

    # Usuario.create(nombre=f"Axel", email=f"axel@mail.com")

    # print("Leer datos:")
    # usuarios = Usuario.select()

    # for usuario in usuarios:
    #     print(usuario.nombre," <--->" ,usuario.email)

    # usuario = Usuario.get(Usuario.nombre == "Axel")
    # usuario.nombre = "Hiram"
    # usuario.email = "hiram@pollitos.com"
    # usuario.save()

    # usuarios = Usuario.select()
    # for usuario in usuarios:
    #     print(usuario.nombre," <--->" ,usuario.email)
    print("borrando")
    usuario =Usuario.get(Usuario.nombre == "Hiram")
    usuario.delete_instance() #borrara el registro
