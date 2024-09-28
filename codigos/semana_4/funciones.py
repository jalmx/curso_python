# calcule el perimetro del cuadrado


import math


def perimetro_cuadrado():
    # aqui va todo el codigo de mi funcion
    lado = 4
    resultado = lado * 4
    print(f"El resultado es {resultado}")


def area_circulo():
    # aqui va todo el codigo de mi funcion
    radio = 3
    resultado = math.pi * pow(radio, 2)
    print(f"El area es {resultado}")


# crear una funcion que calcule el area de un circulo
# con radio 10, e imprima el resultado
# despues ejecutan la funcion

perimetro_cuadrado()
area_circulo()


# funciones que retornen un valor
def perimetro_cuadrado_2():
    # aqui va todo el codigo de mi funcion
    lado = 4
    resultado = lado * 4
    return resultado


print(f"El resultado del cuadrado es {perimetro_cuadrado_2()}")


def area_circulo_2():
    # aqui va todo el codigo de mi funcion
    radio = 3
    resultado = math.pi * pow(radio, 2)
    return resultado


print(f"El resultado del circulo {area_circulo_2()}")

# funciones que reciben argumentos


def saludo(nombre):  # funcion que recibe un argumento
    return f"Holis {nombre}!!!"


print(saludo("Amado"))
print(saludo("Ismael"))
print(saludo("Karol"))
print(saludo("Axel"))


def perimetro_cuadrado_3(lado):
    return lado * 4


for i in range(1, 5):
    print(f"El perimetro del lado {i} es {perimetro_cuadrado_3(i)}")


def area_triangulo(base, altura):
    return (base * altura) / 2


print(f"La base es: 4, altura: 3, El area es: {area_triangulo(4,3)}")

# area del rectángulo

def area_rectangulo(base, altura):
    return (base * altura)


print(f"La base es: 6, altura: 2, El area es: {area_rectangulo(6,2)}")
