class Auto:

    noPuertas : int = 0
    kilometraje : float = 0.0

    def acelerar(self):
        self.avanzar(50)
        print(f"acelerando muy rapido 50km/h...")
    
    def arrancar(self):
        print("arrancando....")
    
    def avanzar(self,velocidad:int = 0):
        self.kilometraje += (velocidad/10)
        print(f"kilometraje acumulado: {self.kilometraje}km...")


carrito = Auto()# estoy creando la instancia
carrito.arrancar() # llamo al metodo arrancar
carrito.acelerar() # llamo al metodo acelerar
carrito.avanzar(100) # llamo al metodo acelerar