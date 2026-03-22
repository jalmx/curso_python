class Animal:

    def sonido(self):
        print("haciendo un sonido")
    
    def mensaje(self,text:str):
        print(f"te saluda un animal general: {text}")


class Perro(Animal):
    
    def sonido(self):
        print("Gua, Gua!!!")


class Gato(Animal):
    
    def sonido(self):
        print("miua!!!")


if __name__ == "__main__":

    a = Animal()
    a.sonido()
    a.mensaje("")
    
    p = Perro()
    p.sonido()
    p.mensaje("soy un perro")

    g = Gato()
    g.sonido()
    g.mensaje("soy un gatito")