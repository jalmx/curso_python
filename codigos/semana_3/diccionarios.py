diccionario ={
    "nombre_1" : "ismael",
    "nombre_2" : "amado",
    "3": "tres",
    "2": "dos",
    "lista": ["roberto", "pablo", "diego", "luis", "jesus"]
}

print(diccionario)
# obtener los valores del diccionario

nombre = diccionario["nombre_1"]
print(nombre)

nombres = diccionario.get("lista")
print(nombres)

# if diccionario.get("x"):
#     print("hago algo con la llave")
# else:
#     print("hago otro cosa sin la llave")

# recorriendo un diccionario

for key in diccionario:
    print(f"La llave {key} tiene de valor: {diccionario[key]}")
