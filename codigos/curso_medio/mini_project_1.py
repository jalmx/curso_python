import csv
import os
import uuid


class Component:
    """
    Represents an electronic component in the store.
    Attributes:
        id (str): Unique ID of the component.
        name (str): Name of the component.
        description (str): Description of the component in stock.
        quantity (int): Quantity of the component.
    """

    def __init__(
        self, name: str, description: str = "", quantity: int = 0, id: str | None = None
    ):
        self.id = str(uuid.uuid4())[:6] if not id else id
        self.name = name
        self.description = description
        self.quantity = quantity

    @staticmethod
    def get_columns():
        return [
            "ID",
            "Name",
            "Description",
            "Quantity",
        ]

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, description {self.description}, quantity: {self.quantity}"


class Inventory:
    """
    Manages the inventory of electronic components.
    Attributes:
        file_name (str): Name of the CSV file used to store component data.
    Methods:
        add_component(): Adds a new component to the inventory.
        update_component(): Updates the details of an existing component.
        delete_component(): Deletes a component from the inventory.
        view_inventory(): Displays all components in the inventory.
        _save_data(): Saves the inventory to a CSV file.
        _load_data(): Loads inventory data from a CSV file.
    """

    def __init__(self, file_name: str = "inventory.csv"):
        self.components = []
        self.file_name = file_name
        if not self._exist_csv():
            self._create_csv(self.file_name)
        else:
            self._load_data()

    def _exist_csv(self):
        return os.path.exists(self.file_name)

    def _create_csv(self, path_file):
        with open(path_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(Component.get_columns())

    def add_component(self, new_component: Component):
        """
        Adds a new component to the inventory.

        Args:
            component_id (str): The ID of the component.
            name (str): The name of the component.
            quantity (int): The quantity of the component.
            unit_price (float): The unit price of the component.
        """
        self.components.append(self._add(component=new_component))
        self._save_data()
        print("Component added successfully.")

    def _add(self, component: Component):
        return {"id": component.id, "component": component}

    def _save_data(self):
        """
        Saves the current inventory data to the CSV file.
        """
        with open(self.file_name, mode="w+", newline="") as file:
            fields = Component.get_columns()
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for component in self.components:
                component = component["component"]
                writer.writerow(
                    {
                        Component.get_columns()[0]: component.id,
                        Component.get_columns()[1]: component.name,
                        Component.get_columns()[2]: component.description,
                        Component.get_columns()[3]: component.quantity,
                    }
                )

    def update_component(self, id: str, component_to_update: Component):
        """Updates the details of an existing component."""
        old_components = self.components
        self.components = []
        change = False

        for component in old_components:
            if component["id"] == id:
                old_component = component["component"]
                print(f"new update {component_to_update}")
                print(f"old component {old_component}")
                old_component.name = (
                    component_to_update.name
                    if component_to_update.name
                    else old_component.name
                )
                old_component.description = (
                    component_to_update.description
                    if component_to_update.description
                    else old_component.description
                )
                old_component.quantity = (
                    component_to_update.quantity
                    if component_to_update.quantity
                    else old_component.quantity
                )
                change = True
                print("Component updated")
                component = self._add(old_component)
            self.components.append(component)
        if not change:
            print("Not found ID")
        else:
            self._save_data()

    def delete_component(self, component_id):
        """Deletes a component from the inventory."""
        old_components = self.components
        self.components = []
        for component in old_components:
            if not component["id"] == component_id:
                self.components.append(component)
                print(f"Component with ID {component_id} deleted.")
        self._save_data()

    def view_inventory(self):
        """Displays all components in the inventory."""
        print("=" * 80)
        for component in self.components:
            print(component["component"])
        print("=" * 80)

    def _load_data(self):
        """
        Loads inventory data from the CSV file into memory.
        If the file does not exist, no data is loaded.
        """
        if self._exist_csv():
            with open(self.file_name, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    component = Component(
                        id=row[Component.get_columns()[0]],
                        name=row[Component.get_columns()[1]],
                        description=row[Component.get_columns()[2]],
                        quantity=int(row[Component.get_columns()[3]]),
                    )

                    self.components.append(self._add(component))
        else:
            print("CSV file not found. A new file will be created upon saving data.")


if __name__ == "__main__":
    inventory = Inventory()

    while True:
        print("*" * 80)
        print("Electronic Components Inventory Management")
        print("1. Add Component")
        print("2. Update Component")
        print("3. Delete Component")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter component name: ")
            description = input("Enter component description: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_component(
                Component(name=name, description=description, quantity=quantity)
            )
        elif choice == "2":
            component_id = input("Enter component ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            inventory.update_component(
                id=component_id,
                component_to_update=Component(
                    name=name or None,
                    description=description or None,
                    quantity=quantity if int(quantity) else 0,
                ),
            )
            inventory.view_inventory()
        elif choice == "3":
            component_id = input("Enter component ID to delete: ")
            inventory.delete_component(component_id)
        elif choice == "4":
            inventory.view_inventory()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
