from peewee import *
from flask_login import UserMixin
# import os
import datetime
# from playhouse.db_url import connect

DATABASE = SqliteDatabase('data.sqlite')


class User(UserMixin, Model):
    loginTime = DateTimeField(default=datetime.datetime.now)
    username = CharField(unique=True, null=True)
    password = CharField(null=True)
    login = DateTimeField(default=datetime.datetime.now)
    is_active = BooleanField(default=False, null=True)

    class Meta:
        database = DATABASE


class Data(Model):
    current_time = DateTimeField(default=datetime.datetime.now, null=True)
    query_string = CharField(null=False)
    exclusions = CharField(null=True)
    cached_ID = CharField(null=True)
    initial_value = IntegerField(default=0, null=True)
    search_num = IntegerField(default=0, null=True)
    was_selected = BooleanField(default=False, null=True)
    search_num = IntegerField(default=0, null=True)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Data], safe=True)
    print("Data TABLES created")
    DATABASE.close()
