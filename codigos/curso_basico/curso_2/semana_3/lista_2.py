files = [
    "foto.jpg",
    "documento.pdf",
    "foto2.png",
    "documento2.pdf",
    "archivo.txt",
    "foto3.png",
    "documento3.docx",
    "archivo",
]
print(files)
list_pdf = []
list_images = []
list_unknown = []

for file in files:
    if file.endswith(".pdf"):
        list_pdf.append(file)
    elif file.endswith(".jpg") or file.endswith(".png"):
        list_images.append(file)
    else:
        list_unknown.append(file)
list_pdf.sort()
list_images.sort()
list_unknown.sort()
print(f"{len(list_pdf)} - " + "PDFs:", list_pdf)
print(f"{len(list_images)} - " "Images:", list_images)
print(f"{len(list_unknown)} - " "Unknown:", list_unknown)

list_pdf.reverse()
list_images.reverse()
list_unknown.reverse()
print(f"{len(list_pdf)} - " + "PDFs:", list_pdf)
print(f"{len(list_images)} - " "Images:", list_images)
print(f"{len(list_unknown)} - " "Unknown:", list_unknown)

print("*" * 20)

frase = "Hola, soy una frase de prueba"

for letra in frase:
    print(letra)

for pdf in list_pdf:
    for letra in pdf:
        print(letra)

list_pdf.extend(list_images)
print(list_pdf)
lista2 = list_pdf + list_unknown
print(lista2)

lista2[-1] = "foto_final.png"
print(lista2)

contador = 0
while contador < len(lista2):
    if lista2[contador].endswith("pdf"):
        lista2[contador] = lista2[contador].replace("documento", "mi archivo")
    contador += 1
print(lista2)
