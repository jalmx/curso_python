from os import path, makedirs, listdir
from pathlib import Path
import shutil
import sys  # aqui viene el método para mover archivos


files_ext = {
    "pdf": {"ext": [".pdf"]},
    "exec" : {"ext": ["exec"]},
    "compress" : {"ext": ["zip","rar","7zip"]},
    "word": {"ext": [".doc", ".docx"]},
    "imgs": {"ext": [".png", ".jpeg", ".jpg", "webm", ".gif", ".svg"]},
    "others": {"ext": []},
}


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

    path_dir_base = "" # la ruta la carpeta que vamos a ordenar

    # creación de las carpetas
    for folder in files_ext:
        files_ext[folder]["path"] = create_dir(folder)

    # leo todos los archivos de la carpetas
    files = listdir(path.abspath(path_dir_base))
    count = 0

    for f in files:

        if not path.isdir(path.join(path_dir_base, f)):

            name_folder = "others"

            for folder in files_ext:

                if Path(f).suffix in files_ext.get(folder)["ext"]:
                    name_folder = folder
                    break

            shutil.move(
                path.join(path_dir_base, f),  # ruta completa con nombre
                path.join(path_dir_base, name_folder, f),  # ruta nueva con el nombre
            )
            count += 1

    print(f"{count} moved")
