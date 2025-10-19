"""! @file tests_math_library.py
@brief Tests for math library
@author xhnato00, xlanro00, xmacho12, xslivk03
"""

import math_library
import unittest

PRECISION = 1e-5

class TestAddition(unittest.TestCase):

    def test_add_two(self):
        self.assertEqual(math_library.add(1, 2), 3)

    def test_add_more(self):
        self.assertEqual(math_library.add(1, 4, 8, 10, 2, -3), 22)

    def test_add_two_float(self):
        self.assertAlmostEqual(math_library.add(1.3, 1.4), 2.7, delta=PRECISION)

class TestSubtraction(unittest.TestCase):

    def test_sub_two(self):
        self.assertEqual(math_library.subtract(4, 3), 1)

    def test_sub_more(self):
        self.assertEqual(math_library.subtract(15, 4, 2, 1, -3), 11)

    def test_sub_two_float(self):
        self.assertAlmostEqual(math_library.subtract(4.8, 3.2), 1.6, delta=PRECISION)

class TestDivision(unittest.TestCase):

    def test_div_two(self):
        self.assertEqual(math_library.divide(10, 2), 5)
        self.assertEqual(math_library.divide(-10, 2), -5)

    def test_div_more(self):
        self.assertEqual(math_library.divide(16, 2, 4), 2)

    def test_div_two_float(self):
        self.assertAlmostEqual(math_library.divide(5, 3), 1.6666667, delta=PRECISION)

class TestMultiplication(unittest.TestCase):

    def test_mul_two(self):
        self.assertEqual(math_library.multiply(2, 8), 16)
        self.assertEqual(math_library.multiply(-30, 2), -60)

    def test_mul_more(self):
        self.assertEqual(math_library.multiply(3, 4, 4), 48)
        self.assertEqual(math_library.multiply(3, 4, -4), -48)

    def test_mul_two_float(self):
        self.assertAlmostEqual(math_library.multiply(4.3, 2.6), 11.18, delta=PRECISION)


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(math_library.factorial(4), 24)

    def test_incorrect_factorial(self):
        with self.assertRaises(Exception):
            math_library.factorial(-3)
        with self.assertRaises(Exception):
            math_library.factorial(3.3)

class TestRoot(unittest.TestCase):

    def test_sqrt(self):
        self.assertEqual(math_library.root(4, 2), 2)
        with self.assertRaises(Exception):
            math_library.root(-2)

    def test_higher_root(self):
        self.assertAlmostEqual(math_library.root(16, 4), 2, delta=PRECISION)
        self.assertAlmostEqual(math_library.root(8, 3), 2, delta=PRECISION)
        with self.assertRaises(Exception):
            math_library.root(-8, 4)

    def test_float_root(self):
        self.assertAlmostEqual(math_library.root(8.8, 2), 2.96647, delta=PRECISION)


class TestExponent(unittest.TestCase):

    def test_2exponent(self):
        self.assertEqual(math_library.exponentiate(4, 2), 16)
        self.assertEqual(math_library.exponentiate(4, 0), 1)
        self.assertEqual(math_library.exponentiate(0, 2), 0)

    def test_bigger_exponent(self):
        self.assertEqual(math_library.exponentiate(2, 4), 16)
        self.assertEqual(math_library.exponentiate(2, 5), 32)

    def test_float_exponent(self):
        self.assertAlmostEqual(math_library.exponentiate(2.356, 2), 5.55073, delta=PRECISION)
        self.assertAlmostEqual(math_library.exponentiate(2.356, 4), 30.81067, delta=PRECISION)


class TestAbs(unittest.TestCase):

    def test_abs(self):
        self.assertEqual(math_library.absolute(8), 8)
        self.assertEqual(math_library.absolute(-8), 8)
        self.assertEqual(math_library.absolute(0), 0)



class TestLogartihm(unittest.TestCase):

    def test_logarithm(self):
        self.assertAlmostEqual(math_library.logarithm(4, 3), 1.26185, delta=PRECISION)
        self.assertAlmostEqual(math_library.logarithm(1, 10), 0, delta=PRECISION)
        self.assertAlmostEqual(math_library.logarithm(10, 5), 1.43067, delta=PRECISION)

    def test_wrong_logarithm(self):
        with self.assertRaises(Exception):
            math_library.logarithm(3, 0)
        with self.assertRaises(Exception):
            math_library.logarithm(10, 1)
        with self.assertRaises(Exception):
            math_library.logarithm(-10, 1)
        with self.assertRaises(Exception):
            math_library.logarithm(-1, 10)



class TestSine(unittest.TestCase):

    def test_sine(self):
        self.assertAlmostEqual(math_library.sine(5), -0.9589242, delta=PRECISION)
        self.assertAlmostEqual(math_library.sine(100), -0.5063656, delta=PRECISION)
        self.assertAlmostEqual(math_library.sine(-5), 0.9589242, delta=PRECISION)
        self.assertAlmostEqual(math_library.sine(0), 0, delta=PRECISION)


class TestCosine(unittest.TestCase):

    def test_cosine(self):
        self.assertAlmostEqual(math_library.cosine(5), 0.2836621, delta=PRECISION)
        self.assertAlmostEqual(math_library.cosine(100), 0.8623188, delta=PRECISION)
        self.assertAlmostEqual(math_library.cosine(-5), 0.2836621, delta=PRECISION)
        self.assertAlmostEqual(math_library.cosine(0), 1, delta=PRECISION)

class TestTangent(unittest.TestCase):

    def test_tangent(self):
        self.assertAlmostEqual(math_library.tangent(5), -3.3805150, delta=PRECISION)
        self.assertAlmostEqual(math_library.tangent(100), -0.5872139, delta=PRECISION)
        self.assertAlmostEqual(math_library.tangent(-5), 3.3805150, delta=PRECISION)
        self.assertAlmostEqual(math_library.tangent(0), 0, delta=PRECISION)





