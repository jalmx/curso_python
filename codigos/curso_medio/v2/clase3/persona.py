class Persona:

    def __init__(self):
        self.nombre = "persona"

    def __str__(self):
        return f"Persona. nombre={self.nombre} :D"


class Empleado(Persona):

    def __init__(self):
        self.nombre = "Empleado"
         
    def datos(self):
        print("empleado")
    
    def __str__(self):
        print(super().__str__())
        return f"Empleado. nombre={self.nombre}"

# Prueba
persona = Persona()
print(persona)

empleado = Empleado()
print(empleado)