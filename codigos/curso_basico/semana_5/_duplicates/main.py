
# Checa los archivos de una carpeta y debe indicar cuales son los mismo

# metodo 1 con sus datos de peso, extension
# metodo 2 de hash basico con md5

import os
from pathlib import Path

path_dir = "/media/data/Books/Hardware hacking"

path_dir = os.path.abspath(path_dir)
list_files = (os.listdir(path_dir))

for e in list_files:
    full_path_file = os.path.join(path_dir, e)
    print(f"{full_path_file} suffix:{Path(full_path_file).suffix}:" )
    print(f"size: {os.path.getsize(full_path_file) }")
    print("********************")
