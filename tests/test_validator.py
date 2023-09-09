#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestValidator(unittest.TestCase):
    def test_import(self):
        import passwordlib.validator  # noqa

    def test_no_rules(self):
        from passwordlib.validator import Validator

        validator = Validator()

        self.assertTrue(validator.verify("any"))


if __name__ == '__main__':
    unittest.main()
