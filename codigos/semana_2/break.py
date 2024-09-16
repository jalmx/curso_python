count = 0

while count <= 10:
    print("antes del break")

    count += 1

    if count == 3:
        break # rompe ciclos

    print( f"El contador va en {count}")
