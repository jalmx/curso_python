class Auto:
    def __init__(self, tipo, marca):
        self._tipo = tipo
        self._marca = marca

    def mostrar_informacion(self):
        print(f"Tipo: {self._tipo}, Marca: {self._marca}")


auto1 = Auto("Super vocho", "Voshito")
auto2 = Auto("Moto", "Yamaha")
auto1.mostrar_informacion()
auto2.mostrar_informacion()
