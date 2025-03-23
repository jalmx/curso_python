from peewee import *

db = SqliteDatabase("components.db")


class ModelComponent(Model):
    id = AutoField()
    name = CharField(max_length=20)
    code = CharField(max_length=10)
    description = TextField(null=True)
    count = IntegerField(default=0)
    location = CharField(default="NA")
    status = BooleanField(default=False)

    def __str__(self):
        return f"[id]: {self.id} - [name] {self.name} - [code]:{self.code} - [count]: {self.count} - [location]: {self.location}"

    class Meta:
        database = db


class Component:

    def __init__(self, name, code, description=None, id=None, location="N/A", count=0):
        self.id = id
        self.name = name
        self.description = description
        self.code = code
        self.count = count
        self.location = location

    def __str__(self):
        return f"[id]: {self.id} - [name] {self.name} - [code]:{self.code} - [count]: {self.count} - [location]: {self.location}"

    @staticmethod
    def get_columns():
        return ["id", "Name", "Code", "Count", "Description", "Location", "Status"]

    def get_model(self):
        model = {
            "name": self.name,
            "code": self.code,
            "count": self.count,
            "description": self.description,
            "location": self.location,
            "status": bool(self.count),
        }

        if id:
            model["id"] = self.id

        return ModelComponent(**model)

    @staticmethod
    def get_component(component: ModelComponent):
        return Component(
            id=component.id,
            name=component.name,
            code=component.code,
            description=component.description if component.description else "",
            location=component.location if component.location else "",
            count=component.count,
        )
