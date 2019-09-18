from domain.alert_logic import AlertLogic
from unittest import TestCase
import sys
from io import StringIO


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
        self.assertEqual([
            "[Alert] Following dom has critical diff\n"
            "\tTotal Count: 1\n",
            "```\n"
            "\thtml > body > h1\n\n"
            "```\n"],
            actual
        )

    def test_send_problem_list_with_several_problems(self):
        problem_list = [
            {
                "diff": "html > body > h1",
                "count": 1
            },
            {
                "diff": "html > body > h2",
                "count": 2
            }
        ]
        alert = AlertLogic(slack_client=SlackMock())
        actual = alert.send_problem_list(problem_list)
        self.assertEqual([
            "[Alert] Following dom has critical diff\n"
            "\tTotal Count: 2\n",
            "```\n"
            "\thtml > body > h1\n\n"
            "\thtml > body > h2\n\n"
            "```\n"
        ],
            actual
        )

    def test_send_problem_list_with_empty_list(self):
        problem_list = []
        alert = AlertLogic(slack_client=SlackMock())
        org_stdout, sys.stdout = sys.stdout, StringIO()
        actual = alert.send_problem_list(problem_list)
        self.assertIsNone(actual)
        self.assertEqual("No critical diff was found\n", sys.stdout.getvalue())
        sys.stdout = org_stdout


class SlackMock:
    class Slack:
        def __init__(self, url):
            self.url = url

        def notify(self, text):
            return text
