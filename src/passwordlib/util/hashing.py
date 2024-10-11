#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import hmac
import hashlib
import typing as t
from . import functions as fn
from .dumping import dumps, loads


__all__ = ['hash_only', 'hash_password', 'compare_hashes', 'compare_password']


def hash_only(password: t.AnyStr, *, algorithm: str = None, iterations: int = None, salt: bytes = None) -> bytes:
    r"""
    hash the password and return the hashed version (no other information like algorithm, iterations or salt)

    :param password: the password to hash
    :param algorithm: the algorithm to use
    :param iterations: the number of iterations
    :param salt: random salt
    :return: the hashed password
    """
    password = fn.get_password_bytes(password)
    algorithm = fn.get_algorithm(algorithm)
    iterations = fn.get_iterations(iterations)
    salt = fn.get_salt(salt)
    if algorithm == "scrypt":
        n = iterations
        from ..config import (
            SCRYPT_BLOCK_SIZE as R,
            SCRYPT_PARALLELIZATION as P,
        )
        return hashlib.scrypt(
            password=password,
            salt=salt,
            n=n, r=R, p=P, maxmem=128 * n * R * P,
            dklen=64,  # 64 bytes => 512 bits
        )
    else:
        return hashlib.pbkdf2_hmac(
            hash_name=algorithm,
            password=password,
            salt=salt,
            iterations=iterations,
        )


def hash_password(
        password: t.AnyStr,
        *, algorithm: str = None, iterations: int = None, salt: bytes = None, salt_length: int = None,
) -> bytes:
    r"""
    hash the password and return the dumped version of the algorithm, the iterations, the salt and the password-hash

    :param password: the password to hash
    :param algorithm: the algorithm to use
    :param iterations: the number of iterations
    :param salt: random salt
    :param salt_length: length of the salt if it's generated
    :return: the dumped version of the algorithm, the iterations, the salt and the password-hash
    """
    password = fn.get_password_bytes(password)
    algorithm = fn.get_algorithm(algorithm)
    iterations = fn.get_iterations(iterations)
    salt = fn.get_salt(salt, salt_length=salt_length)
    hashed = hash_only(
        password=password,
        algorithm=algorithm,
        salt=salt,
        iterations=iterations
    )
    return dumps(algorithm=algorithm, iterations=iterations, salt=salt, hashed=hashed)


def compare_hashes(a: t.AnyStr, b: t.AnyStr) -> bool:
    r"""
    securely compare two hashed passwords
    (basically a == b but in a way to prevent timing attacks)

    :param a: password-1 hash
    :param b: password-2 hash
    :return: True if it's the same, False otherwise
    """
    return hmac.compare_digest(a, b)


def compare_password(password: t.AnyStr, to: bytes) -> bool:
    r"""
    compare a password to the dumped version of another one

    :param password: the password
    :param to: to dumped password to compare to
    :return: True if it's the same, False otherwise
    """
    parts = loads(to, verify=True)
    return compare_hashes(
        hash_only(password=password, algorithm=parts.algorithm, iterations=parts.iterations, salt=parts.salt),
        parts.hashed,
    )
