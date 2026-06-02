# sorty
import os
from sys import argv
import shutil


files_ext = {
    "img": ["png", "jpg", "jpeg", "gif", "bmp", "tiff"],
    "video": ["mp4", "mkv", "avi", "mov"],
    "document": ["docx", "xlsx", "pptx", "csv"],
    "pdf": ["pdf"],
    "programacion": ["py", "js", "html", "css", "java", "c", "cpp", "h"],
    "programas": ["exe", "bin"],
    "otros": ["txt"],
}


def get_files_path(path_dir: str):
    """obtener la lista de los archivos de esa carpeta

    Args:
        path_dir (str): ruta de la carpeta
    """
    paths_files = []
    if os.path.exists(path_dir) and os.path.isdir(path_dir):
        paths = os.listdir(path_dir)
        for file in paths:
            full_path = os.path.join(path_dir, file)
            if os.path.isfile(full_path):
                paths_files.append(full_path)
        return paths_files
    else:
        print("la ruta no existe o no es una carpeta")


def change_path(path_file: str, new_folder: str):
    #'tmp/archivo_626.txt'
    #'tmp/otros/archivo_626.txt'
    name_file = os.path.basename(path_file)
    base_dir = os.path.dirname(path_file)
    return os.path.join(base_dir, new_folder, name_file)

def move_files(file_paths: list):
    """mover archivos de una carpeta a otra

    Args:
        src (str): ruta de la carpeta origen
    """
    other_ext = []

    for file in file_paths:
        _, ext = os.path.splitext(file)
        for folder, extentions in files_ext.items():
            if ext.replace(".","") in extentions:
                shutil.move(file, change_path(file, folder))
            else:
                pass
                #shutil.move(file, change_path(file, "otros"))

    print("Files moved")

def create_folders(path_base: str):
    """Crear las carpetas

    Args:
        path_base (str): nombre de la carpeta
    """
    for folder in files_ext.keys():
        os.makedirs(os.path.join(path_base, folder), exist_ok=True)
    print("Folders created")


if __name__ == "__main__":
    folder_base = "./"
    files =(get_files_path(folder_base))
    create_folders(folder_base)
    move_files(files)