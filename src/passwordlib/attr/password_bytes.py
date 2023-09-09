#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from ..util import compare_password, extract_algorythm, extract_iterations, extract_salt, extract_hashed


__all__ = ['PasswordBytes']


class PasswordBytes(bytes):
    def __eq__(self, other):
        if isinstance(other, str):
            return compare_password(password=other, to=self)
        return super().__eq__(other)

    def compare(self, password: str) -> bool:
        return compare_password(password=password, to=self)

    @property
    def algorithm(self) -> str:
        return extract_algorythm(self)

    @property
    def iterations(self) -> int:
        return extract_iterations(self)

    @property
    def salt(self) -> bytes:
        return extract_salt(self)

    @property
    def hashed(self) -> bytes:
        return extract_hashed(self)
