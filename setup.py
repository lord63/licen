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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='license generate cli',
    python_requires='>=3.10',
    packages=['licen'],
    install_requires=['docopt==0.6.2',
                      'jinja2>=3.0'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'licen=licen.main:main']
    }
)
