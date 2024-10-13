# -*- coding=utf-8 -*-
r"""

"""
from ..core import LoadedTuple
from ..exceptions import *


__all__ = ['load_bcrypt', 'load_sha1']


def load_bcrypt(dump: str) -> LoadedTuple:
    parts = dump.split("$")
    if len(parts) != 4: raise PWLibSyntaxError("bad format")

    void, prefix, rounds, salt_and_hash = parts
    if void: raise PWLibSyntaxError("dump does not start with '$'")
    if prefix not in {"2", "2a", "2b", "2x", "2y"}: raise PWLibBadPrefixError("unknown prefix")
    if not rounds.isdigit(): raise PWLibSyntaxError("rounds are not an integer")

    iterations = int(rounds)
    salt = salt_and_hash[:22].encode()  # note: salt is in a base-64 encoded format
    hashed = salt_and_hash[22:].encode()
    return LoadedTuple(algorithm="bcrypt", iterations=iterations, salt=salt, hashed=hashed)


def load_sha256(dump: str) -> LoadedTuple:
    parts = dump.split("$")
    n_parts = len(parts)
    if n_parts != 4 and n_parts != 5: raise PWLibSyntaxError("bad format")

    if n_parts == 4:
        void, prefix, salt, checksum = parts
        rounds = "rounds=5000"
    else:
        void, prefix, rounds, salt, checksum = parts
    if void: raise PWLibSyntaxError("dump does not start with '$'")
    if prefix != "5": raise PWLibSyntaxError("unknown prefix")
    if not rounds.startswith("rounds=") or not rounds[7:].isdigit(): raise PWLibSyntaxError("bad rounds")

    iterations = int(rounds[7:])
    salt = salt.encode()
    hashed = checksum.encode()

    return LoadedTuple(algorithm="sha256", iterations=iterations, salt=salt, hashed=hashed)


def load_sha1(dump: str) -> LoadedTuple:
    from base64 import b64decode
    if not dump.startswith("{SHA}"): raise PWLibBadPrefixError("Invalid dump format")
    b64encoded = dump[6:]
    hashed = b64decode(b64encoded)
    return LoadedTuple(algorithm="sha1", iterations=-1, salt=b'', hashed=hashed)
