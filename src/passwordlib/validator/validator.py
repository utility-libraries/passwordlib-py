#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import inspect
import typing as t
from types import UnionType
from .rules import RuleSet, RuleBase
from ..analyzer import Analyzer


class Validator:
    def __init__(self, rules: t.Union[UnionType, RuleSet, RuleBase, t.Type[RuleBase]] = None):
        self._rules = rules

    @property
    def rules(self) -> t.Set[RuleBase]:
        if self._rules is None:
            return set()
        elif inspect.isclass(self._rules) and issubclass(self._rules, RuleBase):
            return {self._rules()}
        elif isinstance(self._rules, RuleBase):
            return {self._rules}
        else:
            rules = set()
            for rule in self._rules:
                if inspect.isclass(rule) and issubclass(rule, RuleBase):
                    rule = rule()  # instantiate
                rules.add(rule)
            return rules

    def verify(self, password: str) -> bool:
        analyzer = Analyzer(password)
        for rule in self.rules:
            if not rule.validate(analyzer):
                return False
        return True
