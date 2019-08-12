from dom_monitor import DomMonitor
from unittest import TestCase


class DomMonitorTest(TestCase):
    def test_exec(self):
        dom_monitor = DomMonitor()
        try:
            dom_monitor.exec("test.conf")
        except SystemExit:
            self.fail('SystemExit exception doesn\'t expected')
        except SystemError:
            self.fail('SystemError exception doesn\'t expected')
        else:
            self.assertTrue(True)

    def test_exec_without_args(self):
        dom_monitor = DomMonitor()
        try:
            dom_monitor.exec()
        except SystemExit as e:
            self.assertEqual(1, e.code)
        else:
            self.fail('SystemExit exception expected')

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

    def test_get_domain(self):
        domain = DomMonitor.get_domain("", "", "")
        self.assertTrue(callable(domain.exec))

