import unittest

from ac_parser.ac_parser import SourceCodeParser
from tests.helpers import ParserTestCase


class CSharpDocParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = SourceCodeParser(language="c_sharp")

    def test_doc_normal(self):
        doc_normal = \
            "<summary>\n" \
            "Docstring example\n" \
            "</summary>"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_normal)
        self.assertEqual(expected_res, doc_data.text)

    def test_doc_multiline(self):
        doc_multiline = \
            "<summary>\n" \
            "Docstring example\n" \
            "Docstring extra line example\n" \
            "</summary>"
        expected_res = "Docstring example\nDocstring extra line example"
        doc_data = self.parser.parse_docstring(doc_multiline)
        self.assertEqual(expected_res, doc_data.text)

    def test_doc_w_params_return(self):
        doc_w_params_return = \
            "<summary>\n" \
            "Docstring example\n" \
            "</summary>\n" \
            "<param name=\"example param\">Param description</param>\n" \
            "<param name=\"example param2\">Param description2</param>\n" \
            "<returns>\n" \
            "return description\n" \
            "</returns>\n"
        expected_res = "Docstring example"
        doc_data = self.parser.parse_docstring(doc_w_params_return)
        self.assertEqual(expected_res, doc_data.text)
