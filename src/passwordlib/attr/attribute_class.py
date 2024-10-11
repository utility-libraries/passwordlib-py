# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from .. import util


class PasswordAttribute:
    r"""
    automatically hash the password attribute on your class instances

        class User:
            name: str
            password = PasswordAttribute()

        user = User()
        print(user.password)  # None
        user.password = "secret"
        print(user.password)  # b'...'

    """

    _owner: str = None
    _name: str = None

    def __init__(
            self, *,
            allow_reset: bool = True,
            algorithm: t.Optional[str] = None,
            iterations: t.Optional[str] = None,
            salt: t.Optional[str] = None,
    ):
        r"""
        :param allow_reset: allow to reset the attribute to None (by passing None)
        :param algorithm: the algorithm to use
        :param iterations: the number of iterations to use
        :param salt: the salt to use (recommended to leave unset)
        """
        self._allow_reset = allow_reset
        self._algorithm = algorithm
        self._iterations = iterations
        self._salt = salt

    def __set_name__(self, owner, name):
        self._owner = owner
        self._name = name

    @property
    def _instance_attribute_name(self) -> str:
        return f"_{type(self._owner).__name__}_{self._name}"

    def __set__(self, instance, value):
        if self._allow_reset and value is None:
            self.__delete__(instance=instance)
        elif isinstance(value, (str, bytes)):
            dumped = util.hash_password(password=value, algorithm=self._algorithm,
                                        iterations=self._iterations, salt=self._salt)
            setattr(instance, self._instance_attribute_name, dumped)
        else:
            raise TypeError(f"Value of type {type(value)} is not password-hashable")

    def __get__(self, instance, owner) -> t.Optional[bytes]:
        attr = self._instance_attribute_name
        if not hasattr(instance, attr):
            return None
        return getattr(instance, attr)

    def __delete__(self, instance):
        delattr(instance, self._instance_attribute_name)
