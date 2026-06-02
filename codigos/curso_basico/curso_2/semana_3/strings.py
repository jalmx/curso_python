frase = "Hola, python , Soy uNa frASe muy divertIDA, python es genial"

print(frase.lower())  # convierte todo a minusculas
print(frase.upper())  # convierte todo a mayusculas
print(frase.capitalize())  # convierte la primera letra en mayuscula y las demas en minusculas
print(frase.title())  # convierte la primera letra de cada palabra en may
print(f"la palabra 'a' aparece {frase.lower().count('a')} veces")
print(frase)

archivos = [
    "foto1.png",
    "documento1.pdf",
    "foto2.png",
    "documento2.pdf",
    "musica1.mp3",
]
contador = 0
contador_pdf = 0

while contador < 5:
    archivo = archivos[contador]
    print(f"El archivo es: {archivo}")
    if archivo.endswith(".pdf"):
        contador_pdf += 1
    contador += 1

print(f"Hay {contador_pdf} archivos pdf")

frase2 = "   hola     "
print(frase2.lstrip())
print(frase2.rstrip())
print(frase2.strip())

frase3 = "python es el mejor lenguaje"
frase4 = frase3.replace("python", "java")
print(frase4.replace(" ", "_"))

contador = 0
while contador < 5:
    archivo = archivos[contador]
    print(f"El archivo es: {archivo}")
    if archivo.startswith("foto"):
        arch2 = archivo.replace("foto", "imagen")
        print(f"el {archivo} se ha renombrado a ->{arch2}")
    contador += 1

frase5 = "carpeta/carpeta2/archivo.txt"
print(frase5.split("a"))