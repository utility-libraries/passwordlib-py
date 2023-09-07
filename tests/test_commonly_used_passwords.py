#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestImport(unittest.TestCase):
    def test_import(self):
        import passwordlib.commonly_used  # noqa

    def test_common(self):
        from passwordlib.commonly_used import is_commonly_used

        self.assertTrue(is_commonly_used("123456"))
        self.assertTrue(is_commonly_used("password"))
        self.assertTrue(is_commonly_used("matrix"))
        self.assertFalse(is_commonly_used("password-library"))
        self.assertFalse(is_commonly_used("TifnedjothUj"))


if __name__ == '__main__':
    unittest.main()
