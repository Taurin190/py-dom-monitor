import os
import configparser

from client.requests_client import RequestClient
from client.selenium_client import SeleniumClient
from model.mongo import Mongo
from model.file import File
from notify.notify_slack import NotifySlack
from domain.monitor_logic import MonitorLogic


class DomMonitor:
    def exec(self, *args):
        if len(args) < 1:
            exit(1)
        arg_config = args[0]
        current_path = os.getcwd()
        config = configparser.ConfigParser()
        config.read(current_path + "/" + arg_config)

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

    @staticmethod
    def get_domain(client, database, notification):
        return MonitorLogic(client, database, notification)
