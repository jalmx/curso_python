from random import random
from component import Component

if __name__ == "__main__":
    if not Component.table_exists():
        Component.create_table()

    Component.create(name="R1k", code="r1k", description="Resistencia de 1k", quantity= int(random()*1000))
    Component.create(name="C10u", code="c10u", description="Capacitor de 10uF",quantity= int(random()*1000))
    Component.create(name="16f84", code="PIC16F84A", description="Un microcontrolador de 8 bits",quantity= int(random()*1000))

    components = Component.select()
    for component in components:
        print(component)

    component = Component.get(Component.id == 2)
    component.quantity = 1000
    component.save()
    print("-------------------------")
    components = Component.select()
    for component in components:
        print(component)
