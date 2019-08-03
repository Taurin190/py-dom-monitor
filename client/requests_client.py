from client.client import Client
import requests


class RequestClient(Client):
    def get_html(self, url):
        response = requests.get(url)
        return response.text
