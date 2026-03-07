import os
import csv
from component import Component


class Inventory:

    def __init__(self, file_name="inventory.csv"):
        self.components = []# guarda o mantiene los componentes en memoria
        self.file_name = file_name

        if not self._exit_csv():
            self._create_csv()
        else:
           self._load_data()

    def _exit_csv(self):
        """Revisar si existe mi db"""
        return os.path.exists(self.file_name)

    def _create_csv(self):
        with open(self.file_name, mode="w+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(Component.get_columns())

    def _load_data(self):
        with open(self.file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                component = Component(
                    id=row[Component.get_columns()[0]],
                    name=row[Component.get_columns()[1]],
                    description=row[Component.get_columns()[2]],
                )
                self.components.append(component)

    def view_inventory(self):
        print("=" * 80)
        for component in self.components:
            print(component)
        print("=" * 80)

    def _save_data(self):
        with open(self.file_name, mode="w+", newline="") as file:
            fields = Component.get_columns()
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()

            for component in self.components:
                writer.writerow(
                    {
                        Component.get_columns()[0]: component.id,
                        Component.get_columns()[1]: component.name,
                        Component.get_columns()[2]: component.description,
                    }
                )

    def add_component(self, new_component):
        self.components.append(new_component)
        self._save_data()
        print("Component added successfully :D")
