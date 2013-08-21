#!/usr/bin/env python

import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'src'))
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

execfile(join(dirname(__file__), 'src', 'PycURLLibrary', 'version.py'))

DESCRIPTION = """
PycURLLibrary is a HTTP web service testing library for Robot Framework
that leverages PycURL to test HTTP and SOAP-based services.
"""[1:-1]

setup(
    name             = 'robotframework-pycurllibrary',
    version          = VERSION,
    description      = 'PyCurl testing library for Robot Framework',
    long_description = DESCRIPTION,
    author           = 'Markku Saarela',
    author_email     = 'ivalo@iki.fi',
    url              = 'https://github.com/jivalo/robotframework-pycurllibrary',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation pycurl curl',
    platforms        = 'any',
    classifiers      = [
                          "Development Status :: 3 - Alpha",
                          "License :: OSI Approved :: Apache License 2.0",
                          "Operating System :: OS Independent",
                          "Programming Language :: Python",
                          "Topic :: Software Development :: Testing"
                       ],
    py_modules       = ['ez_setup'],
    package_dir      = {'': 'src'},
    install_requires = [
                        'robotframework >= 2.7.5', 
                        'pycurl>=7.19'
                       ],
    packages=['PycURLLibrary']
)
