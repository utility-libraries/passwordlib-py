#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import unittest


class TestAttribute(unittest.TestCase):
    def test_import(self):
        import passwordlib.attr # noqa

    def test_set(self):
        from passwordlib.util import compare_password
        from passwordlib.attr import PasswordAttribute

        class User:
            name: str
            password = PasswordAttribute()

        user = User()
        self.assertEqual(user.password, None)

        user.password = "secret"
        self.assertNotEqual(user.password, "secret")
        self.assertTrue(compare_password("secret", user.password))

        user.password = None
        self.assertEqual(user.password, None)

        user.password = "secret2"
        self.assertNotEqual(user.password, "secret2")
        self.assertTrue(compare_password("secret2", user.password))

        del user.password
        self.assertEqual (user.password, None)


if __name__ == '__main__':
    unittest.main()
