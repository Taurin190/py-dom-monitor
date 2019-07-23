from client.requests_client import RequestClient
from client.selenium_client import SeleniumClient


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
