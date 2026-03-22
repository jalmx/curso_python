import uuid


class Component:

    def __init__(self, nombre: str, valor: str, codigo: str = None, id=None):
        self.__nombre = nombre
        self.__valor = valor
        self.__codigo = codigo if codigo else Component.generate_code()
        self.__id = id if id else Component.generate_code()[:7]

    def get_nombre(self) -> str:
        return self.__nombre

    def get_valor(self) -> str:
        return self.__valor

    def get_codigo(self) -> str:
        return self.__codigo

    def get_id(self) -> str:
        return self.__id

    def description(self):
        return f"id[{self.__id}] -> el nombre es {self.__nombre} tiene el valor {self.__valor} con el codigo: {self.__codigo}"

    @staticmethod
    def generate_code():
        return str(uuid.uuid4())

    @staticmethod
    def columnas():
        return ["id", "nombre", "valor", "codigo"]
