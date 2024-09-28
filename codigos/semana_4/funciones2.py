import math


# argumentos con valores por default
def area_circulo(radio=1):
    return math.pi * pow(radio, 2)


def fuerza(masa, acelaracion=9.81):
    return masa * acelaracion


print(area_circulo())
print(area_circulo(4))

print(fuerza(2))
print(fuerza(3, 5.4))

r1 = fuerza(acelaracion=5.7, masa=8)
r2 = fuerza(masa=7)
r3 = fuerza(masa=7, acelaracion=9.4)

print(r1)
print(r2)
print(r3)
