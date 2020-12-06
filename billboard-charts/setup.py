#!/usr/bin/env python

from setuptools import setup

setup(
    name="billboard.py",
    version="6.2.1",  # Don't forget to update CHANGELOG.md!
    description="Python API for downloading Billboard charts",
    author="Allen Guo",
    author_email="guoguo12@gmail.com",
    url="https://github.com/guoguo12/billboard-charts",
    py_modules=["billboard"],
    license="MIT License",
    install_requires=["beautifulsoup4 >= 4.4.1", "requests >= 2.2.1"],
)
