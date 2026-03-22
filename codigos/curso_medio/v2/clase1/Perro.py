from random import choice

class Perro:
    __nombre :str = "solovino"
    __raza : str= "electrico"
    __velocidad :float = 0.0

    def get_nombre(self):
        return self.__nombre

    def descripcion(self):
        print(f"nombre: {self.__nombre} de raza {self.__raza}")

    def ladrar(self):
        print("guua guuua!!!!")

    def correr(self, velocidad:int = 5):
        self.__velocidad+= velocidad
        print(f"va corriendo a {self.__velocidad} km/h")
    
    def jugar(self):
        objetos = ["pelota", "hueso", "chancla"]
        return choice(objetos)

perrito = Perro()
perrito.descripcion()
perrito.ladrar()
for n in range(10):
    perrito.correr(n+1)
print(f"El perrito {perrito.get_nombre()} esta jugando con {perrito.jugar()}")