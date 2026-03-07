from codigos.curso_medio.poo_basic.circulo import Circulo
from random import random

if __name__ == "__main__":
    circulo1 = Circulo(10)
    circulo2 = Circulo(4)
    circulo3 = Circulo(random()*10)

    circulo1.show_information()
    circulo2.show_information()
    circulo3.show_information()

    for i in range(1000):
        Circulo(random()*10).show_information()
