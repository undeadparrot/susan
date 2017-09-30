#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='susan',
    version='0.0.1',
    author='Shane Matuszek',
    packages=find_packages(),
    install_requires=[
        'click',
        'sqlalchemy',
    ],
    entry_points={'console_scripts': ['susan=susan.cli:cli']})
