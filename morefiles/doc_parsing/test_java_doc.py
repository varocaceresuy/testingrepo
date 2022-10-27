import unittest

from ac_parser.ac_parser import SourceCodeParser


class JavaDocParserTestCase(unittest.TestCase):
    """
    To enhance see:
    https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#examples
    https://developer.wordpress.org/coding-standards/inline-documentation-standards/javascript/
    """

    def setUp(self):
        self.parser = SourceCodeParser(language="java")

    def test_doc_normal(self):
        doc_normal = \
            "docstring example.\n"
        expected_doc = "docstring example."
        expected_tags = []
        doc_data = self.parser.parse_docstring(doc_normal)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_extra_line(self):
        doc_w_extra_line = \
            "docstring example.\n" \
            "extra line\n"
        expected_doc = "docstring example.\n" \
                       "extra line"
        expected_tags = []
        doc_data = self.parser.parse_docstring(doc_w_extra_line)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_param_return(self):
        doc_w_param_return = \
            "docstring example.\n" \
            "\n" \
            "@param param2 text\n" \
            "value from param2 continues\n" \
            "@return value"
        expected_doc = "docstring example."
        expected_tags = [("param", "param2 text\nvalue from param2 continues"),
                         ("return", "value")]
        doc_data = self.parser.parse_docstring(doc_w_param_return)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_html_tags(self):
        doc_w_html_tags = \
            "<p>docstring example.</p>\n"
        expected_doc = "docstring example."
        expected_tags = []
        doc_data = self.parser.parse_docstring(doc_w_html_tags)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_ref(self):
        doc_w_param_return = \
            "docstring {@link String.size} example.\n" \
            "\n" \
            "@param {@link String}\n" \
            "value from param2 continues\n" \
            "@return {@link String} value\n"
        expected_doc = "docstring String.size example."
        expected_tags = [("param", "String\nvalue from param2 continues"),
                         ("return", "String value")]
        doc_data = self.parser.parse_docstring(doc_w_param_return)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_multiple_tags_no_description(self):
        doc_w_multiple_tags_no_description = \
            "@param {@link String}\n" \
            "value from param2 continues\n" \
            "@return {@link String} value\n" \
            "@see"
        expected_doc = ""
        expected_tags = [("param", "String\nvalue from param2 continues"),
                         ("return", "String value"),
                         ("see", "")]
        doc_data = self.parser.parse_docstring(doc_w_multiple_tags_no_description)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_w_emoji(self):
        doc_w_emoji = \
            "docstring example 😂 汉字.\n"
        expected_doc = "docstring example 😂 汉字."
        expected_tags = []
        doc_data = self.parser.parse_docstring(doc_w_emoji)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_empty_tag(self):
        doc_w_emoji = \
            "docstring example\n" \
            "@param"
        expected_doc = "docstring example"
        expected_tags = [("param", "")]
        doc_data = self.parser.parse_docstring(doc_w_emoji)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_only_one_tag(self):
        doc_only_one_tag = \
            "@return int"
        expected_doc = ""
        expected_tags = [("return", "int")]
        doc_data = self.parser.parse_docstring(doc_only_one_tag)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)

    def test_doc_only_one_empty_tag(self):
        doc_only_one_empty_tag = \
            "@return"
        expected_doc = ""
        expected_tags = [("return", "")]
        doc_data = self.parser.parse_docstring(doc_only_one_empty_tag)
        self.assertEqual(expected_doc, doc_data.text)
        self.assertEqual(expected_tags, doc_data.tags)
