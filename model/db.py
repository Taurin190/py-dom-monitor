
class Database:
    def get_exec_count(self):
        raise NotImplementedError()

    def get_previous_html(self):
        raise NotImplementedError()

    def update_exec_count(self):
        raise NotImplementedError()

    def update_previous_html(self):
        raise NotImplementedError()
