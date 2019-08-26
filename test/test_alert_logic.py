from domain.alert_logic import AlertLogic
from unittest import TestCase


class TestAlertLogic(TestCase):
    def test_send_slack_message(self):
        alert = AlertLogic(slack_client=SlackMock())
        text = alert.send_slack_message("test")
        self.assertEqual("test", text)

    def test_send_problem_list(self):
        problem_list = [{
            "diff": "html > body > h1",
            "count": 1
        }]
        alert = AlertLogic(slack_client=SlackMock())
        actual = alert.send_problem_list(problem_list)
        self.assertEqual(
            "[Alert] Following dom has critical diff\n"
            "\thtml > body > h1\n",
            actual
        )


class SlackMock:
    class Slack:
        def __init__(self, url):
            self.url = url

        def notify(self, text):
            return text
