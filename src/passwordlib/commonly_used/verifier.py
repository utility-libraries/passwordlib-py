#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path as p


COMMON_PASSWORDS = set()


def init():
    r"""
    load the password-list into the memory

    (normally you don't have to call this method yourself)
    """
    global COMMON_PASSWORDS
    if len(COMMON_PASSWORDS):
        return
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
