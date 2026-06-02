#Vamos a imprimir 10 números, del 0 al 9, recordemos que el número que le pasamos es el tope y ese no se imprime,
#y el valor inicial por default es 0, el incremento es de 1 en 1

tabla = int(input("Dame la tabla de multiplicar que quieres: "))
end = int(input("Dame el número hasta donde quieres la tabla: "))

for valor in range(1,end +1,):
    print(f'{tabla} x {valor} = {tabla * valor}')
