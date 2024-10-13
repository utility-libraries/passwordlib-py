# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..core import functions as fn


__all__ = ['encrypt_bcrypt', 'encrypt_sha1']


BCRYPT_PREFIX: t.TypeAlias = t.Union[t.Literal[b"2a"], t.Literal[b"2b"]]


def encrypt_bcrypt(password: t.AnyStr, salt: str = None, rounds: int = 12, prefix: BCRYPT_PREFIX = "2b") -> str:
    import bcrypt
    password = fn.get_password_bytes(password)
    salt = salt or bcrypt.gensalt(rounds=rounds, prefix=prefix)
    return bcrypt.hashpw(password, salt=salt).decode()


def encrypt_sha1(password: t.AnyStr) -> str:
    from hashlib import sha1
    from base64 import b64encode
    password = fn.get_password_bytes(password)
    hashed = sha1(password).digest()
    return "{SHA1}" + b64encode(hashed).decode()
