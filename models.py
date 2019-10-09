from flask_login import UserMixin
import os
import datetime
from peewee import *
from playhouse.db_url import connect


# DATABASE = SqliteDatabase('data2.sqlite')
DATABASE = connect(os.environ.get(
    'https://art-thoughts-with-flask.herokuapp.com/'))


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
    query_string = CharField(null=True)
    exclusions = CharField(null=True)
    cached_ID = CharField(null=True)
    initial_value = IntegerField(default=0, null=True)
    search_num = IntegerField(default=0, null=True)
    was_selected = BooleanField(default=False, null=True)
    search_num = IntegerField(default=0, null=True)
    user_id = IntegerField(default=0, null=True)

    class Meta:
        database = DATABASE


class Select(Model):
    current_time = DateTimeField(default=datetime.datetime.now, null=True)
    search_num = IntegerField(default=0, null=True)
    search_query = CharField(null=True)
    search_target = CharField(null=True)
    search_remainder = CharField(null=True)
    snippet = CharField(null=True)
    cached_ID = CharField(null=True)
    link_url = CharField(null=True)
    title = CharField(null=True)
    user_id = IntegerField(default=0, null=True)
    was_selected = BooleanField(default=True, null=True)
    image_info = TextField(null=True)

    class Meta:
        database = DATABASE


class Source(Model):
    cached_ID = CharField(null=True)
    current_time = DateTimeField(default=datetime.datetime.now, null=True)
    query_string = CharField(null=False)
    initial_value = IntegerField(default=0, null=True)
    search_num = IntegerField(default=0, null=True)
    # all results of search creation triggered on selection?
    base_url = TextField(null=True)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Data, Source, Select], safe=True)
    print("Data TABLES created")
    DATABASE.close()
