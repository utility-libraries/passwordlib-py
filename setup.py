# -*- coding=utf-8 -*-
r"""

"""
import sys; sys.path.append('src')  # noqa
from setuptools import setup
from passwordlib import __version__, __author__, __description__, __license__
import os.path as p

HERE = p.abspath(p.dirname(__file__))

with open(p.join(HERE, 'README.md'), 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='password-library',
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PlayerG9/passwordlib-py/",
    author=__author__,
    license=__license__,
    project_urls={
        "Author Github": "https://github.com/PlayerG9",
        "Homepage": "https://github.com/PlayerG9/passwordlib-py/",
        "Bug Tracker": "https://github.com/PlayerG9/passwordlib-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    test_suite="tests",
)
