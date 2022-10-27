import unittest

from ac_parser.ac_parser import SourceCodeParser


class PythonDocParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = SourceCodeParser(language="python")

    def test_doc_normal(self):
        doc_normal = \
            "Docstring example"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_normal)
        self.assertEqual(expected_res, doc_data.text)

    def test_w_non_ascii(self):
        doc_w_non_ascii = \
            "Docstring example 😂 汉字"
        expected_res = "Docstring example 😂 汉字"
        doc_data = self.parser.parse_docstring(doc_w_non_ascii)
        self.assertEqual(expected_res, doc_data.text)

    def test_reStructuredText_format(self):
        doc_reStructuredText_format = \
            "Docstring example\n" \
            ":param example_param: Param description\n" \
            ":type example_param: str\n" \
            ":return: return description\n" \
            ":rtype: list"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_reStructuredText_format)
        self.assertEqual(expected_res, doc_data.text)

    def test_reStructuredText_multiline(self):
        doc_reStructuredText_format = \
            "Docstring example\n" \
            ":param example_param: Param description\n" \
            "                      Extra description\n" \
            ":type example_param: str\n" \
            ":return: return description\n" \
            ":rtype: list"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_reStructuredText_format)
        self.assertEqual(expected_res, doc_data.text)

    def test_google_format(self):
        doc_google_format = \
            "Docstring example\n" \
            "\n" \
            "Args:\n" \
            "   example_param (str): Param description\n" \
            "       (default is 'default')\n" \
            "Returns:\n" \
            "   list: return description\n"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_google_format)
        self.assertEqual(expected_res, doc_data.text)

    def test_numpy_format(self):
        doc_numpy_format = \
            "Docstring example\n" \
            "\n" \
            "Parameters\n" \
            "----------\n" \
            "example_param : str\n" \
            "    Param description\n" \
            "\n" \
            "Returns\n" \
            "-------\n" \
            "list" \
            "   return description\n"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_numpy_format)
        self.assertEqual(expected_res, doc_data.text)

    def test_epytext_format(self):
        doc_epytext_format = \
            "Docstring example\n" \
            "@type example_param: str\n" \
            "@param example_param: Param description\n" \
            "@rtype: list" \
            "@return: return description\n"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_epytext_format)
        self.assertEqual(expected_res, doc_data.text)
