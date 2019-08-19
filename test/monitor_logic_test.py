from domain.monitor_logic import MonitorLogic
from client.client import Client
from model.db import Database
from unittest import TestCase


class MonitorLogicTest(TestCase):
    def setUp(self):
        client = ClientMock()
        database = DBMock()
        notification = NotificationMock()
        config = {"url": "http://test.com"}
        self.monitor = MonitorLogic(client, database, notification, config)

    def test_exec(self):
        actual = self.monitor.exec()
        self.assertEqual("", actual)


class ClientMock(Client):
    def __init__(self):
        self.html = "<html><body><h1>TEST</h1></body></html>"

    def set_html(self, html):
        self.html = html

    def get_html(self, url):
        return self.html


class DBMock(Database):
    def __init__(self):
        self.count = 1

    def set_exec_count(self, count):
        self.count = count

    def get_exec_count(self):
        return self.count

    def get_previous_html(self):
        return "<html><body><h1>TEST</h1></body></html>"

    def update_exec_count(self):
        pass

    def update_previous_html(self, html):
        pass


class NotificationMock:
    def send_slack_message(self, message):
        pass
