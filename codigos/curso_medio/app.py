from inventory import Inventory
from component import Component
if __name__ == "__main__":

    inventory = Inventory(file_name="mi_db.csv")

    option = 0

    while option != 3:
        print("Almancen Chido de components")
        print("1) Ver listado")
        print("2) Agregar componente")
        print("3) Salir")
        option = int(input())

        if option == 1:
            inventory.view_inventory()
        elif option == 2:
            name = input("Nombre del component: ")
            description = input("Description del componente: ")
            component = Component(name=name, description=description)
            inventory.add_component(component)
