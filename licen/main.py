#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
licen, generates license for you via command line

Usage:
  licen [header] (-l | --list)
  licen [-y YEAR] [-f FULLNAME] [-e EMAIL] LICENSE_NAME
  licen header [-y YEAR] [-f FULLNAME] [-e EMAIL] LICENSE_HEADER
  licen --var NAME
  licen (-h | --help)
  licen (-V | --version)

Options:
  -l --list     List all the support licenses or headers.
  -y YEAR       Specify the year.
  -f FULLNAME   Specify the owner's fullname.
  -e EMAIL      Specify the email.
  --var         List all the variables in the template.
  -h --help     Show the help message.
  -V --version  Show the version info.

"""


import os
from os import path
from datetime import date
import subprocess
import string

from docopt import docopt
from jinja2 import FileSystemLoader, Environment, meta

from licen import __version__


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


def get_vars(name):
    if 'header' in name:
        env = Environment(loader=FileSystemLoader(HEADERS_DIR))
    else:
        env = Environment(loader=FileSystemLoader(LICENSES_DIR))
    template_source = env.loader.get_source(env, name)[0]
    parsed_content = env.parse(template_source)
    variables = list(meta.find_undeclared_variables(parsed_content))
    default_context = get_default_context()
    result = ("The {0} template contains following "
              "defaults:\n").format(string.upper(name))
    for variable in variables:
        result = result + "\t{0}: {1}\n".format(
            variable,default_context[variable])
    result = result + "You can overwrite them at your ease."
    return result


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
    elif arguments['LICENSE_HEADER']:
        print generate_file(arguments['LICENSE_HEADER'], user_context, 0)
    elif arguments['LICENSE_NAME']:
        print generate_file(arguments['LICENSE_NAME'], user_context, 1)
    elif arguments['--var']:
        print get_vars(arguments['NAME'])
    else:
        print __doc__


if __name__ == '__main__':
    main()
