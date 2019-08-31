from model.file import File
from unittest import TestCase


class TestFile(TestCase):
    def setUp(self):
        config = ""
        self.client = File(config)
        self.client.insert_previous_html("<html><body><h1>TEST</h1></body></html>")

    def test_get_exec_count(self):
        actual = self.client.get_exec_count()
        self.assertEqual(1, actual)

    def test_get_previous_html(self):
        actual = self.client.get_previous_html()
        self.assertEqual("<html><body><h1>TEST</h1></body></html>", actual["html"])

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
        self.assertEqual(1, actual["id"])
        self.assertEqual("html > body > h1", actual["diff"])
        self.assertEqual(1, actual["count"])

    def test_find_diff_from_previous_empty(self):
        actual = self.client.find_diff_from_previous("invalid key")
        self.assertIsNone(actual)

    def test_insert_previous_diff(self):
        previous = self.client.find_diff_from_previous("key1")
        self.assertIsNone(previous)
        self.client.insert_previous_diff("key1")
        actual = self.client.find_diff_from_previous("key1")
        self.assertIsNotNone(actual)

    def test_update_previous_diff(self):
        previous = self.client.find_diff_from_previous("html > body > h1")
        self.assertEqual(1, previous["count"])
        self.client.update_previous_diff("html > body > h1")

        actual = self.client.find_diff_from_previous("html > body > h1")
        self.assertEqual(2, actual["count"])

    def test_insert_or_update_diff_with_new_diff(self):
        actual = self.client.insert_or_update_diff("key1")
        self.assertEqual("key1", actual["diff"])
        self.assertEqual(1, actual["count"])

    def test_insert_or_update_diff_with_exist_diff(self):
        actual = self.client.insert_or_update_diff("html > body > h1")
        self.assertEqual("html > body > h1", actual["diff"])
        self.assertEqual(2, actual["count"])

    def tearDown(self):
        self.client.drop()