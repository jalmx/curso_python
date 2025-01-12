from peewee import *

db = SqliteDatabase("components.db")

class Component(Model):
    id =
    name = CharField()
    description = CharField()
    quantity = IntegerField()
    date_register = DateTimeField()

    class Meta:
        database = db
