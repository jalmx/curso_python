from peewee import *
from datetime import datetime

db = SqliteDatabase("components.db")

class Component(Model):

    id = AutoField()
    name = CharField()
    code = CharField(max_length=10)
    description = CharField(null=True)
    quantity = IntegerField(default=0)
    date_register = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"id:{self.id}, code: {self.code}, name:{self.name}"

    class Meta:
        database = db
        db_table = "component"
