from client.requests_client import RequestClient
from client.selenium_client import SeleniumClient
from model.mongo import Mongo
from model.file import File
from notify.notify_slack import NotifySlack


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
        if config == "mongo":
            return Mongo(setting)
        elif config == "file":
            return File(setting)
        else:
            return Mongo(setting)

    @staticmethod
    def get_notification(config, setting):
        return NotifySlack(setting)
