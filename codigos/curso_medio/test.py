class Persona:

    def __init__(self, nombre=None, edad=None):
        if nombre is None and (edad is None or edad == 0):
            self.nombre = "Desconocido"
            self.edad = 0
        elif edad is None:
            self.nombre = nombre
            self.edad = 0
        elif nombre is None:
            self.nombre = "Desconocido"
            self.edad = edad
        else:
            self.nombre = nombre
            self.edad = edad


persona1 = Persona()
persona2 = Persona("Luis")
persona3 = Persona("Ana", 30)
persona4 = Persona(edad=30)
print(persona1.nombre, persona1.edad)  # Desconocido 0
print(persona2.nombre, persona2.edad)  # Luis 0
print(persona3.nombre, persona3.edad)  # Ana 30
print(persona4.nombre, persona4.edad)  # Desconocido 30
