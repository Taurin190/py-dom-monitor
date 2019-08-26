from model.db import Database


class File(Database):
    def __init__(self, setting):
        self.setting = setting

    def get_exec_count(self):
        pass

    def get_previous_html(self):
        pass

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
