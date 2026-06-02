# crear archivos dummy
from random import randint
from os import path

exts = ["txt", "csv", "docx", "pdf", "png", "jpg", "mp4", "exe"]

for i in range(1000):
    for ext in exts:
        open(f"tmp{path.sep}archivo_{randint(1,1000)}.{ext}", "w+")
print("archivos creados")
