#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestAttribute(unittest.TestCase):
    def test_import(self):
        from passwordlib import attr # noqa

    def test_set(self):
        from passwordlib.attr import PasswordAttribute

        class User:
            name: str
            password = PasswordAttribute()

        user = User()
        self.assertEquals(user.password, None)

        user.password = "secret"
        self.assertNotEquals(user.password, "secret")

        user.password = None
        self.assertEquals(user.password, None)

        user.password = "secret2"
        self.assertNotEquals(user.password, "secret2")

        del user.password
        self.assertEquals(user.password, None)


if __name__ == '__main__':
    unittest.main()
