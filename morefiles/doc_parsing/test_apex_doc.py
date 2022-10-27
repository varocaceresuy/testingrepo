import unittest

from ac_parser.ac_parser import SourceCodeParser


class ApexDocParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = SourceCodeParser(language="apex")

    def test_doc_w_normal_and_tag_description(self):
        doc_w_param_return = \
            "some initial description\n" \
            "\n" \
            "@description some description\n" \
            "value from description continues\n" \
            "@return value"
        expected_doc = "some initial description\nsome description\nvalue from description continues"
        expected_tags = [("description", "some description\nvalue from description continues"),
                         ("return", "value")]
        doc_data = self.parser.parse_docstring(doc_w_param_return)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_only_tag_description(self):
        doc_w_param_return = \
            "@description some description\n" \
            "value from description continues\n" \
            "@return value"
        expected_doc = "some description\nvalue from description continues"
        expected_tags = [("description", "some description\nvalue from description continues"),
                         ("return", "value")]
        doc_data = self.parser.parse_docstring(doc_w_param_return)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)