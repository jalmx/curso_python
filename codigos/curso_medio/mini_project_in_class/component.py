import uuid


class Component:

    @staticmethod
    def generate_id():
        return uuid.uuid4()

    def __init__(self, name, description="", id=0):

        self.id = Component.generate_id() if id == 0 else id
        print(self.id)
        self.name = name
        self.description = description

    def __str__(self):
        return f"My component: id-> {self.id} - name: {self.name}"

    @staticmethod
    def get_columns():
        return ["ID", "Name", "Description"]
