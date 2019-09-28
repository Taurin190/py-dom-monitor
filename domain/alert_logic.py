import os
import slackweb
import configparser


class AlertLogic:
    def __init__(self, slack_client=None, config_file_path=None, target_url=None):
        current_path = os.getcwd()
        config = configparser.ConfigParser()
        self.target_url = target_url
        if not config_file_path:
            config_path = current_path + "/config/slack.conf"
        else:
            config_path = current_path + config_file_path
        config.read(config_path)
        if not slack_client:
            self.slack = slackweb.Slack(url=config["slack"]["url"])
        else:
            self.slack = slack_client.Slack(url=config["slack"]["url"])

    def send(self, message):
        return self.send_slack_message(message)

    def send_slack_message(self, message):
        return self.slack.notify(text=message)

    def send_with_template(self, message):
        all_message = ""
        if self.target_url:
            all_message += "URL: " + self.target_url + "\n\n"
        all_message += message
        self.send(all_message)

    def send_problem_list(self, problem_list):
        if len(problem_list) == 0:
            print("No critical diff was found")
            return
        print("There are critical diffs.")
        message = "[Alert] Following dom has critical diff\n"
        message += "\tTotal Count: " + str(len(problem_list)) + "\n"
        result_message = [self.send_with_template(message)]
        for problem_dom in problem_list:
            problem_message = "```\n"
            problem_message += "Ratio: " + str(problem_dom["appearance_rate"]) + "%\n"
            problem_message += "\t" + str(problem_dom["diff"]) + "\n"
            problem_message += "```\n"
            result_message.append(self.send(problem_message))
        return result_message

