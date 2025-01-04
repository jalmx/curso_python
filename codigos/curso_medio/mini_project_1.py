import csv


class Component:
    """
    Represents an electronic component in the inventory.

    Attributes:
        component_id (str): Unique identifier for the component.
        name (str): Name of the component.
        quantity (int): Quantity of the component in stock.
        unit_price (float): Price per unit of the component.
    """

    def __init__(self, component_id, name, quantity, unit_price):
        """
        Initializes a Component instance.

        Args:
            component_id (str): The ID of the component.
            name (str): The name of the component.
            quantity (int): The quantity of the component.
            unit_price (float): The unit price of the component.
        """
        self.component_id = component_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        """
        Returns a string representation of the component.

        Returns:
            str: A formatted string containing the component's details.
        """
        return f"ID: {self.component_id}, Name: {self.name}, Quantity: {self.quantity}, Unit Price: {self.unit_price}"


class Inventory:
    """
    Manages a list of electronic components, including operations for
    adding, removing, listing, and searching components. Data is stored
    persistently in a CSV file.

    Attributes:
        csv_file (str): Path to the CSV file used for storing inventory data.
        components (list): List of Component objects in the inventory.
    """

    def __init__(self, csv_file):
        """
        Initializes the Inventory instance and loads data from the CSV file.

        Args:
            csv_file (str): Path to the CSV file for inventory data.
        """
        self.csv_file = csv_file
        self.components = []
        self.load_data()

    def load_data(self):
        """
        Loads inventory data from the CSV file into memory.
        If the file does not exist, no data is loaded.
        """
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    component = Component(
                        row['ID'],
                        row['Name'],
                        int(row['Quantity']),
                        float(row['Unit Price'])
                    )
                    self.components.append(component)
        except FileNotFoundError:
            print("CSV file not found. A new file will be created upon saving data.")

    def save_data(self):
        """
        Saves the current inventory data to the CSV file.
        """
        with open(self.csv_file, mode='w', newline='') as file:
            fields = ['ID', 'Name', 'Quantity', 'Unit Price']
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for component in self.components:
                writer.writerow({
                    'ID': component.component_id,
                    'Name': component.name,
                    'Quantity': component.quantity,
                    'Unit Price': component.unit_price
                })

    def add_component(self, component_id, name, quantity, unit_price):
        """
        Adds a new component to the inventory.

        Args:
            component_id (str): The ID of the component.
            name (str): The name of the component.
            quantity (int): The quantity of the component.
            unit_price (float): The unit price of the component.
        """
        for component in self.components:
            if component.component_id == component_id:
                print("Error: A component with this ID already exists.")
                return
        new_component = Component(component_id, name, quantity, unit_price)
        self.components.append(new_component)
        self.save_data()
        print("Component added successfully.")

    def remove_component(self, component_id):
        """
        Removes a component from the inventory by its ID.

        Args:
            component_id (str): The ID of the component to remove.
        """
        for component in self.components:
            if component.component_id == component_id:
                self.components.remove(component)
                self.save_data()
                print("Component removed successfully.")
                return
        print("Error: Component with this ID not found.")

    def list_components(self):
        """
        Lists all components in the inventory.
        """
        if not self.components:
            print("No components in inventory.")
        else:
            for component in self.components:
                print(component)

    def find_component(self, component_id):
        """
        Searches for a component in the inventory by its ID.

        Args:
            component_id (str): The ID of the component to search for.
        """
        for component in self.components:
            if component.component_id == component_id:
                print(component)
                return
        print("Error: Component with this ID not found.")


# Main program
if __name__ == "__main__":
    """
    Entry point of the program. Provides a menu for managing the inventory.
    """
    inventory = Inventory("components_inventory.csv")

    while True:
        print("\nMenu:")
        print("1. Add Component")
        print("2. Remove Component")
        print("3. List Components")
        print("4. Find Component by ID")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            component_id = input("Component ID: ")
            name = input("Component Name: ")
            quantity = int(input("Quantity: "))
            unit_price = float(input("Unit Price: "))
            inventory.add_component(component_id, name, quantity, unit_price)

        elif option == "2":
            component_id = input("Enter the ID of the component to remove: ")
            inventory.remove_component(component_id)

        elif option == "3":
            inventory.list_components()

        elif option == "4":
            component_id = input("Enter the ID of the component to find: ")
            inventory.find_component(component_id)

        elif option == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
