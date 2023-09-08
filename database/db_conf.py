from peewee import (SqliteDatabase, Model,
    CharField, IntegerField, AutoField, 
    ForeignKeyField, DateField, BooleanField)

from config_data.config import DB_DYNAMIC_PATH, DB_STATIC_PATH


db_dynamic = SqliteDatabase(DB_DYNAMIC_PATH)
db_static = SqliteDatabase(DB_STATIC_PATH)


class Dynamic(Model):
    class Meta:
        database = db_dynamic

class User(Dynamic):
    user_id = IntegerField(primary_key=True)
    user_name = CharField()
    user_lang = CharField()


class Static(Model):
    class Meta:
        database = db_static

# class DB_Python(Static):
#     py_id = AutoField()
#     py_name = ForeignKeyField()

class DB_Coll(Static):
    coll_id = AutoField()
    coll_name = CharField()

class DB_Method(Static):
    met_id = AutoField()
    met_coll = ForeignKeyField(DB_Coll, backref="methods")
    met_name = CharField()
    met_desc = CharField()


def create_models():
    db_dynamic.create_tables(Dynamic.__subclasses__())


def filling_static_db():
    pass  # TODO доработать заполнение базы данных собственно данными из дампа
    