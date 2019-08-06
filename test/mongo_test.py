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
            "collection": "monitor"
        }
        self.client = Mongo(config)

    def test_fail(self):
        self.fail("fail")