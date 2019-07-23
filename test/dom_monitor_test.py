from dom_monitor import DomMonitor
from unittest import TestCase


class DomMonitorTest(TestCase):
    def test_get_client(self):
        client = DomMonitor.get_client("test")
        self.assertTrue(callable(client.get_html))

