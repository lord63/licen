# Licen
[![Latest Version][1]][2]
[![Build Status][3]][4]

Generate your license. Yet another [lice][5], but implemented with Jinja2 and
docopt, should be much more elegant and cleaner. I also get many inspirations
from [joe][6](help you generate gitignore).

## Why and what's the difference

seems better than lice:

* Licen use Jinja2 as its template engine, sweet and easy. Lice do it by hand.
* Licen use docopt for the command line interface. Lice use argparse.
* Licen don't render the boilerplate in the license template. Lice do. Check
  out the issue [here][].
* Licen is pep8 checked. Lice don't.

seems not good as lice:

* Licen support less licenses. Check [issue#1][]
* Licen haven't support comment the license header yet. Check [issue#2][]

## Install

    $ pip install licen

## Usage

NOTE: because licen use the git configuration(user.name and user.email) as
default context, please make sure that you've set up git properly. You can
check this [guide][] if you have done yet.

A gif is worth than a thousand words.

![demo_gif][gif]

In short, generate a licnese:

    $ licen mit > LICENSE

Generate a header:

    $ licen header gpl-2.0-header > main.py

Or get detailed help message from the terminal.

    $ licen -h
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

## License

MIT.


[1]: http://img.shields.io/pypi/v/licen.svg
[2]: https://pypi.python.org/pypi/licen
[3]: https://travis-ci.org/lord63/licen.svg
[4]: https://travis-ci.org/lord63/licen
[5]: https://github.com/licenses/lice
[6]: https://github.com/karan/joe
[guide]: https://help.github.com/articles/set-up-git/
[gif]: https://github.com/lord63/licen/blob/master/licen_demo.gif
[here]: https://github.com/licenses/lice/issues/44
[issue#1]: https://github.com/lord63/licen/issues/1
[issue#2]: https://github.com/lord63/licen/issues/2
