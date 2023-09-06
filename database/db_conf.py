from peewee import (SqliteDatabase, Model,
    CharField, IntegerField, AutoField, 
    ForeignKeyField, DateField, BooleanField)
import sqlite3
from config_data.config import DB_PATH, DATE_FORMAT


db = SqliteDatabase(DB_PATH)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    user_name = CharField()
    user_lang = CharField()

class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref="tasks")
    title = CharField()
    due_date = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {check} {title} - {due_date}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[  ]",
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )


def get_script(user_id):
        with sqlite3.connect(DB_PATH) as connect:
            script = rf"SELECT `user_lang` FROM `User` WHERE `user_id` == {user_id}"
            cursor = connect.cursor()
            cursor.execute(script)
            return cursor.fetchall()[0][0]
        
        
def set_script(user_id, val):
    with sqlite3.connect(DB_PATH) as connect:
        script = rf"UPDATE `User` SET `user_lang` = '{val}' WHERE `user_id` == {user_id}"
        cursor = connect.cursor()
        cursor.execute(script)
        connect.commit()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
