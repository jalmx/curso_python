import os
from pathlib import Path
import shutil  # aqui viene el metodo para mover archivos

path_dir_base = "/home/xizuth/Projects/curso_python/codigos/semana_3/prueba"

files_ext = {
    "pdf": [".pdf"],
    "word": [".doc", ".docx"],
    "imgs": [".png", ".jpeg", ".jpg", "webm", ".gif", ".svg"],
    "psd": [".psd", ".ai"],
    "compress": [".zip", ".rar", ".7zip"],
    "code": [".py", ".c", ".h", ".ino"],
    "presentation": ["ppt", "pptx"],
    "others": [],
}

# creación de las carpetas

for folder in files_ext:
    os.makedirs(f"{path_dir_base}{os.path.sep}{folder}", exist_ok=True)

# leo todos los archivos de la carpetas
files = os.listdir(path_dir_base)
count = 0

for f in files:

    if not os.path.isdir(f"{path_dir_base}{os.path.sep}{f}"):

        name_folder = "others"

        for folder in files_ext:

            if Path(f).suffix in files_ext.get(folder):
                name_folder = folder
                break

        shutil.move(
            f"{path_dir_base}{os.path.sep}{f}",  # ruta completa con nombre
            f"{path_dir_base}{os.path.sep}{name_folder}{os.path.sep}{f}",  # ruta nueva con el nombre
        )
        count += 1


print(f"{count} moved")
