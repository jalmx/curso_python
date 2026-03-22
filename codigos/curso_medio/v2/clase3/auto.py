# clase padre Auto
#  metodo tipo-> retorna un mensaje diciendo que tipo de carro es

# clase  Sedan -> sobre escribir el metodo de la clase padre
# clase  Deportivo

# despues crear una instancia de Auto, Sedan y Deportivo y mandan a imprimir cada mensaje

class Auto(object):
    """Clase padre
    """
    def mensaje(self):
        return "Soy un auto general"

    def __str__(self)-> str:
        return "Instanacia de Auto"


class Sedan(Auto):
    """Clase hija
    """
    def mensaje(self):
        return "Soy un auto Sedan"
    
    def __str__(self):
        return "Soy una instancia de Sedan"

class Deportivo(Auto):
    """Clase hija
    """
    def mensaje(self):
        return "Soy un auto Deportivo"
    
    def __str__(self):
        return "Soy una instancia de deportivo"

if __name__ == "__main__":
    auto = Auto()
    sedan = Sedan()
    deportivo = Deportivo()

    print(auto.mensaje())
    print(sedan.mensaje())
    print(deportivo.mensaje())

    print(auto)
    print(sedan)
    print(deportivo)