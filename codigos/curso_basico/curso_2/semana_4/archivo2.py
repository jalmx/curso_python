## crear un archivo separado por comas, simular datos de un sensor temperatura
from random import random

def create_file(header_colum, content,  file_name="archivo.csv"):
    with open(file_name, mode="w+", encoding="utf-8") as file:
        file.write(header_colum+"\n") ## titulo de la columna
        file.writelines(content) ## insertar todos los datos del sensor
        
def create_data():
    data = []
    for d in range(20):
        data.append( str(random()*50)[:5] + "\n")
    
    return data

create_file("temperatura", create_data())