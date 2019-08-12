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
            {"count": 1, "id": 1},
            {"html": "<html><body><h1>TEST</h1></body></html>", "id": 1},
            {"id": 1, "diff": "html > body > h1", "count": 1}
        )

    def test_get_exec_count(self):
        actual = self.client.get_exec_count()
        self.assertEqual(1, actual)

    def test_get_previous_html(self):
        actual = self.client.get_previous_html()
        self.assertEqual("<html><body><h1>TEST</h1></body></html>", actual)

    def test_update_exec_count(self):
        self.client.update_exec_count()
        actual = self.client.get_exec_count()
        self.assertEqual(2, actual)

    def test_update_previous_html(self):
        self.client.update_previous_html("<html><body><h1>TEST</h1><h2>TEST2</2></body></html>")
        actual = self.client.get_previous_html()
        self.assertEqual("<html><body><h1>TEST</h1><h2>TEST2</2></body></html>", actual)

    def test_find_diff_from_previous(self):
        actual = self.client.find_diff_from_previous("html > body > h1")
        self.assertEqual(1, actual[0]["id"])
        self.assertEqual("html > body > h1", actual[0]["diff"])
        self.assertEqual(1, actual[0]["count"])

    def test_find_diff_from_previous_empty(self):
        actual = self.client.find_diff_from_previous("invalid key")
        self.assertEqual(0, len(actual))

    def tearDown(self):
        self.client.drop()
