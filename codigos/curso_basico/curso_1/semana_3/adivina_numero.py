import random

number_random = random.randint(1, 10) # obtenemos el numero random
errors = 0

print("ADIVINA EL NÚMERO")
while True:
    number_user = int(input("Dame un numero de entre 1 al 10: "))

    if number_user == number_random:
        print("Adivinaste el número crack!!!")
        break
    else:
        errors += 1
        if errors >=3:
            print(f"Lastima margarito, el número era {number_random}")
            break
        if number_user < number_random:
            print("Es hacia arriba")
        else:
            print("Es hacia abajo")
