#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import hashlib
import typing as t
from .. import config


__all__ = ['generate_salt', 'get_password_bytes', 'get_algorithm', 'get_iterations', 'get_salt']


def generate_salt(*, length: int = None):
    return os.urandom(length or config.DEFAULT_SALT_LENGTH)


def get_password_bytes(password: t.Optional[t.AnyStr]) -> bytes:
    return password.encode() if isinstance(password, str) else password


def get_algorithm(algorithm: t.Optional[str] = None) -> str:
    algorithm = algorithm or config.DEFAULT_ALGORITHM
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Algorithm {algorithm} is not available")
    return algorithm


def get_iterations(iterations: t.Optional[int] = None) -> int:
    iterations = iterations or config.DEFAULT_ITERATIONS
    if iterations <= 0:
        raise ValueError("Bad number of iterations")
    return iterations


def get_salt(salt: t.Optional[bytes] = None) -> bytes:
    salt = salt or generate_salt()
    return salt
