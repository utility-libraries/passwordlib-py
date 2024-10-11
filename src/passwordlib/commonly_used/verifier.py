# -*- coding=utf-8 -*-
r"""

"""
import os.path as p
from importlib import resources


COMMON_PASSWORDS = set()


def init(force: bool = False, packaged: bool = False) -> None:
    r"""
    load the password-list into the memory

    (normally you don't have to call this method yourself)

    :param force: whether to clear the cache and read the passwords again
    :param packaged: whether this application was packaged (e.g. zipapp) and normal reading is not possible
    """
    global COMMON_PASSWORDS
    if not force and len(COMMON_PASSWORDS): return
    'password-list.txt'
    COMMON_PASSWORDS.clear()

    if packaged:
        with resources.open_text('passwordlib.commonly_used', 'password-list.txt', encoding='utf-8') as file:
            for password in file:
                COMMON_PASSWORDS.add(password.rstrip())
    else:
        password_file = p.join(p.dirname(__file__), 'password-list.txt')
        with open(password_file, 'r', encoding='utf-8') as file:
            for password in file:
                COMMON_PASSWORDS.add(password.rstrip())


def is_commonly_used(password: str) -> bool:
    r"""
    checks whether a password is commonly used or not
    """
    init()
    return password in COMMON_PASSWORDS
