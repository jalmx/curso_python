import random
import os

exts = ["pdf", "doc", "png", "zip"]
path_dir = "/home/xizuth/Projects/curso_python/codigos/semana_3/prueba"

for i in range(10):
    for ext in exts:
        with open(f"{path_dir + os.path.sep}archivo_{int(random.random() * 1000)}.{ext}", "w+") as file:
            file.write("hola")

