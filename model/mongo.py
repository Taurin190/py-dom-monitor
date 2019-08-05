from model.db import Database
from pymongo import MongoClient
import urllib.parse


class Mongo(Database):
    def __init__(self, setting):
        self.setting = setting
        username = urllib.parse.quote_plus(setting['username'])
        password = urllib.parse.quote_plus(setting['password'])
        self.client = MongoClient('mongodb://%s:%s@%s:%s/' % (username, password, setting['hostname'], setting['port']))
        self.col = self.client[setting['database']][setting['collection']]

    def __del__(self):
        self.client.close()

    def get_exec_count(self):
        pass

    def get_previous_html(self):
        pass

    def update_exec_count(self):
        pass

    def update_previous_html(self):
        pass
