count = 0

while count <= 10:
    print("antes del continue")

    count += 1

    if count == 8 or count == 3:
        continue

    print( f"El contador va en {count}")
