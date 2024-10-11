# -*- coding=utf-8 -*-
r"""

"""


__all__ = ['encrypt_sha1']


def encrypt_sha1(password: str):
    from hashlib import sha1
    from base64 import b64encode
    hashed = sha1(password.encode()).digest()
    return "{SHA1}" + b64encode(hashed).decode()
