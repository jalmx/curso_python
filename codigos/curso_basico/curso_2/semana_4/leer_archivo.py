
with open("archivo.csv", mode="r", encoding="utf-8") as file:
    lines = file.readlines() ## me da una lista de renglones
    
    for index, line in enumerate(lines):
        print(f"en la linea {index +1} contiene: {line.strip()}")
        
    
    