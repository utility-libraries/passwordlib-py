# -*- coding=utf-8 -*-
r"""

"""


__all__ = ['PasswordlibError', 'PWLibSyntaxError', 'PWLibBadPrefixError']


class PasswordlibError(Exception):
    pass


class PWLibSyntaxError(PasswordlibError):
    pass


class PWLibBadPrefixError(PasswordlibError):
    pass
