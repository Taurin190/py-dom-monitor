from model.mongo import Mongo
from unittest import TestCase


class MongoTest(TestCase):
    def setUp(self):
        config = {
            "hostname": "localhost",
            "port": 27017,
            "username": "python",
            "password": "python",
            "database": "monitor",
        }
        self.client = Mongo(config)
        self.client.insert(
            {"count": 1},
            {"html": "<html><body><h1>TEST</h1></body></html>"}
        )

    def test_fail(self):
        self.fail("fail")

    def tearDown(self):
        self.client.drop()