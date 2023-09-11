from peewee import (SqliteDatabase, Model,
    CharField, IntegerField, AutoField,
    ForeignKeyField, DateField, BooleanField)

from config_data.config import DB_PATH


db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    user_name = CharField()

class Words(BaseModel):
    word_id = AutoField()
    word_name = CharField()
    word_count = IntegerField()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
    