from domain.dom_diff import DomDiff


class MonitorLogic:
    def __init__(self, client, database, notification, config):
        self.client = client
        self.database = database
        self.notification = notification
        self.config = config
        if "threshold" in self.config.keys():
            self.threshold = self.config["threshold"]
        else:
            self.threshold = 20

    def exec(self):
        results = ""
        exec_count = self.database.get_exec_count()
        current_html = self.client.get_html(self.config["url"])
        if exec_count != 1:
            prev_html = self.database.get_previous_html()
            diff_tool = DomDiff()
            diff_results = diff_tool.compare(prev_html, current_html)
            problem_list = self._handle_diff_list(diff_results, exec_count)
            self.notification.send_problem_list(problem_list)
        self.database.update_previous_html(current_html)
        self.database.update_exec_count()
        return results

    def _handle_diff_list(self, diff_list, exec_count):
        diff_data_list = []
        problem_list = []
        for diff in diff_list:
            diff_data_list.append(self.database.insert_or_update_diff(diff))
        for diff_data in diff_data_list:
            appearance_rate = 100 * diff_data["count"] / exec_count
            if appearance_rate < self.threshold:
                problem_list.append(diff_data)

        return problem_list
