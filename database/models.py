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
    word_user_id = IntegerField(null=False)
    word_name = CharField(null=False)
    word_count = IntegerField(null=False)


class Cities(BaseModel):
    city_id = AutoField()
    city_name = CharField(null=False)
    city_count = IntegerField(null=False)

    def __str__(self) -> str:
        return f"Город {self.city_name} - запросов всего: {self.city_count}."


class Countries(BaseModel):
    country_id = AutoField()
    country_name = CharField(null=False)
    country_count = IntegerField(null=False)

    def __str__(self) -> str:
        return f"Страна {self.country_name} - запросов всего: {self.country_count}."

 
class Orders(BaseModel):
    order_id = AutoField()
    order_local = IntegerField(null=False, unique=True)
    order_date = DateField(null=False)
    order_total = IntegerField(null=False)
    order_customer = CharField(null=False)
    order_user_id = IntegerField(null=False)

class Products(BaseModel):
    product_id = AutoField()
    product_name = IntegerField(null=False)
    product_price = IntegerField(null=False)
    product_order = ForeignKeyField(Orders)


def create_models():
    db.create_tables(BaseModel.__subclasses__())
    