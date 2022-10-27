import unittest
from ac_parser.ac_parser import SourceCodeParser

class DocParserTestCase(unittest.TestCase):

    @classmethod
    def __init_subclass__(cls, lang, file, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.lang = lang

    @classmethod
    def setUpClass(cls):
        cls.parser = SourceCodeParser(cls.lang)
