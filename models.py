from peewee import *
from flask_login import UserMixin
import os
import datetime
from playhouse.db_url import connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = SqliteDatabase('data2.sqlite')

class Data(Model):
    current_time = DateTimeField(default=datetime.datetime.now, null=True)
    query_string = CharField(null=True)
    exclusions = CharField(null=True)
    cached_ID = CharField(null=True)
    initial_value = IntegerField(default=0, null=True)
    search_num = IntegerField(default=0, null=True)
    was_selected = BooleanField(default=False, null=True)
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
