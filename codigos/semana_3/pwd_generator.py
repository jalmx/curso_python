import random

letters = "abcdefghijklmnopqrstuvwxyz"
letters_upper = letters.upper()
numbers = "1234567890"
symbols = "|¬°!\"#$%&/()=?¡¿'@+}{-.,_:;[*¨]}><"

length = 8
name_file = f"pwd_{int(random.random()*100000)}.txt"
passwords = ""

for i in range(10):
    pwd = ""
    while len(pwd) < length:
        symbol = random.choice(letters + letters_upper + numbers + symbols)
        pwd += symbol

    print(f"{i+1}.- {pwd}")
    passwords +=pwd +"\n"

file_pwd = open(name_file,mode="w+", encoding="utf-8")
file_pwd.write(passwords)
file_pwd.close()
print(f"File created with name {name_file}")

