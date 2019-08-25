from domain.dom_diff import DomDiff
from unittest import TestCase


class TestDomDiff(TestCase):
    def setUp(self):
        self.diff_tool = DomDiff({"text_max": 20})

    def test_compare(self):
        html1 = "<html><body><h1>TEST</h1></body></html>"
        result = self.diff_tool.compare(html1, html1)
        self.assertEquals([], result)

    def test_compare_have_diff(self):
        html1 = "<html><body><h1>TEST1</h1></body></html>"
        html2 = "<html><body><h1>TEST2</h1></body></html>"
        result = self.diff_tool.compare(html1, html2)
        self.assertEquals([
            "html > body > h1"
        ], result)

    def test_compare_have_diff_and_same(self):
        html1 = "<html><body><h1>TEST1</h1><h2>TEST</h2></body></html>"
        html2 = "<html><body><h1>TEST2</h1><h2>TEST</h2></body></html>"
        result = self.diff_tool.compare(html1, html2)
        self.assertEquals([
            "html > body > h1"
        ], result)
