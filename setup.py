#!/usr/bin/env python
'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''

import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'src'))
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

execfile(join(dirname(__file__), 'src', 'PycURLLibrary', 'version.py'))

DESCRIPTION = """
PycURLLibrary is client-side URL transfer test library for Robot Framework
based on PycURL
"""[1:-1]

setup(
    name             = 'robotframework-pycurllibrary',
    version          = VERSION,
    description      = 'Robot Framework test library for client-side URL transfer',
    long_description = DESCRIPTION,
    author           = 'Markku Saarela',
    author_email     = 'ivalo@iki.fi',
    url              = 'https://github.com/jivalo/robotframework-pycurllibrary',
    license          = 'Apache License 2.0',
    keywords         = 'robotframework testing testautomation pycurl curl',
    platforms        = 'any',
    classifiers      = [
                          "Development Status :: 4 - Beta",
                          "License :: OSI Approved :: Apache Software License",
                          "Operating System :: OS Independent",
                          "Programming Language :: Python",
                          "Topic :: Software Development :: Testing"
                       ],
    py_modules       = ['ez_setup'],
    package_dir      = {'': 'src'},
    packages         = ['PycURLLibrary'],
    install_requires = [
                        'robotframework >= 2.7.5' 
                       ]
)
