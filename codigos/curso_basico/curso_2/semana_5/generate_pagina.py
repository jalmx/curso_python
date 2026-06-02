from random import choice

colors = ["peru", "red", "blue", "green", "yellow", "purple", "orange","tomatoe", "blueskype"]


def get_page(title, content, color="peru"):
    with open("/home/xizuth/Downloads/tmp/curso/semana_5/index.html", mode="r", encoding="utf-8") as file:
        template = file.read()
        template = template.replace("{title}", title)
        template = template.replace("{content}", content)
        template = template.replace("{color}", color)
        return template


def save_file(page: str, name_file="pagina.html"):
    with open(name_file, mode="w+", encoding="utf-8") as file:
        file.write(page)
        print(f"Archivo {name_file} creado exitosamente.")


def main():
    for i in range(30):
        page = get_page(
            title=f"Página {i+1}",
            content=f"Contenido de la página {i+1} generado dinamicamente.",
            color=choice(colors),
        )
        save_file(page, name_file=f"pagina_{i+1}.html")


if __name__ == "__main__":
    main()
