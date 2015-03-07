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
import getpass

from docopt import docopt
from jinja2 import FileSystemLoader, Environment, meta

from licen import __version__


ROOT = path.dirname(path.abspath(__file__))
LICENSES_DIR = path.join(ROOT, 'templates/licenses')
HEADERS_DIR = path.join(ROOT, 'templates/headers')
LICENSES = sorted(os.listdir(LICENSES_DIR))
HEADERS = sorted(os.listdir(HEADERS_DIR))


def get_default_context():
    year = date.today().year
    try:
        fullname = subprocess.check_output(
            'git config --get user.name'.split()
        ).strip().decode('utf-8')
    except:
        print("WARNING: Please configure your git.\n")
        fullname = getpass.getuser()
    try:
        email = subprocess.check_output(
            'git config --get user.email'.split()
        ).strip().decode('utf-8')
    except:
        print("WARNING: Please configure your git.\n")
        email = "undefined"
    return {'year': year, 'fullname': fullname, 'email': email}


def generate_file(name, context, is_license):
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
    return template.render(**context)


def get_vars(name):
    if 'header' in name:
        env = Environment(loader=FileSystemLoader(HEADERS_DIR))
    else:
        env = Environment(loader=FileSystemLoader(LICENSES_DIR))
    template_source = env.loader.get_source(env, name)[0]
    parsed_content = env.parse(template_source)
    variables = sorted(list(meta.find_undeclared_variables(parsed_content)))
    return variables


def print_vars(name):
    variables = get_vars(name)
    default_context = get_default_context()
    if len(variables) == 0:
        return "The {0} template don't need variables.".format(name.upper())
    else:
        result = ("The {0} template contains following "
                  "defaults:\n").format(name.upper())
        for variable in variables:
            result = result + "\t{0}: {1}\n".format(
                variable, default_context[variable])
        result = result + "You can overwrite them at your ease."
    return result


def main():
    arguments = docopt(__doc__, version=__version__)
    raw_context = {'year': arguments['-y'],
                   'fullname': arguments['-f'],
                   'email': arguments['-e']}
    user_context = {key: value for (key, value) in raw_context.items()
                    if value is not None}
    context = get_default_context()
    # Overwrite the default value with user specified.
    for (key, value) in user_context.items():
        context[key] = value

    if arguments['--list'] and arguments['header']:
        print(', '.join(HEADERS))
    elif arguments['--list']:
        print(', '.join(LICENSES))
    elif arguments['LICENSE_HEADER']:
        print(generate_file(arguments['LICENSE_HEADER'],
                            context, 0))
    elif arguments['LICENSE_NAME']:
        print(generate_file(arguments['LICENSE_NAME'],
                            context, 1))
    elif arguments['--var']:
        print(print_vars(arguments['NAME']))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
