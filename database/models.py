from peewee import (SqliteDatabase, Model,
    CharField, IntegerField, AutoField,
    ForeignKeyField, DateField, BooleanField)

from config_data.config import DB_DYNAMIC_PATH, DB_STATIC_PATH
from database import static_data


db_dynamic = SqliteDatabase(DB_DYNAMIC_PATH)
db_static = SqliteDatabase(DB_STATIC_PATH)


class Dynamic(Model):
    class Meta:
        database = db_dynamic

class User(Dynamic):
    user_id = IntegerField(primary_key=True)
    user_name = CharField()

class Words(Dynamic):
    word_id = AutoField()
    word_name = CharField()
    word_count = IntegerField()


class Static(Model):
    class Meta:
        database = db_static

class DB_Coll(Static):
    coll_id = IntegerField(primary_key=True)
    coll_name = CharField()

class DB_Method(Static):
    met_id = AutoField()
    met_coll = ForeignKeyField(DB_Coll, backref='method')
    met_name = CharField()
    met_desc = CharField()

    def __str__(self) -> str:
        return f'<b>{self.met_name}</b>:  {self.met_desc}'


def create_models():
    db_dynamic.create_tables(Dynamic.__subclasses__())


def filling_static_db():
    db_dynamic.create_tables(Static.__subclasses__())

    for coll_id, coll_name in static_data.dump['collections'].items():
        DB_Coll.create(
            coll_id=coll_id,
            coll_name=coll_name
            )
        
    for met_coll, method in static_data.dump['methods'].items():
        for met_name, met_desc in method.items():
            DB_Method.create(
                met_coll=met_coll,
                met_name=met_name,
                met_desc=met_desc
            )
    