import os

path_dir = "archivos"

limit = 10

for count in range(limit):
    file_name = f"mi_archivo_{count+1}.txt"
    full_path = f"{path_dir}{os.path.sep}{file_name}"

    print(full_path)
    count+=1

    with open(full_path, "w+", encoding="utf-8") as new_file:
        new_file.write(f"has sido hackeado {count}")



