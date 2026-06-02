from random import randint, choice

number_random = randint(1, 20)
frases_fail = [
    "TAZ PELADO!!",
    "CASI TE CAE UN RAYO!!",
    "TE FALTA MAS PUNCH!!",
    "LO HACE MEJOR MI AWELITA MUERTA!!",
]

frases_win = [
    "ERES UN GENIO!!",
    "LO LOGRASTE!!",
    "ERES UN CRACK!!",
]

print("Adivina el numero")
print("Tienes 3 intentos")
print("El numero esta entre 1 y 20")
print("Que la fuerza te acompañe!!")

intentos = 0
print("el numero aleatorio es: ", number_random)

while True:
    new_number = int(input("Introduce un numero: "))
    if new_number < number_random:
        print("FALLASTE!!")
        print(choice(frases_fail))
        print("El numero es mayor")
    elif new_number > number_random:
        print("FALLASTE!!")
        print(choice(frases_fail))
        print("El numero es menor")
    else:
        print("FELICIDADES!!")
        print(choice(frases_win))
        break
    intentos += 1
    if intentos >= 3:
        print("LASTIMA MARGARITO!!")
        print("PERDISTE!!")
        print("El numero era: ", number_random)
        break
