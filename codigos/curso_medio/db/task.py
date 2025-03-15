from peewee import *
from datetime import datetime

db = SqliteDatabase("task.db")

class Task(Model):

    id = AutoField()
    name = CharField()
    description = CharField(null=True)
    state = BooleanField(default=False)
    date_register = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"id:{self.id}, name: {self.name}, state:{self.state}"

    class Meta:
        database = db
        db_table = "tasks"
