#definir clase
# como se escribir el nombre de una clase
# CalmelCase 

class Carro:
    ## ESTAS VARIABLES SON GLOBALES
    color = "Sin color"
    status = False ## esta variable es global 
    autopilot = False

    def saludo(self):
        print(f"hola soy un carrito volador, soy de color: {self.color}")

    def arracar(self):
        self.status = True #aqui la variable status es local
    
    ###  def apagar

mi_carrito = Carro() #cree mi instancia de Carro

print(f"mi carrito 1: {mi_carrito.color} y estado {mi_carrito.status}")## False
mi_carrito.saludo()
mi_carrito.arracar()

print(f"mi carrito 1: {mi_carrito.color} y estado {mi_carrito.status}") ## True
mi_carrito.status = False ##aqui estoy cambiando el estado de status

print(f"el status nuevo: {mi_carrito.status}")

mi_carrito.color = "verde"
print(f"mi carrito 1: {mi_carrito.color} y estado {mi_carrito.status}") ## True