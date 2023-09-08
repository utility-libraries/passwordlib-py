#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import re
import math
import typing as t
from functools import cached_property


_RE_LOWERCASE = re.compile(r"[a-z]")
_RE_UPPERCASE = re.compile(r"[A-Z]")
_RE_DIGITS = re.compile(r"[0-9]")
_RE_SYMBOLS = re.compile(r"[^a-zA-Z0-9]")


class Analyzer:
    r"""
    analyze the given password for different criteria
    """

    def __init__(self, password: str):
        self._password = password

    @cached_property
    def is_secure(self) -> bool:
        r"""
        means not easily guessable (but still possible)
        """
        return self.score >= 5

    @cached_property
    def is_highly_secure(self) -> bool:
        r"""
        means it should be guessed in a reasonable time
        """
        return self.score >= 8

    @cached_property
    def hardcoded_secure(self) -> bool:
        r"""
        hardcoded way to ensure a password is safe by checking the following criteria
        - not commonly used
        - at least 8 characters
        - more than 5 different characters
        - at least 3 of lowercase, uppercase, digits or symbols
        - max consecutive number of a character is 2
        """
        if self.is_commonly_used:
            return False
        if self.length < 8 or self.charset_length <= 4:
            return False
        if (self.contains_lowercase + self.contains_uppercase + self.contains_digits + self.contains_symbols) < 3:
            return False
        if self.max_consecutive_character > 3:
            return False
        return True

    @cached_property
    def score(self) -> int:
        r"""
        calculate a score for the password in consideration of
        - type of characters (lowercase, uppercase, digits and symbols)
        - the length of the password
        - the variety of characters
        - the max number of consecutive characters
        """
        if self.length < 4 or self.is_commonly_used:
            return 0
        score = 0.0
        score += self.contains_lowercase
        score += self.contains_uppercase
        score += self.contains_digits
        score += self.contains_symbols
        score += self.length * 0.25
        score += (self.charset_length - 4) * 0.2
        score -= (self.max_consecutive_character - 2) * 0.5
        return max(0, math.floor(score))

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
    def charset(self) -> t.Set[str]:
        return set(self.password)

    @cached_property
    def charset_length(self) -> int:
        return len(self.charset)

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
