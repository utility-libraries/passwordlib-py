#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestValidator(unittest.TestCase):
    def test_import(self):
        import passwordlib.analyzer  # noqa

    def test_lowercase(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("password")
        self.assertTrue(result.contains_lowercase)

        result = Analyzer("PASSWORD")
        self.assertFalse(result.contains_lowercase)

    def test_uppercase(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("PASSWORD")
        self.assertTrue(result.contains_uppercase)

        result = Analyzer("password")
        self.assertFalse(result.contains_uppercase)

    def test_digits(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("passw0rd")
        self.assertTrue(result.contains_digits)

        result = Analyzer("password")
        self.assertFalse(result.contains_digits)

    def test_symbols(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("password!")
        self.assertTrue(result.contains_symbols)

        result = Analyzer("password")
        self.assertFalse(result.contains_symbols)

    def test_longest_consecutive_character(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("passswoords")
        self.assertEquals(result.max_consecutive_character, 3)

    def test_commonly_used(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("password")
        self.assertTrue(result.is_commonly_used)

    def test_score(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("password")
        self.assertEquals(result.score, 0)

    def test_secure_common(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("password")
        self.assertFalse(result.is_secure)
        self.assertFalse(result.is_highly_secure)

    def test_secure_random(self):
        from passwordlib.analyzer import Analyzer

        result = Analyzer("Pegbope1!")
        self.assertTrue(result.is_secure)
        self.assertFalse(result.is_highly_secure)


if __name__ == '__main__':
    unittest.main()
