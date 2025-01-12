class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self, argumento):
        print(f"{self.nombre} - {argumento}")

class Estudiante(Persona):
    def __init__(self, nombre, matricula):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.matricula = matricula

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Matrícula: {self.matricula}")
        self.saludo(self.nombre)


# Prueba
estudiante = Estudiante("Juan", "12345")
estudiante.mostrar_informacion()
