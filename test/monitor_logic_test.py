from domain.monitor_logic import MonitorLogic
from client.client import Client
from model.db import Database
from unittest import TestCase


class MonitorLogicTest(TestCase):
    def setUp(self):
        client = ClientMock
        database = DBMock
        notification = NotificationMock
        config = {}
        self.monitor = MonitorLogic(client, database, notification, config)

    def test_failure(self):
        self.fail("fail")


class ClientMock(Client):
    def get_html(self, url):
        pass


class DBMock(Database):
    def get_exec_count(self):
        pass

    def get_previous_html(self):
        pass

    def update_exec_count(self):
        pass

    def update_previous_html(self, html):
        pass


class NotificationMock:
    def send_slack_message(self, message):
        pass
