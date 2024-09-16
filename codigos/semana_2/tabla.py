# imprimir la tabla que elija el usuario
# el usuario da el limite de la tabla

tabla = int(input("Da la tabla que quieres conocer: "))
limit = int(input("Da el limite de la tabla: "))
count = 1

while count <= limit:
    print(f"{tabla} x {count } = { tabla * count}")
    count += 1


