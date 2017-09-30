#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    # project bio things
    name='susan',
    version='0.0.1',
    author='Shane Matuszek',
    author_email='smatuszeksa@gmail.com',
    keywords='note wiki todo cli',
    license='MIT',

    url='https://github.com/undeadparrot/susan',
    description="Simple CLI note taker and free-wheeling wiki",

    #things for pypi
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Topic :: Database',
        'Topic :: Education',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Office/Business :: News/Diary',
    ],

    # things import for setup
    packages=find_packages(),
    install_requires=[
        'click',
        'sqlalchemy',
    ],
    entry_points={'console_scripts': ['susan=susan.cli:cli']})
