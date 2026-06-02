# calculo de una media, para 5 numeros

count = 0
total = 0
max_count = 5

while count < max_count:
    value = float( input(f"Dar el valor {count+1}: "))
    total += value
    count += 1

average = total / max_count

print(f"La media es: {average}")


