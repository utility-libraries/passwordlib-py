# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t


__all__ = ['gen_salt_str']


def gen_salt_str(length: int, *, characters: t.Sequence[str]) -> str:
    r"""
    :param length: length of the resulting salt
    :param characters: characters to use in the salt
    :return: generated salt
    """
    return ''.join(characters[int(r / 256 * len(characters))] for r in os.urandom(length))
