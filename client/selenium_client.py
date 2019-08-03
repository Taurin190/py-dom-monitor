from client.client import Client
from selenium import webdriver


class SeleniumClient(Client):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()

    def get_html(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def __del__(self):
        self.driver.close()

