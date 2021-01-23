#!/usr/bin/env python
#  encoding: utf-8
#
#  -----------------------------------------------------------------------------------------------------------------------
#  Name: test_fractions.py
#  Version: 0.0.1
#  Summary: Tests for Fraction class.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  -----------------------------------------------------------------------------------------------------------------------

import unittest
from fractions import Fraction


class TestFraction(unittest.TestCase):

    # def test_rational_number_ZeroDivisionError(self):
    #
    #     self.assertRaises(Fraction(4, 0), 'ZeroDivisionError')

    def test_rational_number_representation(self):
        frac1 = Fraction(3)
        self.assertEqual(str(frac1), '3/1')
        self.assertEqual(frac1.numerator, 3)
        self.assertEqual(frac1.denominator, 1)

        frac2 = Fraction(1, 2)
        self.assertEqual(str(frac2), '1/2')
        self.assertEqual(frac2.numerator, 1)
        self.assertEqual(frac2.denominator, 2)

        frac3 = Fraction(1, 3)
        self.assertEqual(str(frac3), '1/3')
        self.assertEqual(frac3.numerator, 1)
        self.assertEqual(frac3.denominator, 3)

        frac4 = Fraction(2, 5)
        self.assertEqual(str(frac4), '2/5')
        self.assertEqual(frac4.numerator, 2)
        self.assertEqual(frac4.denominator, 5)

        frac5 = Fraction(3, 5)
        self.assertEqual(str(frac5), '3/5')
        self.assertEqual(frac5.numerator, 3)
        self.assertEqual(frac5.denominator, 5)

        frac6 = Fraction(7, 9)
        self.assertEqual(str(frac6), '7/9')
        self.assertEqual(frac6.numerator, 7)
        self.assertEqual(frac6.denominator, 9)

        frac7 = Fraction(12, 16)
        self.assertEqual(str(frac7), '3/4')
        self.assertEqual(frac7.numerator, 3)
        self.assertEqual(frac7.denominator, 4)

        frac8 = Fraction(100, 400)
        self.assertEqual(str(frac8), '1/4')
        self.assertEqual(frac8.numerator, 1)
        self.assertEqual(frac8.denominator, 4)

        frac9 = Fraction(8, 4)
        self.assertEqual(str(frac9), '2/1')
        self.assertEqual(frac9.numerator, 2)
        self.assertEqual(frac9.denominator, 1)

        frac10 = Fraction(1, -6)
        self.assertEqual(str(frac10), '-1/6')
        self.assertEqual(frac10.numerator, -1)
        self.assertEqual(frac10.denominator, 6)

        frac11 = Fraction(-2, -6)
        self.assertEqual(str(frac11), '1/3')
        self.assertEqual(frac11.numerator, 1)
        self.assertEqual(frac11.denominator, 3)

    def test_rational_float_conversion(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        frac3 = Fraction(3, 4)
        frac4 = Fraction(4, 5)
        frac5 = Fraction(5, 6)

        self.assertEqual(float(frac1), 0.5)
        self.assertEqual(round(float(frac2), 2), 0.67)
        self.assertEqual(float(frac3), 0.75)
        self.assertEqual(float(frac4), 0.80)
        self.assertEqual(round(float(frac5), 2), 0.83)

    def test_rational_int_conversion(self):
        frac1 = Fraction(6, 5)
        frac2 = Fraction(7, 3)
        frac3 = Fraction(8, 5)
        frac4 = Fraction(9, 2)
        frac5 = Fraction(10, 3)

        self.assertEqual(int(frac1), 1)
        self.assertEqual(int(frac2), 2)
        self.assertEqual(int(frac3), 1)
        self.assertEqual(int(frac4), 4)
        self.assertEqual(int(frac5), 3)

    def test_rational_number_addition(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)
        frac3 = Fraction(5, 3)

        self.assertEqual(str(frac1 + frac2), '5/4')
        self.assertEqual(str(frac1 + frac3), '13/6')
        self.assertEqual(str(frac2 + frac3), '29/12')

        self.assertEqual(str(frac1 + frac1), '1/1')
        self.assertEqual(str(frac2 + frac2), '3/2')
        self.assertEqual(str(frac3 + frac3), '10/3')

        self.assertEqual(str(frac1 + frac2 + frac3), '35/12')
        self.assertEqual(str(frac3 + frac2 + frac1), '35/12')
        self.assertEqual(str(frac3 + frac1 + frac2), '35/12')
        self.assertEqual(str(frac2 + frac1 + frac3), '35/12')
        self.assertEqual(str(frac2 + frac3 + frac1), '35/12')

        self.assertEqual(str(1 + frac1), '3/2')
        self.assertEqual(str(2 + frac1), '5/2')
        self.assertEqual(str(frac1 + 1), '3/2')
        self.assertEqual(str(frac1 + 2), '5/2')

        self.assertEqual(str(1 + frac2), '7/4')
        self.assertEqual(str(2 + frac2), '11/4')
        self.assertEqual(str(frac2 + 1), '7/4')
        self.assertEqual(str(frac2 + 2), '11/4')

        self.assertEqual(str(1 + frac3), '8/3')
        self.assertEqual(str(2 + frac3), '11/3')
        self.assertEqual(str(frac3 + 1), '8/3')
        self.assertEqual(str(frac3 + 2), '11/3')

    def test_rational_number_subtraction(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)
        frac3 = Fraction(5, 3)

        self.assertEqual(str(frac1 - frac2), '-1/4')
        self.assertEqual(str(frac1 - frac3), '-7/6')
        self.assertEqual(str(frac2 - frac3), '-11/12')

        self.assertEqual(str(frac1 - frac1), '0/1')
        self.assertEqual(str(frac2 - frac2), '0/1')
        self.assertEqual(str(frac3 - frac3), '0/1')

        # self.assertEqual(str(frac1 - frac2 - frac3), '-1 11/12')
        self.assertEqual(str(frac3 - frac2 - frac1), '5/12')
        # self.assertEqual(str(frac3 - frac1 - frac2), '1/6')
        # self.assertEqual(str(frac2 - frac1 - frac3), '-1 5/12')
        # self.assertEqual(str(frac2 - frac3 - frac1), '-1 5/12')

        # self.assertEqual(str(1 - frac1), '1/2')
        # self.assertEqual(str(2 - frac1), '1 1/2')
        self.assertEqual(str(frac1 - 1), '-1/2')
        # self.assertEqual(str(frac1 - 2), '-1 1/2')

        # self.assertEqual(str(1 - frac2), '1/4')
        # self.assertEqual(str(2 - frac2), '5/4')
        self.assertEqual(str(frac2 - 1), '-1/4')
        # self.assertEqual(str(frac2 - 2), '-1 1/4')

        # self.assertEqual(str(1 - frac3), '-2/3')
        # self.assertEqual(str(2 - frac3), '1/3')
        self.assertEqual(str(frac3 - 1), '2/3')
        self.assertEqual(str(frac3 - 2), '-1/3')

    def test_rational_number_multiplication(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)

        self.assertEqual(str(frac1 * frac2), '3/8')
        self.assertEqual(str(frac1 * frac1), '1/4')
        self.assertEqual(str(frac2 * frac2), '9/16')

        self.assertEqual(str(1 * frac1), '1/2')
        self.assertEqual(str(2 * frac1), '1/1')
        self.assertEqual(str(1 * frac2), '3/4')
        self.assertEqual(str(2 * frac2), '3/2')

        self.assertEqual(str(frac1 * 1), '1/2')
        self.assertEqual(str(frac1 * 2), '1/1')
        self.assertEqual(str(frac2 * 1), '3/4')
        self.assertEqual(str(frac2 * 2), '3/2')

    def test_rational_number_division(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)
        frac3 = Fraction(5, 3)

        self.assertEqual(str(frac1 / frac1), '1/1')
        self.assertEqual(str(frac1 / frac2), '2/3')
        self.assertEqual(str(frac1 / frac3), '3/10')
        self.assertEqual(str(frac2 / frac2), '1/1')
        self.assertEqual(str(frac2 / frac3), '9/20')
        self.assertEqual(str(frac3 / frac1), '10/3')
        self.assertEqual(str(frac3 / frac2), '20/9')

        self.assertEqual(str(frac1 / 1), '1/2')
        self.assertEqual(str(frac1 / 2), '1/4')
        self.assertEqual(str(frac2 / 1), '3/4')
        self.assertEqual(str(frac2 / 2), '3/8')
        self.assertEqual(str(frac3 / 1), '5/3')
        self.assertEqual(str(frac3 / 2), '5/6')

        # self.assertEqual(str(1 / frac1), '2/1')
        # self.assertEqual(str(2 / frac1), '4/1')
        # self.assertEqual(str(1 / frac2), '3/4')
        # self.assertEqual(str(2 / frac2), '8/3')
        # self.assertEqual(str(1 / frac3), '5/3')
        # self.assertEqual(str(2 / frac3), '5/6')

    def test_rational_absolute_value(self):
        frac1 = Fraction(-1, 5)
        frac2 = Fraction(-2, 6)
        frac3 = Fraction(-3, 7)
        frac4 = Fraction(-4, 8)

        self.assertEqual(str(abs(frac1)), '1/5')
        self.assertEqual(str(abs(frac2)), '1/3')
        self.assertEqual(str(abs(frac3)), '3/7')
        self.assertEqual(str(abs(frac4)), '1/2')

    def test_rational_inverse(self):
        frac1 = Fraction(1, 5)
        frac2 = Fraction(2, 6)
        frac3 = Fraction(3, 7)
        frac4 = Fraction(4, 8)

        self.assertEqual(str(~frac1), '5/1')
        self.assertEqual(str(~frac2), '3/1')
        self.assertEqual(str(~frac3), '7/3')
        self.assertEqual(str(~frac4), '2/1')

    def test_rational_negated(self):
        frac1 = Fraction(1, 5)
        frac2 = Fraction(2, 6)
        frac3 = Fraction(3, 7)
        frac4 = Fraction(4, 8)

        self.assertEqual(str(-frac1), '-1/5')
        self.assertEqual(str(-frac2), '-1/3')
        self.assertEqual(str(-frac3), '-3/7')
        self.assertEqual(str(-frac4), '-1/2')

    def test_rational_number_comparisons(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)
        frac3 = Fraction(1, 2)
        frac4 = Fraction(3, 4)

        self.assertTrue(frac1 == frac1)
        self.assertTrue(frac2 == frac2)
        self.assertTrue(frac3 == frac3)
        self.assertTrue(frac4 == frac4)
        self.assertTrue(frac1 == frac3)
        self.assertTrue(frac2 == frac4)
        self.assertTrue(frac3 == frac1)
        self.assertTrue(frac4 == frac2)

        self.assertFalse(frac1 == frac2)
        self.assertFalse(frac3 == frac4)
        self.assertFalse(frac2 == frac1)
        self.assertFalse(frac4 == frac3)

        self.assertTrue(frac1 != frac2)
        self.assertTrue(frac1 != frac4)
        self.assertTrue(frac2 != frac3)
        self.assertFalse(frac1 != frac3)
        self.assertFalse(frac2 != frac4)

        self.assertFalse(frac1 < frac3)
        self.assertFalse(frac2 < frac4)
        self.assertFalse(frac4 < frac2)
        self.assertFalse(frac4 < frac1)
        self.assertFalse(frac2 < frac1)

        self.assertTrue(frac1 <= frac3)
        self.assertTrue(frac1 <= frac3)
        self.assertTrue(frac2 <= frac4)
        self.assertTrue(frac4 <= frac2)
        self.assertFalse(frac4 <= frac1)
        self.assertFalse(frac2 <= frac1)

        self.assertTrue(frac4 > frac1)
        self.assertTrue(frac2 > frac1)
        self.assertFalse(frac1 > frac3)
        self.assertFalse(frac2 > frac4)
        self.assertFalse(frac4 > frac2)

        self.assertTrue(frac1 >= frac3)
        self.assertTrue(frac4 >= frac1)
        self.assertTrue(frac2 >= frac1)
        self.assertTrue(frac1 >= frac3)
        self.assertTrue(frac2 >= frac4)
        self.assertTrue(frac4 >= frac2)

if __name__ == '__main__':
    unittest.main()
