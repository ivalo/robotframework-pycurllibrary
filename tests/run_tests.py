#! /usr/bin/env python

"""Runner Script for Robot Framework PycURLLibrary tests

Tests are run by giving a path to the tests to be executed as an argument to
this script. Possible Robot Framework options are given before the path.

Examples:
  run_tests.py acceptance                        # Run all tests in a directory
  run_tests.py acceptance/valid_login.text       # Run tests in a specific file


Running the tests requires that Robot Framework, pycurl, Python to be installed.
"""
import testenv
import os
import sys
from os.path import join
from subprocess import call

try:
    import pycurl
except ImportError, e:
    print 'Importing pycurl module failed (%s).' % e
    print 'Please make sure you have pycurl properly installed.'
    print 'See INSTALL.rst for troubleshooting information.'
    sys.exit(1)

ROBOT_ARGS = [
    '--doc', 'PycURLLibrary_Acceptance_Tests',
    '--outputdir', testenv.RESULTS_DIR,
    '--report', 'none',
    '--log', 'none',
    '--pythonpath', testenv.SRC_DIR,
    '--debugfile', join(testenv.RESULTS_DIR, 'syslog.txt')
]
ROOT = os.path.dirname(os.path.abspath(__file__))


def run_tests(args):
    call(['pybot'] + ROBOT_ARGS + args, shell=(os.sep == '\\'))

def print_help():
    print __doc__

def print_usage():
    print 'Usage: run_tests.py help'


if __name__ == '__main__':
    action = {'help': print_help,
              '': print_usage}.get('-'.join(sys.argv[1:]))
    if action:
        action()
    else:
        run_tests(sys.argv[1:])

sys.exit(0)

