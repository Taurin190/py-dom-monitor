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
            DomMonitor.print_error("ERROR: this command need args of config file")
            print("usage: dommonitor config_file")
            exit(1)
        arg_config = args[1]
        current_path = os.getcwd()
        config_path = current_path + "/" + arg_config
        if not os.path.exists(config_path):
            DomMonitor.print_error("ERROR: invalid args of config file")
            print("usage: dommonitor config_file")
            exit(1)

        config = configparser.ConfigParser()
        config.read(config_path)
        client = DomMonitor.get_client(config["app"]["client"])
        db = DomMonitor.get_database(config["app"]["db_type"], config["database"])
        slack_conf = None
        if config.has_option("app", "slack_config"):
            slack_conf = config["app"]["slack_config"]
        notification = DomMonitor.get_notification(config, slack_conf)
        domain = DomMonitor.get_domain(client, db, notification, config["app"])
        domain.exec()

    @staticmethod
    def print_error(message):
        # show error message with red color
        print('\033[31m' + message + '\033[0m')

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
    def get_notification(config, config_file_path=None):
        return AlertLogic(config_file_path=config_file_path, target_url=config["app"]["url"])

    @staticmethod
    def get_domain(client, database, notification, config):
        return MonitorLogic(client, database, notification, config)
