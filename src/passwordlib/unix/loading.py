# -*- coding=utf-8 -*-
r"""

"""
from ..core import LoadedTuple


__all__ = ['load_sha1']


def load_sha1(dump: str) -> LoadedTuple:
    from base64 import b64decode
    if not dump.startswith("{SHA}"):
        raise ValueError("Invalid dump format")
    b64encoded = dump[6:]
    hashed = b64decode(b64encoded)
    return LoadedTuple(algorithm="sha1", iterations=-1, salt=b'', hashed=hashed)
