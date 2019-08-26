
class Database:
    def get_exec_count(self):
        raise NotImplementedError()

    def get_previous_html(self):
        raise NotImplementedError()

    def update_exec_count(self):
        raise NotImplementedError()

    def update_previous_html(self, html):
        raise NotImplementedError()

    def find_diff_from_previous(self, target):
        raise NotImplementedError()

    def insert_previous_diff(self, diff):
        raise NotImplementedError()

    def insert_or_update_diff(self, diff):
        raise NotImplementedError()
