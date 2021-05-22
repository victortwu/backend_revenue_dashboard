from peewee import *
import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('revenue.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE


class Report(Model):
    date = DateField()
    vendor = CharField()
    wholesale = BooleanField(default=False)
    subtotal = FloatField()
    tax = FloatField()
    fee = FloatField()
    commission = FloatField()
    tip = FloatField()

    class Meta:
        database = DATABASE


def init():
    DATABASE.connect()

    DATABASE.create_tables([Report], safe=True)
    print('Connected to database and created tables.')

    DATABASE.close()
