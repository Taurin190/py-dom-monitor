from domain.alert_logic import AlertLogic
from unittest import TestCase


class AlertLogicTest(TestCase):
    def test_send_slack_message(self):
        alert = AlertLogic(slack_client=SlackMock())
        text = alert.send_slack_message("test")
        self.assertEqual(text, "test")


class SlackMock:
    class Slack:
        def __init__(self, url):
            self.url = url

        def notify(self, text):
            return text