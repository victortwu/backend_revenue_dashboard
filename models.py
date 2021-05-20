from peewee import *
import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('revenue.sqlite')

# class User(UserMixin, Model):
#     username = CharField(unique=True)
#     email = CharField(unique=True)
#     password = CharField()
#
#     class Meta:
#         database = DATABASE
