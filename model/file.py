from model.db import Database
import os
import os.path
import json


class File(Database):
    def __init__(self, setting):
        self.setting = setting
        if not os.path.exists("exec_count.txt"):
            with open('exec_count.txt', 'w') as f:
                f.write("1")
        if not os.path.exists("previous_html.json"):
            with open("previous_html.json", "w") as f:
                f.write("")

    def get_exec_count(self):
        with open("exec_count.txt", "r") as f:
            if f:
                count = int(f.read())
            else:
                count = 1
        return count

    def drop(self):
        os.remove('exec_count.txt')
        os.remove('previous_html.json')
        os.remove('previous_diff.json')

    def insert_previous_html(self, html):
        with open("previous_html.json", "w") as f:
            f.write(str({"html": html}))

    def get_previous_html(self):
        with open("previous_html.json", "r") as f:
            if f:
                s = f.read()
                s = s.replace("'", "\"")
                return json.loads(s)
        return ""

    def update_exec_count(self):
        current_count = int(self.get_exec_count())
        with open("exec_count.txt", "w") as f:
            f.write(str(current_count + 1))

    def update_previous_html(self, html):
        pass

    def find_diff_from_previous(self, target):
        with open("previous_diff.json", "r") as f:
            s = f.read()
            s = s.replace("'", "\"")
            diff_list = json.loads(s)
        for diff_json in diff_list:
            if diff_json["diff"] == target:
                return diff_json
        return

    def insert_previous_diff(self, diff):
        with open("previous_diff.json", "w") as f:
            f.write(str([{"id": 1, "count": 1, "diff": diff}]))

    def _get_all_previous_diff_json(self):
        return []

    def insert_or_update_diff(self, diff):
        pass
