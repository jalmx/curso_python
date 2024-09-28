# como manipular archivos

# crear un archivo

# w: escribir
# a: append -> agregar al final
# r: read -> leer
archivo = open("mi archivo.txt", "r")

#print( archivo.read() )

count = 1
for row in archivo.readlines():
    print(f"linea {count}: {row}")
    count+=1
    if row.strip() == "hola":
        print(f"tiene el mensaje '{row}'")

content = """
# generado automaticamente

print("programa creado desde un script en python")
"""

script = open("script.py", "w+")
script.write(content)
script.close()

with open("script2.py", "w+") as my_script:
    my_script.write(content)
