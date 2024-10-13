# -*- coding=utf-8 -*-
r"""

"""
from ..core import LoadedTuple
from ..exceptions import *


__all__ = ['load_bcrypt', 'load_sha1']


def load_bcrypt(dump: str) -> LoadedTuple:
    if dump[0] != "$": raise PWLibSyntaxError()
    prefix, sep, rest = dump[1:].partition("$")
    if sep is None: raise PWLibSyntaxError()
    if prefix not in {"2", "2a", "2b", "2x", "2y"}: raise PWLibBadPrefixError("unknown prefix")
    rounds, sep, rest = rest.partition("$")
    if sep is None: raise PWLibSyntaxError()
    iterations = int(rounds)
    salt = rest[:22].encode()  # note: salt is in a base-64 encoded format
    hashed = rest[22:].encode()
    return LoadedTuple(algorithm="bcrypt", iterations=iterations, salt=salt, hashed=hashed)


def load_sha1(dump: str) -> LoadedTuple:
    from base64 import b64decode
    if not dump.startswith("{SHA}"): raise PWLibBadPrefixError("Invalid dump format")
    b64encoded = dump[6:]
    hashed = b64decode(b64encoded)
    return LoadedTuple(algorithm="sha1", iterations=-1, salt=b'', hashed=hashed)
