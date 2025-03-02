import random


class Resistencia:

    def __init__(self, value:int):
        self.__name = "R"
        self.__set_value(value)

    def __set_value(self, value):
        if value >= 0 and value <= 1_000_000:
            self.__value = value
        else:
            self.__value = int(random.random() * 1000000)
        self.__set_name()

    def __set_name(self):
        self.__name = f"R{self.__value}"

    def get_name(self):
        return self.__name

    def value(self):
        return self.__value

if __name__ == "__main__":
    r10 = Resistencia(1000)
    print(r10.get_name())
    print(r10.value())
    r = Resistencia(1200)
    print(r.get_name())
    print(r.value())
