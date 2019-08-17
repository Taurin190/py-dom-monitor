from domain.dom_diff import DomDiff
from unittest import TestCase


class DomDiffTest(TestCase):
    def setUp(self):
        self.diff_tool = DomDiff({"text_max": 20})

    def test_failure(self):
        self.fail("fail")
