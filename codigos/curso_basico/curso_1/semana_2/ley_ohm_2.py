# Crear una calculadora de ley de ohm,
# preguntando al usuario lo que desea calcular
# 1) Voltaje
# 2) Corriente
# 3) Resistencia

# Formula I = V / R
# Formula R = V / I
# Formula V = R I

option =  input(
        """
======= CALCULADORA DE LEY DE OHM
1) Voltaje
2) Corriente
3) Resistencia\n"""
    )

if option: # Truthy
    option = int(option)

    if option == 1:
        print("Calculando voltaje")
        resistance = float(input("Dar la resistencia:"))
        current = float(input("Dar la corriente:"))
        print(f"El voltaje es {resistance * current} V")
    elif option == 2:
        print("Calculando Corriente")
        resistance = float(input("Dar la resistencia:"))
        voltage = float(input("Dar el voltaje:"))
        print(f"El voltaje es {voltage / resistance } A")
    elif option == 3:
        print("Calculando resistencia")
        voltage = float(input("Dar el voltaje:"))
        current = float(input("Dar la corriente:"))
        print(f"El voltaje es {voltage/ current} Ohm")
    else:
        print(f"La Opción {option} no existe")
else:
        print(f"NO PUEDES DEJAR VACIA LA RESPUESTA")
