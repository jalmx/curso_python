text= "mi super contenido 😃"

mi_archivo = open("archivo.txt", mode="w+", encoding="utf-8")

mi_archivo.write(text)

mi_archivo.close()
print("firts one file created 😃")


with open("archivo2.txt", mode="w+", encoding="utf-8") as documento:
    
    for i in range(10):
        documento.write(str(i)+"\n")
    
print("second file created 😃")