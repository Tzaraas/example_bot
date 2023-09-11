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
    user_name = CharField(null=False)

class Words(BaseModel):
    word_id = AutoField()
    word_user_id = IntegerField(null=False, unique=True)
    word_name = CharField(null=False)
    word_count = IntegerField(null=False)


def create_models():
    db.create_tables(BaseModel.__subclasses__())
    