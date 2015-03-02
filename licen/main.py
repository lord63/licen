#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
licen, generates license for you via command line

Usage:
  licen (-l | --list)
  licen header (-l | --list)
  licen LICENSE_NAME
  licen [-y YEAR] [-f FULLNAME] [-e EMAIL] LICENSE_NAME
  licen header LICENSE_NAME
  licen header [-y YEAR] [-f FULLNAME] [-e EMAIL] LICENSE_NAME
  licen (-h | --help)
  licen (-V | --version)

Options:
  -l --list     List all the support licenses or headers.
  -y YEAR       Specify the year.
  -f FULLNAME   Specify the owner's fullname.
  -e EMAIL      Specify the email.
  -h --help     Show the help message.
  -V --version  Show the version info.

"""

__title__ = "licen"
__version__ = "0.1.0"
__author__ = "lord63"
__license__ = "MIT"
__copyright__ = "Copyright 2015 lord63"


import os
from os import path
from datetime import date
import subprocess

from docopt import docopt
from jinja2 import FileSystemLoader, Environment


ROOT = path.dirname(path.abspath(__file__))
LICENSES_DIR = path.join(ROOT, 'templates/licenses')
HEADERS_DIR = path.join(ROOT, 'templates/headers')
LICENSES = sorted(os.walk(LICENSES_DIR).next()[2])
HEADERS = sorted(os.walk(HEADERS_DIR).next()[2])


def get_default_context():
    year = date.today().year
    fullname = subprocess.check_output(
        'git config --get user.name'.split()).strip()
    email = subprocess.check_output(
        'git config --get user.email'.split()).strip()
    return {'year': year, 'fullname': fullname, 'email': email}


def generate_file(name, user_context, is_license):
    if is_license == 0:
        if name not in HEADERS:
            raise ValueError(
                "Unsuppport license header: {0}".format(name))
        env = Environment(loader=FileSystemLoader(HEADERS_DIR))
    else:
        if name not in LICENSES:
            raise ValueError("Unsuppport license: {0}".format(name))
        env = Environment(loader=FileSystemLoader(LICENSES_DIR))
    template = env.get_template(name)
    context = get_default_context()
    for key, value in user_context.items():
        context[key] = value
    return template.render(**context)


def main():
    arguments = docopt(__doc__, version=__version__)
    raw_context = {'year': arguments['-y'],
                   'fullname': arguments['-f'],
                   'email': arguments['-e']}
    user_context = {key: value for key, value in raw_context.items()
                    if value is not None}
    if arguments['--list'] and arguments['header']:
        print ', '.join(HEADERS)
    elif arguments['--list']:
        print ', '.join(LICENSES)
    elif arguments['header'] and arguments['LICENSE_NAME']:
        license_header = arguments['LICENSE_NAME']+'-header'
        print generate_file(license_header, user_context, 0)
    elif arguments['LICENSE_NAME']:
        print generate_file(arguments['LICENSE_NAME'], user_context, 1)
    else:
        print __doc__


if __name__ == '__main__':
    main()
