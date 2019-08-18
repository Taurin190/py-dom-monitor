from domain.dom_diff import DomDiff


class MonitorLogic:
    def __init__(self, client, database, notification, config):
        self.client = client
        self.database = database
        self.notification = notification
        self.config = config

    def exec(self):
        results = ""
        exec_count = self.database.get_exec_count()
        current_html = self.client.get_html(self.config["url"])
        if exec_count != 1:
            prev_html = self.database.get_previous_html()
            diff_tool = DomDiff()
            diff_results = diff_tool.compare(prev_html, current_html)

        self.database.update_previous_html(current_html)
        self.database.update_exec_count()
        return results
