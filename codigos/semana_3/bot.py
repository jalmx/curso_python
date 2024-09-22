import random

saludos = ["Hola", "holis", "que pedro, pablo"]

edad = random.randrange(35) + 15

lista = ["ismael", "amado", "axel hiram", "karol", "roman"]
nombre = random.choice(lista)
nombres = ["botcito", "terminator",nombre ]

frases = ["Vamos por las frias", "Vamos a echar la reta", "No quiero"]

#############################

print( random.choice(saludos) )
name_user = input("Como te llamas?: ")
print(f"Esta chido tu nombre, yo me llamo {random.choice(nombres)}, tengo una edad de {edad}")

answer = input("Quieres ser mi amigo? [S:Si, N: No]")

if answer.upper() == "S":
    print(random.choice(frases))
else:
    print("Voy estar es tus peores pesadillas por siempre!!!! ")
