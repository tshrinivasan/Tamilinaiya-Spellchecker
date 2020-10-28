# -*- coding: utf-8 -*-

import unittest
from tamilinayavaani.parse_words import check_first_letter, check_last_letter

class TestParseWords(unittest.TestCase):
    def test_check_first_letter(self):
        self.assertTrue(check_first_letter("நன்றி"))
        self.assertTrue(check_last_letter("நன்றி"))

if __name__ == u'__main__':
    unittest.main()
