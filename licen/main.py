#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
licen, generates license for you via command line

Usage:
  licen (ls | list)
  licen NAME
  licen (-h | --help)
  licen (-V | --version)

Options:
  -h --help     Show the helo message.
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


def get_context():
    year = date.today().year
    fullname = subprocess.check_output(
        'git config --get user.name'.split()).strip()
    return {'year': year, 'fullname': fullname}


def handle_licenses(name):
    if name not in LICENSES:
        raise ValueError("Unsuppport license: {0}".format(name))
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(name)
    context = get_context()
    return template.render(**context)


def main():
    arguments = docopt(__doc__, version=__version__)
    if arguments['ls'] or arguments['list']:
        print ', '.join(LICENSES)
    elif arguments['NAME']:
        print handle_licenses(arguments['NAME'])
    else:
        print __doc__


if __name__ == '__main__':
    main()
