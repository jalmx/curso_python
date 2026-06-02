tabla = int(input("Da la tabla que quieres conocer: "))
limit = int(input("Da el limite de la tabla: "))


for count in range(1, limit + 1 ):
    print(f"{tabla} x {count } = { tabla * count}")
    count += 1
