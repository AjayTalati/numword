# -*- coding: utf-8 -*-
#This file is part of numword.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from __future__ import unicode_literals

import sys
from unittest import TestCase


class CompatTestCase(TestCase):
    if sys.version_info[0] == 2:
        def assertRaisesRegex(self, *args, **kwargs):
            return self.assertRaisesRegexp(*args, **kwargs)


class TestNumWordFR(CompatTestCase):

    def test_cardinal(self):
        from numword.numword_fr import cardinal
        self.assertEqual(cardinal(0), "zéro")
        self.assertEqual(cardinal(11.96), "onze virgule quatre-vingt-seize")
        self.assertEqual(cardinal(100), "cent")
        self.assertEqual(cardinal(100.0), "cent")
        self.assertEqual(cardinal(121.01), "cent-vingt-et-un virgule un")
        self.assertEqual(cardinal(3121.45),
                         "trois-mille-cent-vingt-et-un virgule quarante-cinq")

    def test_cardinal_not_a_number(self):
        from numword.numword_fr import cardinal
        error = "type\(Ximinez\) not in \[long, int, float\]"
        with self.assertRaisesRegex(TypeError, error):
            cardinal('Ximinez')

    def test_cardinal_number_too_big(self):
        from numword.numword_fr import cardinal
        from numword.numword_fr import NumWordFR
        max_val = NumWordFR().maxval
        number = max_val + 1
        error = "abs\(%s\) must be less than %s" % (number, max_val)
        with self.assertRaisesRegex(OverflowError, error):
            cardinal(number)


class TestNumWordFR_BE(CompatTestCase):

    def test_cardinal(self):
        from numword.numword_fr_be import cardinal
        self.assertEqual(cardinal(72), "septante-deux")
        self.assertEqual(cardinal(94), "nonante-quatre")
        self.assertEqual(cardinal(93.79),
                         "nonante-trois virgule septante-neuf")


class TestNumWordEN(CompatTestCase):

    def test_cardinal(self):
        from numword.numword_en import cardinal
        self.assertEqual(cardinal(11.96), "eleven point ninety-six")
        self.assertEqual(cardinal(100), "one hundred")
        self.assertEqual(cardinal(100.0), "one hundred")
        self.assertEqual(cardinal(121.01),
                         "one hundred and twenty-one point one")
        self.assertEqual(cardinal(3121.45),
                         "three thousand, one hundred and twenty-one point forty-five")

    def test_cardinal_not_a_number(self):
        from numword.numword_fr import cardinal
        error = "type\(Ximinez\) not in \[long, int, float\]"
        with self.assertRaisesRegex(TypeError, error):
            cardinal('Ximinez')

    def test_cardinal_number_too_big(self):
        from numword.numword_fr import cardinal
        from numword.numword_fr import NumWordFR
        max_val = NumWordFR().maxval
        number = max_val + 1
        error = "abs\(%s\) must be less than %s" % (number, max_val)
        with self.assertRaisesRegex(OverflowError, error):
            cardinal(number)
