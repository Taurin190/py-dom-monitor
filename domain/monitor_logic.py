from domain.dom_diff import DomDiff


class MonitorLogic:
    def __init__(self, client, database, notification, config):
        self.client = client
        self.database = database
        self.notification = notification
        self.config = config

    def exec(self):
        exec_count = self.database.get_exec_count()
        prev_html = self.database.get_previous_html()
        current_html = self.client.get_html(self.config["url"])
        diff_tool = DomDiff(self.config)
        results = diff_tool.compare(prev_html, current_html)
        return results
