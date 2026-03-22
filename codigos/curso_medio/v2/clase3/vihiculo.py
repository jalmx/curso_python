# Crea una clase base llamada Vehiculo con atributos marca y modelo.
# Crea una clase hija llamada Coche que además incluya el atributo puertas.
# Usa super() para inicializar los atributos de la clase base desde la clase hija.

class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Coche(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__(marca=marca, modelo=modelo)
        self.puertas = puertas


c = Coche("vocho", "clasico", 6)

print(c.marca)
print(c.modelo)
print(c.puertas)
