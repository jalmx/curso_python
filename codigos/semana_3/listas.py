nombres = ["roberto", "pablo", "diego", "luis", "jesus"]

print(nombres)
print(f"La lista contiene {len(nombres)} elementos")
## agregar elementos

nombres.append("Fernando")
nombres.append("Roman")
nombres.append("Luis")

print(nombres)

print(f"La lista contiene {len(nombres)} elementos")

## obteniendo un valor

nombre_1 = nombres[2]
print(nombre_1)
nombre_2 = nombres[7]
print(nombre_2)

nombres.append("Francisco")
nombres.append("Amado")
print(nombres)
ultimo_nombre = nombres[len(nombres) - 1]
print(ultimo_nombre)

ultimo_2 = nombres[-2]
print(ultimo_2)

nombres_2 = ["Ismael", "Juan", "Axel"]

nombres.extend(nombres_2)
print(nombres)

nombres += nombres_2
print(nombres)

# ordenar la lista
nombres.sort()
print(nombres)

numeros = [1, 4, 5, 23, 6, 7, 3, 4, 5, 6, 3, 6, 3, 8]
print(f"La suma es: {sum(numeros)}")
print(f"El maximo es: {max(numeros)}")
print(f"El minimo es: {min(numeros)}")


for element in nombres:
    print(element)

for index in range(len(nombres)):
    print(nombres[index])

count = 0
while count < len(nombres):
    print(nombres[count])
    count += 1

# Tuplas
numeros_tupla = (1,5,3)

print(numeros_tupla)

for n in numeros_tupla:
    print(n)
