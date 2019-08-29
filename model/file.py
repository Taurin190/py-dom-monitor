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

    def insert_previous_html(self, html):
        with open("previous_html.json", "w") as f:
            f.write(str({"html": html}))

    def get_previous_html(self):
        with open("previous_html.json", "r") as f:
            if f:
                s = f.read()
                print(s)
                print(json.loads(str(s)))
                print(dict(f.read()))
                return dict(f.read())
        return ""

    def update_exec_count(self):
        pass

    def update_previous_html(self, html):
        pass

    def find_diff_from_previous(self, target):
        pass

    def insert_previous_diff(self, diff):
        pass

    def insert_or_update_diff(self, diff):
        pass
