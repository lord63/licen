#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import re
import codecs

from licen.main import *


class TestLicen():
    def test_list_licenses(self):
        assert sorted(next(os.walk(LICENSES_DIR))[2]) == LICENSES

    def test_list_headers(self):
        assert sorted(next(os.walk(HEADERS_DIR))[2]) == HEADERS

    def test_list_vars(self):
        licenses_and_headers = LICENSES + HEADERS
        for name in licenses_and_headers:
            if 'header' in name:
                file_path = path.join(HEADERS_DIR, name)
            else:
                file_path = path.join(LICENSES_DIR, name)
            with codecs.open(file_path, encoding='utf-8') as f:
                content = f.read()
            variables = sorted(re.findall(r'(?<=\{\{ )\w+(?= \}\})', content))
            assert variables == get_vars(name)

    def test_generate_license(self):
        for license in LICENSES:
            license_path = path.join(LICENSES_DIR, license)
            context = get_default_context()
            with codecs.open(license_path, encoding='utf-8') as f:
                content = f.read()
            for var in re.findall(r'(?<=\{\{ )\w+(?= \}\})', content):
                content = content.replace('{{{{ {0} }}}}'.format(var),
                                          str(context[var]))
            assert content == generate_file(license, context, 1)

    def test_generate_header(self):
        for header in HEADERS:
            header_path = path.join(HEADERS_DIR, header)
            context = get_default_context()
            with codecs.open(header_path, encoding='utf-8') as f:
                content = f.read()
            for var in re.findall(r'(?<=\{\{ )\w+(?= \}\})', content):
                content = content.replace('{{{{ {0} }}}}'.format(var),
                                          str(context[var]))
            assert content == generate_file(header, context, 0)
