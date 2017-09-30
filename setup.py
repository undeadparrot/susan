#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

CLASSIFIERS = [
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
]
REQUIRES = [
    'click',
    'sqlalchemy',
]
setup(
    # project bio things
    name='susan',
    version='0.0.2',
    author='Shane Matuszek',
    author_email='smatuszeksa@gmail.com',
    keywords='note wiki todo cli',
    license='MIT',
    url='https://github.com/undeadparrot/susan',
    description="Simple CLI note taker and free-wheeling wiki",

    #things for pypi
    classifiers=CLASSIFIERS,

    # things import for setup
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=REQUIRES,
    entry_points={'console_scripts': ['susan=susan.cli:cli']})
