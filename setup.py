#!/usr/bin/env python
#  -*- coding: utf-8 -*-


from setuptools import setup

import licen


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


setup(
    name='licen',
    version=licen.__version__,
    description='generate the license for you',
    long_description=long_description,
    url='http://github.com/lord63/licen',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3'
    ],
    keywords='license generate cli',
    packages=['licen'],
    install_requires=['docopt==0.6.2',
                      'jinja2>=2.7.3'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'licen=licen.main:main']
    }
)
