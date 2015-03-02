#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
licen, generates license for you via command line

Usage:
  licen (-l | --list)
  licen LICENSE_NAME
  licen [-y YEAR] [-f FULLNAME] [-e EMAIL] LICENSE_NAME
  licen (-h | --help)
  licen (-V | --version)

Options:
  -l --list     List all the support licenses.
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
TEMPLATE_DIR = path.join(ROOT, 'templates')
LICENSES = sorted(os.walk(TEMPLATE_DIR).next()[2])


def get_default_context():
    year = date.today().year
    fullname = subprocess.check_output(
        'git config --get user.name'.split()).strip()
    email = subprocess.check_output(
        'git config --get user.email'.split()).strip()
    return {'year': year, 'fullname': fullname, 'email': email}


def handle_licenses(name, user_context):
    if name not in LICENSES:
        raise ValueError("Unsuppport license: {0}".format(name))
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(name)
    context = get_default_context()
    for key, value in user_context.items():
        context[key] = value
    return template.render(**context)


def main():
    arguments = docopt(__doc__, version=__version__)
    if arguments['--list']:
        print ', '.join(LICENSES)
    elif arguments['LICENSE_NAME']:
        raw_context = {'year': arguments['-y'],
                       'fullname': arguments['-f'],
                       'email': arguments['-e']}
        user_context = {key: value for key, value in raw_context.items()
                        if value is not None}
        print handle_licenses(arguments['LICENSE_NAME'], user_context)
    else:
        print __doc__


if __name__ == '__main__':
    main()
