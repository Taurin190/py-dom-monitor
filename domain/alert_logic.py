import os
import slackweb
import configparser


class AlertLogic:
    def __init__(self, slack_client=None):
        current_path = os.getcwd()
        config = configparser.ConfigParser()
        config.read(current_path + "/config/slack.conf")
        if not slack_client:
            self.slack = slackweb.Slack(url=config["slack"]["url"])
        else:
            self.slack = slack_client.Slack(url=config["slack"]["url"])

    def send(self, message):
        return self.send_slack_message(message)

    def send_slack_message(self, message):
        return self.slack.notify(text=message)

    def send_problem_list(self, problem_list):
        pass

