from model.db import Database
from pymongo import MongoClient
from pymongo import DESCENDING
import urllib.parse


class Mongo(Database):
    EXEC_COUNT_COL = "exec_count"
    PREV_HTML_COL = "prev_html"
    PREV_DIFF_COL = "prev_diff"

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
        if not Mongo.EXEC_COUNT_COL in self.db.list_collection_names():
            self.db.create_collection(Mongo.EXEC_COUNT_COL)
            self.db[Mongo.EXEC_COUNT_COL].insert_one({"count": 1, "id": 1})
        if not Mongo.PREV_HTML_COL in self.db.list_collection_names():
            self.db.create_collection(Mongo.PREV_HTML_COL)
            self.db[Mongo.PREV_HTML_COL].insert_one({"html": "", "id": 1},)
        if not Mongo.PREV_DIFF_COL in self.db.list_collection_names():
            self.db.create_collection(Mongo.PREV_DIFF_COL)

    def __del__(self):
        self.client.close()

    def insert(self, prev_html, prev_diff):
        self.update_previous_html(prev_html)
        self.db[Mongo.PREV_DIFF_COL].insert_one(prev_diff)

    def drop(self):
        self.db.drop_collection(Mongo.EXEC_COUNT_COL)
        self.db.drop_collection(Mongo.PREV_HTML_COL)
        self.db.drop_collection(Mongo.PREV_DIFF_COL)

    def get_exec_count(self):
        count_data = self.db[Mongo.EXEC_COUNT_COL].find_one()
        if not count_data:
            self.db[Mongo.EXEC_COUNT_COL].insert_one({"count": 1, "id": 1})
            return 1
        return count_data["count"]

    def get_previous_html(self):
        html_data = self.db[Mongo.PREV_HTML_COL].find_one()
        return html_data["html"]

    def update_exec_count(self):
        prev_count = int(self.db[Mongo.EXEC_COUNT_COL].find_one()["count"])
        self.db[Mongo.EXEC_COUNT_COL].find_one_and_update({"id": 1}, {'$set': {"count": prev_count + 1}})

    def update_previous_html(self, new_html):
        self.db[Mongo.PREV_HTML_COL].find_one_and_update({"id": 1}, {'$set': {"html": new_html}})

    def find_diff_from_previous(self, target):
        return self.db[Mongo.PREV_DIFF_COL].find_one({"diff": target})

    def insert_previous_diff(self, diff):
        diff_id = 1 + self._get_previous_diff_max_id()
        self.db[Mongo.PREV_DIFF_COL].insert_one({"id": diff_id, "diff": diff, "count": 1})

    def insert_or_update_diff(self, diff):
        exist_diff = self.find_diff_from_previous(diff)
        if exist_diff:
            self.db[Mongo.PREV_DIFF_COL].find_one_and_update(
                {"diff": exist_diff["diff"]}, {'$set': {"count": int(exist_diff["count"]) + 1}}
            )
            return self.find_diff_from_previous(diff)
        diff_id = self._get_previous_diff_max_id() + 1
        new_record = {"diff": diff, "id": diff_id, "count": 1}
        self.db[Mongo.PREV_DIFF_COL].insert_one(new_record)
        return self.find_diff_from_previous(diff)

    def _get_previous_diff_max_id(self):
        max_id = 0
        results = self.db[Mongo.PREV_DIFF_COL].find().sort('id', DESCENDING).limit(1)
        for c in results:
            if max_id < int(c["id"]):
                max_id = int(c["id"])
        return max_id

    def update_previous_diff(self, target):
        target_diff = self.find_diff_from_previous(target)
        self.db[Mongo.PREV_DIFF_COL].update_one({"diff": target}, {'$set': {"count": int(target_diff["count"]) + 1}})
