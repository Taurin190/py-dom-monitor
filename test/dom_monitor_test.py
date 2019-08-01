from dom_monitor import DomMonitor
from unittest import TestCase


class DomMonitorTest(TestCase):
    def test_get_client(self):
        client = DomMonitor.get_client("test")
        self.assertTrue(callable(client.get_html))

    def test_get_database(self):
        db = DomMonitor.get_database("test", {"hostname": "localhost", "port": "3301", "database": "dom_monitor"})
        self.assertTrue(callable(db.get_exec_count))
        self.assertTrue(callable(db.get_previous_html))
        self.assertTrue(callable(db.update_exec_count))
        self.assertTrue(callable(db.update_previous_html))

    def test_get_notification(self):
        notification = DomMonitor.get_notification("slack", {"url": ""})
        self.assertTrue(callable(notification.send))

