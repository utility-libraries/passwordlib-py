#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import re
from functools import cached_property


_RE_LOWERCASE = re.compile(r"[a-z]")
_RE_UPPERCASE = re.compile(r"[A-Z]")
_RE_DIGITS = re.compile(r"[0-9]")
_RE_SYMBOLS = re.compile(r"[^a-zA-Z0-9]")


class Analyzer:
    def __init__(self, password: str):
        self._password = password

    @cached_property
    def is_secure(self) -> bool:
        return self.score >= 5

    @cached_property
    def is_highly_secure(self) -> bool:
        return self.score >= 8

    @cached_property
    def score(self) -> int:
        if self.length < 4 or self.is_commonly_used:
            return 0
        score = 0.0
        score += self.contains_lowercase
        score += self.contains_uppercase
        score += self.contains_digits
        score += self.contains_symbols
        score += self.length * 0.33
        score -= (self.max_consecutive_character - 1) * 0.5
        return max(0, round(score))

    @property
    def password(self) -> str:
        return self._password

    @cached_property
    def contains_lowercase(self) -> bool:
        return _RE_LOWERCASE.search(self.password) is not None

    @cached_property
    def contains_uppercase(self) -> bool:
        return _RE_UPPERCASE.search(self.password) is not None

    @cached_property
    def contains_digits(self) -> bool:
        return _RE_DIGITS.search(self.password) is not None

    @cached_property
    def contains_symbols(self) -> bool:
        return _RE_SYMBOLS.search(self.password) is not None

    @cached_property
    def length(self) -> int:
        return len(self.password)

    @cached_property
    def max_consecutive_character(self) -> int:
        from collections import defaultdict
        dictionary = defaultdict(int)
        current_count = 0
        latest_char = ''

        for char in self.password:
            if char == latest_char:
                current_count += 1
            else:
                current_count = 1
                latest_char = char
            if current_count > dictionary[char]:
                dictionary[char] = current_count
        return max(dictionary.values())

    @cached_property
    def is_commonly_used(self) -> bool:
        from ..commonly_used import is_commonly_used
        return is_commonly_used(self.password)
