import random

for i in range(2):
    numero_aleatorio = random.random()
    print(numero_aleatorio)

print("*"*25)

for i in range(8):
    numero_aleatorio_rango = random.randrange(20)
    print(numero_aleatorio_rango)

print("*"*25)

lista = ["ismael", "amado", "axel hiram", "karol", "roman"]

for i in range(3):
    nombre_aleatorio = random.choice(lista)
    print(f"{nombre_aleatorio.capitalize()} es hacker en python")

print("*"*25)

for i in range(10):
    numero_rango = random.randint(5, 16)
    print(numero_rango)


