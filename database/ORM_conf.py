from peewee import (SqliteDatabase, Model,
    CharField, IntegerField, AutoField, 
    ForeignKeyField, DateField, BooleanField)
from config_data.config import DB_PATH, DATE_FORMAT


db = SqliteDatabase(DB_PATH)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    user_name = CharField()

class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref="tasks")
    title = CharField()
    due_date = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {check} {title} - {due_date}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[ ]",
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )

def create_models():
    db.create_tables(BaseModel.__subclasses__())
