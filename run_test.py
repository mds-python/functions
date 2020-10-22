# coding: utf-8

import sys
import os
import re

from contextlib import contextmanager
from io import StringIO
import importlib

import random

import unittest

try:
    import functions
except:
    pass


@contextmanager
def capture_stdout():
    old_out = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestPecentage(unittest.TestCase):
    def test_pecentage(self):
        for A,n,p in ((1000, 3, 5), (20, 5, 2)):
            self.assertAlmostEqual(A * (1 + p/100)**n, functions.interest(A=A, n=n, p=p), 2)


class TestTemperature(unittest.TestCase):
    def test_temperature(self):
        for f in (10., 20., 50., 15.):
            self.assertAlmostEqual(5/9 * (f-32), functions.celsius(f), 2)


class TestDollars(unittest.TestCase):
    def test_dollars(self):
        for pln in (10., 20., 50., 15.):
            self.assertAlmostEqual(pln / 3.85, functions.convert_to_usd(pln), 2)


class TestNetto(unittest.TestCase):
    def test_net(self):
        self.assertAlmostEqual(50 / 1.20, functions.calc_net(gross=50, vat=20), 2)

    def test_net_default(self):
        self.assertAlmostEqual(70 / 1.23, functions.calc_net(gross=70), 2)


class TestWords(unittest.TestCase):
    def test_words_default(self):
        words = "Litwo ojczyzno moja ty jesteś jak zdrowie"
        self.assertEqual(['moja', 'ty', 'jak'], functions.get_short_words(words))

    def test_words(self):
        words = "Litwo ojczyzno moja ty jesteś jak zdrowie"
        self.assertEqual(['ty', 'jak'], functions.get_short_words(words, 4))


class TestInitials(unittest.TestCase):
    def test_2_words(self):
        self.assertEqual("A. Einstein", functions.initials("Albert Einstein"))

    def test_3_words(self):
        self.assertEqual("E. A. Poe", functions.initials("Edgar Alan Poe"))

    def test_with_lowercase(self):
        self.assertEqual("E. F. de Choiseul", functions.initials("Etienne Francois de Choiseul"))


class TestMessage(unittest.TestCase):
    def test_message(self):
        data = dict(name="Don Corleone", role="gangster", movie="The Godfather")
        self.assertEqual("In The Godfather, Don Corleone is a gangster.", functions.message(data))

    def test_incomplete(self):
        data = dict(name="Don Corleone", role="gangster", movie="The Godfather")
        data = dict(movie="Kill Bill", role="assassin")
        self.assertIsNone(functions.message(data))


class TestQuadratic(unittest.TestCase):
    def test_two(self):
        self.assertIn(functions.quadratic_equation(1, -5, 4), ((1., 4.), (4., 1.)))

    def test_one(self):
        self.assertEqual(functions.quadratic_equation(1, -2, 1), (1.0,))

    def test_none(self):
        self.assertEqual(functions.quadratic_equation(1, 1, 1), ())

    def test_linear(self):
        self.assertEqual(functions.quadratic_equation(0, 2, -6), (3,))

    def test_linear_none(self):
        self.assertEqual(functions.quadratic_equation(0, 0, 1), ())

    def test_linear_infinity(self):
        self.assertEqual(functions.quadratic_equation(0, 0, 0), ())


class TestDice(unittest.TestCase):
    def assertBetween(self, x, lo, hi):
        if not (lo <= x <= hi):
            raise AssertionError('{!r} not between {!r} and {!r}'.format(x, lo, hi))

    def test_dice(self):
        for _ in range(100):
            self.assertBetween(functions.dice(1), 1, 6)
            self.assertBetween(functions.dice(2), 2, 12)

    def _test_histogram(self, num):
        regex = [re.compile(r"\s*{:2}\s*:\s*#*".format(i)) for i in range(2, 13)]
        with capture_stdout() as out:
            functions.histogram(num)
        result = out.getvalue().rstrip()
        lines = result.split('\n')
        print(lines)
        for l, r in zip(lines, regex):
            if not l.strip(): continue
            self.assertRegex(l, r)
        self.assertEqual(num, sum(1 for c in result if c == '#'))

    def test_histogram_500(self):
        self._test_histogram(500)

    def test_histogram_10(self):
        self._test_histogram(10)
