# -*- coding: utf-8 -*-

import unittest
import re
import unicodedata
import textwrap


def _string_sanity_check(string):
    if string is None:
        return ''
    if not isinstance(string, basestring):
        return str(string)
    return string

''' Return a copy of the string with leading characters removed. '''


def ltrim(string, chars=None):
    sanitzed_string = _string_sanity_check(string)
    if isinstance(chars, int):
        chars = str(chars)
    return sanitzed_string.lstrip(chars)

# ---


class FilterModule(object):

    def filters(self):
        return {
            'ltrim': ltrim
        }

# ---


class TestStringUtlisFunctions(unittest.TestCase):

    def test_ltrim(self):
        self.assertEqual(ltrim(' foo'), 'foo')
        self.assertEqual(ltrim('    foo'), 'foo')
        self.assertEqual(ltrim('foo '), 'foo ')
        self.assertEqual(ltrim(' foo '), 'foo ')
        self.assertEqual(
            ltrim(''), '', 'ltrim empty string should return empty string')
        self.assertEqual(
            ltrim(None), '', 'ltrim null should return empty string')
        self.assertEqual(ltrim('ffoo', 'f'), 'oo')
        self.assertEqual(ltrim('ooff', 'f'), 'ooff')
        self.assertEqual(ltrim('ffooff', 'f'), 'ooff')
        self.assertEqual(ltrim('_-foobar-_', '_-'), 'foobar-_')
        self.assertEqual(ltrim(123, 1), '23')

if __name__ == '__main__':
    unittest.main()
