import math
## Funciones

## saludo

def saludar():
    print("Ya soy hacker!!!")
    

def suma2():
    print(f"dos mas dos es {2+2}")


saludar()
suma2()

def saludo2(name:str):
    print(f"Hola {name}!!!!")

def eleva_cuadrado(x):
    print(pow(x,2))

def eleva_n(x,n):
    print( x**n )
    
def calcular_area_cuadrado(lado):
    area = lado *lado
    return area


def area_circulo(radio):
    return math.pi * radio**2    


def operacion_circulo(radio, opcion="area"):
    if opcion == "area":
        area = area_circulo(radio)# estoy llamando a otra funcion
        return area
    elif opcion == "perimetro":
        perimetro = math.pi * (radio *2)
        return perimetro
    else:
        return -1
    

radio = 5
area = operacion_circulo(opcion="area",radio=radio)
perimetro = operacion_circulo(radio, "perimetro")
desconocido = operacion_circulo(radio)
print(f'El area de un radio de {radio} es {area}')
print(f'El perimetro de un radio de {radio} es {perimetro}')
print(f'Desconocido es {desconocido}')

saludo2("Miguel")
saludo2("Yael")
saludo2("Diego")
eleva_cuadrado(3)
eleva_cuadrado(5)
eleva_cuadrado(9)
eleva_n(2,3)
eleva_n(5,2)

resultado = calcular_area_cuadrado(3)
print(f"El area del cuadrado es {resultado}")

radio = 4
circulo = area_circulo(radio)
print(f"El area del circulo es {circulo}")




