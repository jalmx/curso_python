# 01
# # crea una estructura de python básica ya definida

# Con los siguientes archivos y carpetas

# <nombre pasado> (opcional) si no lo pasan, no se crea
# __main__.py -> aquí va el código a desarrollar
# __init__.py  -> se queda vació
# lib
# ---> util.py

## Funcionamiento
# strc duplicate
# strc

from os import path, makedirs
import sys


def create_file(name_file: str, path_file: str = "") -> str:
    """Create a file with a name
    Args:
        name_file (str): name file to create
        path_file (str): path of file to create

    Returns:
        str: full path from file
    """
    full_path = path.join(path_file, name_file)
    open(full_path, "w+")

    return path.abspath(full_path)


def create_dir(name_dir: str, path_dir: str = ""):
    """Create a folder

    Args:
        name_dir (str): _description_
        path_dir (str, optional): _description_. Defaults to "".
    """
    full_path = path.join(path_dir, name_dir)
    makedirs(full_path, exist_ok=True)
    return path.abspath(full_path)


def cli():
    values = sys.argv  ## Lee los argumentos pasados por terminal
    values = values[1:]  # estoy quitando el primer valor y me quedo con todo lo demás
    if len(values) > 0:
        return values[0]
    return ""


if __name__ == "__main__":
    files = ["__init__.py", "__main__.py", "util.py"]

    folders = ["lib"]

    name_project = cli()  # guardo el nombre del proyecto
    path_base =""
    if name_project:
        files.insert(0, name_project)  # inserto al inicio del array el nombre del proyecto
        path_base = create_dir(name_dir=name_project)

    print(files)

    for index, element in enumerate(files):
        if index != len(files) -1:
            if not element.endswith(".py"):
                element += ".py"
            create_file(element, path_base)
        else:
            dir_lib = create_dir(folders[0],path_dir=path_base)
            create_file(element, dir_lib)

    print(f"Project created at: {path_base or "here"}")

