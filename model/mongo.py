from model.db import Database


class Mongo(Database):
    def __init__(self, setting):
        self.setting = setting

    def get_exec_count(self):
        pass

    def get_previous_html(self):
        pass

    def update_exec_count(self):
        pass

    def update_previous_html(self):
        pass
