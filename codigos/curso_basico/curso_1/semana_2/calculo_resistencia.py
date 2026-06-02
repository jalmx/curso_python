# realizar la calculadora de
# resistencia serie, para 4 resistencias, e imprimir el resultado

contador = 0
resistencia_total_serie = 0
resistencia_total_paralelo = 0

while contador < 4:
    resistencia = float(input(f"Da la resistencia {contador+1}: "))
    resistencia_total_serie += resistencia
    resistencia_total_paralelo += 1 / resistencia
    contador += 1

print(f"La resistencia total en serie es: {resistencia_total_serie} Ohm")
print(f"La resistencia total en paralelo es: {1/resistencia_total_paralelo} Ohm")


