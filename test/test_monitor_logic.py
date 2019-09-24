from domain.monitor_logic import MonitorLogic
from client.client import Client
from model.db import Database
from unittest import TestCase


class TestMonitorLogic(TestCase):
    def setUp(self):
        self.client = ClientMock()
        database = DBMock()
        notification = NotificationMock()
        config = {"url": "http://test.com"}
        self.monitor = MonitorLogic(self.client, database, notification, config)

    def test_exec(self):
        actual = self.monitor.exec()
        self.assertEqual("", actual)

    def test_exec_with_diff(self):
        self.monitor.exec()
        self.client.set_html("<html><body><h1>TEST2</h1></body></html>")
        actual = self.monitor.exec()
        self.assertEqual(["html > body > h1"], actual)

    def test_exec_with_404page(self):
        self.client.set_exception("404 Not Found Error")
        actual = self.monitor.exec()
        self.assertEqual("Error Occur\n\t404 Not Found Error", actual)


class ClientMock(Client):
    def __init__(self):
        self.html = "<html><body><h1>TEST</h1></body></html>"
        self.exception = None

    def set_html(self, html):
        self.html = html

    def set_exception(self, exception):
        self.exception = exception

    def get_html(self, url):
        if self.exception:
            raise Exception(self.exception)
        return self.html


class DBMock(Database):
    def __init__(self):
        self.count = 1
        self.html = "<html><body><h1>TEST</h1></body></html>"

    def set_exec_count(self, count):
        self.count = count

    def get_exec_count(self):
        return self.count

    def get_previous_html(self):
        return self.html

    def update_exec_count(self):
        self.count += 1

    def update_previous_html(self, html):
        self.html = html

    def insert_or_update_diff(self, diff):
        return {"diff": diff, "id": 1, "count": 1}


class NotificationMock:
    def send_slack_message(self, message):
        pass

    def send_problem_list(self, problem_list):
        pass
