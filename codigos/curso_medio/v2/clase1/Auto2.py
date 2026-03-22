
class Auto:

    def __init__(self, tipo:str, marca:str):
        self.__tipo = tipo
        self.__marca = marca

    def show_information(self):
        print(f"Es un {self.__tipo} de la marca: {self.__marca}")


if __name__ == "__main__":

    auto1 = Auto("moto", "robada")
    auto2 = Auto("auto", "descompuesto")
    auto1.show_information()
    auto2.show_information()