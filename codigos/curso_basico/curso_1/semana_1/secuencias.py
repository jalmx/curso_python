# Secuencias de escape

# colocando varios enter
sep = "*"*40
one_line = "1. hola\n2. hola2\n3. adios"
## string con pre-formato
multi = """1. hola
2. hola2
3. adios"""

print(one_line)
print(sep)
print(multi)
print(sep)
row = "col1\t\tcol2\t\tcol3"
table = row + "\n" + row + "\n" + row + "\n" + row+ "\n" + row+ "\n" + row+ "\n" + row+ "\n" + row
print(table)
