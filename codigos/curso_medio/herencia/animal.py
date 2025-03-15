class Animal(object):


    def __init__(self, nombre):
        self.nombre = nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Soy {self.nombre} de Animal"

    def __str__(self):
        return f"Soy la clase Animal - {self.nombre}"

class Pato(Animal):

    def __init__(self, nombre, velocidad):
        super().__init__(nombre) # se manda a llamar al constructor padre
        self.velocidad = velocidad


    def saludar(self):
        return "cuak cuak!!!!"

    def volar(self):
        print(f"voy volando {self.velocidad}")

class Gato(Animal):

    def saludar(self):
        return f"{super().saludar()} - miau!!!!!!"

class Tigre(Gato):

    def saludar(self):
        return "rourrrrrrr!!!!!!!!"

if __name__ == "__main__":
    animalito = Animal("animalito de la creacion")
    animalito.set_nombre("patito")
    print(animalito)
    print(animalito.saludar())
    patito = Pato("Duck", 120)
    patito.set_nombre("Super pato")
    print(patito)
    print(patito.saludar())
    patito.volar()
    gatito = Gato("Gatillo")
    gatito.set_nombre("gato volador")
    print(gatito.saludar())
    tiger = Tigre("Toñito")
    tiger.set_nombre("Toño")
    print(tiger.saludar())
