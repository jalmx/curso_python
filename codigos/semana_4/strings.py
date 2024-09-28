# manipulación de strings

#lista = ["s","o","y"]
mensaje = "soy un hacker usando python"

# print(mensaje[0])
# print(mensaje[1])
# print(mensaje[2])
# print(mensaje[3])

count = 0
for letra in mensaje:
    #print(letra)
    if letra == "o":
        count+=1

print(f"La letra 'o' se repite {count}")

# metodos de los string

# convertir a minusculas, mayusculas, primera letra en mayuscula

frase = "python veniaM aliQuip sIt eT eu Laboris siT NON. python"

print(f"frase original {frase}")
minuscula = frase.lower()
mayusculas = frase.upper()
capitaliza = frase.capitalize()

print(f"minusculas: {minuscula}")
print(f"mayusculas: {mayusculas}")
print(f"primera mayuscula: {capitaliza}")

print(f"La palabra 'python' aparece {frase.count('python')} veces")

print(f'Es un número: {"4".isdigit()}')
print(f'Es un número: {"4".isnumeric()}')
print(f'Esta en minúsculas: {"hola".islower()}')
print(f'Esta en mayúsculas: {"HOLA".isupper()}')
print(f'Es un espacio: {" ".isspace()}')

frase2 = "    texto       ".strip()
print(frase2)
