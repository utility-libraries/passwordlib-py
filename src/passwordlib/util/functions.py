#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import hashlib
import typing as t
from .. import config


__all__ = ['generate_salt', 'get_password_bytes', 'get_algorithm', 'get_iterations', 'get_salt']


def generate_salt(length: int = None):
    r"""
    generate a random salt

    :param length: length of the salt in bytes
    """
    return os.urandom(length or config.DEFAULT_SALT_LENGTH)


def get_password_bytes(password: t.Optional[t.AnyStr]) -> bytes:
    r"""
    ensures the password is bytes
    """
    return password.encode() if isinstance(password, str) else password


def get_algorithm(algorithm: t.Optional[str] = None) -> str:
    r"""
    returns and checks the given algorithm or returns the default

    :param algorithm: name of the algorithm
    """
    algorithm = algorithm or config.DEFAULT_ALGORITHM
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Algorithm {algorithm} is not available")
    return algorithm


def get_iterations(iterations: t.Optional[int] = None) -> int:
    r"""
    return and validate the iterations or returns the default

    :param iterations: number of iterations you want
    """
    iterations = iterations or config.DEFAULT_ITERATIONS
    if iterations <= 0:
        raise ValueError("Bad number of iterations")
    return iterations


def get_salt(salt: t.Optional[bytes] = None, *, salt_length: int = None) -> bytes:
    r"""
    return the salt or returns a generated one

    :param salt: your salt
    :param salt_length: length of the salt if it's generated
    """
    salt = salt or generate_salt(length=salt_length)
    return salt
