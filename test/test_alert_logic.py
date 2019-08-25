from domain.alert_logic import AlertLogic
from unittest import TestCase


class TestAlertLogic(TestCase):
    def test_send_slack_message(self):
        alert = AlertLogic(slack_client=SlackMock())
        text = alert.send_slack_message("test")
        self.assertEqual("test", text)


class SlackMock:
    class Slack:
        def __init__(self, url):
            self.url = url

        def notify(self, text):
            return text
