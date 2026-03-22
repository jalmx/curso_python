# recibe un componen y lo puede guardar, eliminar, actualizar, leer, va a guardar todo en un archivo CSV
import os
import csv
from componente import Component


class Inventario:

    def __init__(self, file_name="inventario.csv"):
        self.__components = []  # aqui estan mis componentes
        self.__inventario_name = file_name

        if not os.path.exists(self.__inventario_name):
            self.__create_inventory(self.__inventario_name)
        else:
            self.__load_inventory()

    def __create_inventory(self, name_file):
        """crea el archivo donde se gestiona el inventario"""
        with open(name_file, mode="w+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(Component.columnas())

    def agregar_componente(self, nuevo_componente: Component):
        self.__components.append(nuevo_componente)
        self.__save_component()  ## se encarga de guarda los componentes
        print(f"componente agregado: {nuevo_componente.description()}")

    def __save_component(self):
        with open(self.__inventario_name, mode="w+", encoding="utf-8") as file:
            columns = Component.columnas()
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            for component in self.__components:
                writer.writerow(
                    {
                        Component.columnas()[0]: component.get_id(),
                        Component.columnas()[1]: component.get_nombre(),
                        Component.columnas()[2]: component.get_valor(),
                        Component.columnas()[3]: component.get_codigo(),
                    }
                )

    def __load_inventory(self):
        if os.path.exists(self.__inventario_name):
            with open(self.__inventario_name, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.__components.append(
                        Component(
                            id=row[Component.columnas()[0]],
                            nombre=row[Component.columnas()[1]],
                            valor=row[Component.columnas()[2]],
                            codigo=row[Component.columnas()[3]],
                        )
                    )
                print("Componentes cargados")
        else:
            print(f"NO ENCONTRE EL INVENTARIO: {self.__inventario_name}")

    def ver_inventario(self):
        print(81 * "*")
        print(f"|\tid\t\t|\tnombre\t\t|\tvalor\t|\tcodigo\t|")
        print(81 * "-")
        for c in self.__components:
            print(
                f"|\t{c.get_id()}\t\t|\t{c.get_nombre()}\t|\t{c.get_valor()}\t|\t{c.get_codigo()}\t|"
            )
        print(81 * "*")

    def borrar_componente(self, id: str) -> str:
        count = 0

        for c in self.__components:
            if c.get_id() == id:
                self.__components.pop(count)
                print("se elimino el componente")
                self.__save_component()
                return id
            count += 1
        print("Componente no exite")

    def actualizar_componente(self, id: str, component: Component):
        count = 0
        for c in self.__components:
            if c.get_id() == id:
                self.__components.pop(count)
                self.__components.insert(count, component)
                self.__save_component()
                print(f"[ACTUALIZADO]: {c.description()}")
                return id
            count += 1
        print("Componente no encontrado")
