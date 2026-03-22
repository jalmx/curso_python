
class Pokemon:

    def __init__(self, nombre):
        self.nombre = nombre

    def decir_nombre(self):
        print(self.nombre)

class Pikachu(Pokemon):
    
    def __init__(self, nombre, poder):
        super().__init__(nombre)
        self.poder=poder

    def __str__(self):
        return f"{self.nombre} con un poder de {self.poder}"

if __name__ == "__main__":
    pikachu = Pikachu("picachu", 10)
    pikachu.decir_nombre()
    print(pikachu)