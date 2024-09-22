import random

tijera = 1
papel = 2
piedra = 3

robot = random.choice([tijera, papel, piedra])

mensaje = """
1 -> tijera
2 -> papel
3 -> piedra
"""

while True:

    answer = int(input(mensaje))
    if answer == robot:
        print("empate")
    else:
        if answer > robot:
            print("Ganaste!!!!!")
            break
        else:
            print("Perdiste!!!!")
            break
