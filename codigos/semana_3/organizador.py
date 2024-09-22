import os
import shutil #aqui viene el metodo para mover archivos

path_dir_base = "/home/xizuth/Projects/curso_python/codigos/semana_3/prueba"

files_ext = {
    "pdf": [".pdf"],
    "word" : [".doc", ".docx"],
    "imgs" : [".png", ".jpeg",".jpg", "webm", ".gif", ".svg"],
    "psd": [".psd", ".ai"],
    "compress": [".zip", ".rar"],
    "code": [".py", ".c", ".h", ".ino"],
    "presentacion": ["ppt", "pptx"],
    "others": []
}

# creación de las carpetas

for folder in files_ext:
    os.makedirs(f"{path_dir_base}{os.path.sep}{folder}", exist_ok=True)

# leo todos los archivos de la carpetas
files = os.listdir(path_dir_base)

for f in files:

    if not os.path.isdir(f"{path_dir_base}{os.path.sep}{f}"):
        name_folder = "others"
        if f.endswith(".pdf"):
            name_folder = "pdf"
        elif f.endswith(".doc") or f.endswith(".docx"):
            name_folder = "word"

        shutil.move(
            f"{path_dir_base}{os.path.sep}{f}", # ruta completa con nombre
            f"{path_dir_base}{os.path.sep}{name_folder}{os.path.sep}{f}" # ruta nueva con el nombre
            )
