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
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    install_requires=[],
    test_suite="tests",
)
