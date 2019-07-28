from client.requests_client import RequestClient
from client.selenium_client import SeleniumClient
from model.db import Database


class DomMonitor:
    def exec(self, **args):
        pass

    @staticmethod
    def get_client(config):
        if config == "request":
            return RequestClient()
        elif config == "selenium":
            return SeleniumClient()
        else:
            return RequestClient()

    @staticmethod
    def get_database(config, setting):
        return Database()
