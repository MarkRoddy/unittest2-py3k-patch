#! /usr/bin/env python
# setup.py
# Install script for unittest2
# Copyright (C) 2010 Michael Foord
# E-mail: fuzzyman AT voidspace DOT org DOT uk

# This software is licensed under the terms of the BSD license.
# http://www.voidspace.org.uk/python/license.shtml

import os
import sys
from unittest2 import __version__ as VERSION

NAME = 'unittest2py3k'

PACKAGES = ['unittest2', 'unittest2.test']
SCRIPTS = ['unit2.py', 'unit2']

DESCRIPTION = 'A Python 3 compatible version of unittest2'

URL = 'http://pypi.python.org/pypi/unittest2'

readme = os.path.join(os.path.dirname(__file__), 'README.txt')
LONG_DESCRIPTION = open(readme).read()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Testing',
]

AUTHOR = 'Michael Foord'

AUTHOR_EMAIL = 'michael@voidspace.org.uk'

KEYWORDS = "unittest testing tests".split(' ')


params = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=PACKAGES,
    scripts=SCRIPTS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS
)


py_version = sys.version[:3]

SCRIPT1 = 'unit2'
SCRIPT2 = 'unit2-%s' % (py_version,)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
else:
    params['entry_points'] = {
        'console_scripts': [
            '%s = unittest2:main_' % SCRIPT1,
            '%s = unittest2:main_' % SCRIPT2,
        ],
    }
    
    params['test_suite'] = 'unittest2.collector'

setup(**params)
