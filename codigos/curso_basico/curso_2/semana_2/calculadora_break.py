opcion = 0

while True:
    print("-------------------------------------")
    print("Calculadora Suma y Resta")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La suma es: " + str(valor1 + valor2))
    elif opcion == 2:
        valor1 = float(input("Dar el primer valor"))
        valor2 = float(input("Dar el segundo valor"))
        print("La resta es: " + str(valor1 - valor2))
    elif opcion > 3 or opcion < 1:
        print("La opcion no existe")
    else:
        break

print("Programa a finalizado")