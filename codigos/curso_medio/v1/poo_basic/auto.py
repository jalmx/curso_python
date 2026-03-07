class Auto:
    color = "Blue" # agregando atributos a la clase
    on = False

    def decirNombre(self):
        return "Soy un carrito feliz"

    def acelerando(self):
        print("voy mas rapido")

    def encender(self):
        self.on = True

if __name__ == "__main__":
    mi_carrito = Auto()
    print(mi_carrito.color)
    print(mi_carrito.on)
    mensaje = mi_carrito.decirNombre()
    print(mensaje)
    mi_carrito.acelerando()

    print(f"Mi carrito esta encendido {mi_carrito.on}")
    mi_carrito.encender()
    print(f"Mi carrito esta encendido {mi_carrito.on}")
