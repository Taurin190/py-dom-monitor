from unittest import TestCase


class DomMonitorTest(TestCase):
    def test_failure(self):
        self.fail("失敗")