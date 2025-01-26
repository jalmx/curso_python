from peewee import *
from datetime import datetime

db = SqliteDatabase("components.db")

class Component(Model):
    id = AutoField()
    name = CharField()
    code = CharField(unique=True)
    description = CharField()
    quantity = IntegerField(default=0)
    power = FloatField(null=True)
    date_register = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"code: {self.code} - name: {self.name} - date: {self.date_register}"
    class Meta:
        database = db
        db_table = "component"


if __name__ == "__main__":

    if not Component.table_exists():
        Component.create_table()

    # Component.create(name="resistencia R10", code="r10", description=f"Resistencia de 10 ohms", quantity=5)
    # Component.create(name="capacitor 4.7u", code="c4.7u", description=f"capacitor de 4.7uF a 50V", quantity=5)
    # Component.create(name="microcontrolador ATMEGA328P", code="ATMEGA328P", description=f"microcontrolador ATMEGA328P AVR 8-bits PDIP28", quantity=5)

    component = Component.get(Component.id == "2")
    print(component)


