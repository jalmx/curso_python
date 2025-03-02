from math import pi
class Circulo:

    def __init__(self, radio: float) -> None:
        self.__radio = radio

    def get_area(self):
        return pow(self.__radio, 2) * pi

    def get_perimetro(self):
        return 2 * self.__radio * pi

    def show_information(self):
        print(f"El circulo con radio {self.__radio} tiene un area de {self.get_area()} con un perimetro de {self.get_perimetro()}")
