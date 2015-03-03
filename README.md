# Licen
[![Latest Version][1]][2]

Generate your license. Yet another [lice][3], but implement with Jinja.

## Install

    $ pip install licen

## Usage

A gif is worth than a thousand words.

![demo_gif][gif]

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
[3]: https://github.com/licenses/lice
[gif]: https://github.com/lord63/licen/blob/master/licen_demo.gif