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
        diff_list = self._get_all_previous_diff_json()
        for diff_json in diff_list:
            if diff_json["diff"] == target:
                return diff_json
        return

    def insert_previous_diff(self, diff):
        new_id = 1 + self._get_max_id_of_previous_diff()
        current_diff = self._get_all_previous_diff_json()
        new_diff = {"id": new_id, "count": 1, "diff": diff}
        current_diff.append(new_diff)
        with open("previous_diff.json", "w") as f:
            f.write(str(current_diff))
        return new_diff

    def _update_previous_diff(self, diff):
        all_diff_json = self._get_all_previous_diff_json()
        new_all_diff = all_diff_json
        index = 0
        for diff_json in all_diff_json:
            if diff_json["id"] == diff["id"]:
                new_all_diff[index] = diff
                break
            index += 1
        with open("previous_diff.json", "w") as f:
            f.write(str(new_all_diff))
        return diff

    def _get_all_previous_diff_json(self):
        if not os.path.exists("previous_diff.json"):
            return []
        with open("previous_diff.json", "r") as f:
            s = f.read()
            s = s.replace("'", "\"")
            return json.loads(s)

    def _get_max_id_of_previous_diff(self):
        max_id = 0
        if not os.path.exists("previous_diff.json"):
            return max_id
        previous_diff_list = self._get_all_previous_diff_json()
        for previous_diff in previous_diff_list:
            id = int(previous_diff["id"])
            if max_id < id:
                max_id = id
        return max_id

    def insert_or_update_diff(self, diff):
        target_diff = self.find_diff_from_previous(diff)
        if not target_diff:
            return self.insert_previous_diff(diff)
        new_diff = target_diff
        new_diff["count"] = target_diff["count"] + 1
        return self._update_previous_diff(new_diff)
