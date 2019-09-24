from client.client import Client
import requests


class RequestClient(Client):
    def get_html(self, url):
        response = requests.get(url)
        if response.status_code != 200 and response.status_code != 302:
            raise Exception("Status Code" + str(response.status_code))
        return response.text
