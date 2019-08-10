from model.db import Database
from pymongo import MongoClient
import urllib.parse


class Mongo(Database):
    def __init__(self, setting):
        self.setting = setting
        username = urllib.parse.quote_plus(setting['username'])
        password = urllib.parse.quote_plus(setting['password'])
        self.client = MongoClient('mongodb://%s:%s@%s:%s/%s' % (
            username, password,
            setting['hostname'],
            setting['port'],
            setting['database']
        ))
        self.db = self.client[setting['database']]
        if not "exec-count" in self.db.collection_names():
            self.db.create_collection("exec-count")
        if not "prev-html" in self.db.collection_names():
            self.db.create_collection("prev-html")

    def __del__(self):
        self.client.close()

    def insert(self, count, prev_html):
        self.db["exec-count"].insert_one(count)
        self.db["prev-html"].insert_one(prev_html)

    def drop(self):
        self.db.drop_collection("exec-count")
        self.db.drop_collection("prev-html")

    def get_exec_count(self):
        count_data = self.db["exec-count"].find_one()
        return count_data["count"]

    def get_previous_html(self):
        html_data = self.db["prev-html"].find_one()
        return html_data["html"]

    def update_exec_count(self):
        pass

    def update_previous_html(self):
        pass
