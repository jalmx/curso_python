from math import pi

class Circulo:

    def __init__(self, radio):
        self.__radio = radio

    def get_area(self):
        return pi * self.__radio**2

    def get_perimetro(self):
        return 2 * pi * self.__radio

    def show_information(self):
        print(f"El circulo con radio {self.__radio} tiene un area de {self.get_area()}u^2 y un perimetro de {self.get_perimetro()}u")

c1 = Circulo(5.2)
c2 = Circulo(9)
c1.show_information()
c2.show_information()