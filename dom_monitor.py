import os
import configparser

from client.requests_client import RequestClient
from client.selenium_client import SeleniumClient
from model.mongo import Mongo
from model.file import File
from domain.alert_logic import AlertLogic
from domain.monitor_logic import MonitorLogic


class DomMonitor:
    def exec(self, *args):
        if len(args) < 2:
            exit(1)
        arg_config = args[1]
        current_path = os.getcwd()
        config = configparser.ConfigParser()
        config.read(current_path + "/" + arg_config)
        client = DomMonitor.get_client(config["app"]["client"])
        db = DomMonitor.get_database(config["app"]["db_type"], config["database"])
        notification = DomMonitor.get_notification(config)
        domain = DomMonitor.get_domain(client, db, notification, config["app"])
        domain.exec()

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
    def get_notification(config, setting=None):
        return AlertLogic(setting)

    @staticmethod
    def get_domain(client, database, notification, config):
        return MonitorLogic(client, database, notification, config)
