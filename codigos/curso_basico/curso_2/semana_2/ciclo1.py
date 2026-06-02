import time

contador = 0 # declaro mi variable auxiliar "contador"

while contador < 10:
    print(contador)         # imprimir el valor del contador
    contador = contador + 1 # incremento al contador
    time.sleep(3)               # espero 1 segundo

print("El ciclo termino")