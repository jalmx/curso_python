class Persona:

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def saludar(self):
        print(f"Hola me llamo {self._nombre}")

    def decir_edad(self):
        mensaje = f"Mi edad es {self._edad}"
        print(mensaje)

    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")


if __name__ == "__main__":
    Ismael = Persona(nombre="Ismael", edad=22)
    Carlos = Persona("Carlos", 22)

    Ismael.mostrar_informacion()
    Carlos.mostrar_informacion()
