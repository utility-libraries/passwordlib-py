#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import inspect
import typing as t
from abc import abstractmethod
from collections.abc import Iterable
from ..analyzer import Analyzer


AnyRule = t.Union['RuleSet', 'RuleBase']


class RuleSet:
    _rules: t.Set[AnyRule]

    def __init__(self, rules: t.Union[AnyRule, t.Set['RuleBase']]):
        if isinstance(rules, set):
            self._rules = rules
        else:
            self._rules = set(rules._rules if isinstance(rules, RuleSet) else {rules})

    def __iter__(self):
        yield from self._rules

    def __len__(self):
        return len(self._rules)

    def __combine__(self, other) -> 'RuleSet':
        if isinstance(other, RuleSet):
            return RuleSet(self._rules | other._rules)
        elif isinstance(other, RuleBase):
            return RuleSet(self._rules | {other})
        else:
            raise NotImplementedError(f"{type(self).__name__} can't handle {type(other).__name__}")

    def __or__(self, other) -> 'RuleSet':
        return self.__combine__(other)

    def __ror__(self, other) -> 'RuleSet':
        return self.__combine__(other)

    def __ior__(self, other):
        self._rules = self.__combine__(other)._rules


class RuleBase:
    def __or__(self, other):
        return RuleSet(self) | other

    @abstractmethod
    def validate(self, analyzer: Analyzer):
        raise NotImplementedError()


class LengthRule(RuleBase):
    def __init__(self, min: int = 8):
        self._min_length = min

    def validate(self, analyzer: Analyzer):
        return analyzer.length >= self._min_length


class NotCommonlyUsedRule(RuleBase):
    def validate(self, analyzer: Analyzer):
        return not analyzer.is_commonly_used
