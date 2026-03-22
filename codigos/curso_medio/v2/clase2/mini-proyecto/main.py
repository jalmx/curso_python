from inventario import Inventario
from componente import Component

if __name__ == "__main__":

    # inventario = Inventario()
    # # for c in range(1,5):
    # #     inventario.agregar_componente(
    # #         Component(nombre=f"resistencia {c*11}", valor=f"{c*11}ohms", codigo=f"R{c*11}")
    # #     )
    # inventario.ver_inventario()
    # # inventario.borrar_componente("229a7a0")
    # inventario.actualizar_componente(
    #     "f1ca699",
    #     Component("capacitor", "4700uF", "c4700", id="f1ca699")
    # )
    # inventario.ver_inventario()

    inventario = Inventario()

    while True:
        print(80 * "*")
        print("INVENTARIO DE COMPONENTES ELECTRONICOS")
        print("1) Ver inventario")
        print("2) Agregar componente")
        print("3) Actualizar componente")
        print("4) Borrar componente")
        print("5) Salir")
        option = int(input())

        if option == 1:
            inventario.ver_inventario()
        elif option == 2:
            name = input("Dame el nombre: ")
            valor = input("Dame el valor: ")
            codigo = input("Dame el codigo: ")
            inventario.agregar_componente(
                Component(nombre=name, valor=valor, codigo=codigo)
            )
        elif option == 3:
            id = input("Dame el id:")
            name = input("Dame el nombre: ")
            valor = input("Dame el valor: ")
            codigo = input("Dame el codigo: ")
            inventario.actualizar_componente(
                id, Component(nombre=name, valor=valor, codigo=codigo, id=id)
            )
        elif option == 4:
            id = input("Dame el id:")
            inventario.borrar_componente(id)
        elif option == 5:
            print("Gracias por usar la aplicacion")
            break
