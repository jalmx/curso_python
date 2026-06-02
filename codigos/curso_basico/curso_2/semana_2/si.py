# Damos el menu y guardamos la opción del usuario
print("Calculadora de Suma y Resta")
print("1) Suma")
print("2) Resta")
print("3) Multiplicación")
print("4) Division")
opcion = int(input())

if opcion == 1:
    print("====== SUMA =======")
    valor_1 = float(input("Dar valor 1: "))
    valor_2 = float(input("Dar valor 2: "))
    suma = valor_1 + valor_2
    print("La suma es: " + str(suma))
elif opcion == 2:
    print("====== RESTA =======")
    valor_1 = float(input("Dar valor 1: "))
    valor_2 = float(input("Dar valor 2: "))
    resta = valor_1 - valor_2
    print("La resta es: " + str(resta))
elif opcion == 3:
    print("====== MULTIPLICACION =======")
    valor_1 = float(input("Dar valor 1: "))
    valor_2 = float(input("Dar valor 2: "))
    suma = valor_1 * valor_2
    print("La suma es: " + str(suma))
elif opcion == 4:
    print("====== DIVISION =======")
    valor_1 = float(input("Dar valor 1: "))
    valor_2 = float(input("Dar valor 2: "))
    resta = valor_1 / valor_2
    print("La resta es: " + str(resta))
else:
    print("Opción no válida")
