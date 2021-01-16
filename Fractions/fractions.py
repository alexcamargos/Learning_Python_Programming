#!/usr/bin/env python
# encoding: utf-8

# -----------------------------------------------------------------------------------------------------------------------
# Name: fractions.py
# Version: 0.0.1
# Summary: implements a rational numbers
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
# -----------------------------------------------------------------------------------------------------------------------


"""fractions.py - implements a rational numbers.

Esta implementação tem proposito meramente educacional
(estudo do comportamento do processo de sobrecarga de operadores).

Para uso em ambiente de produção recomendo:

from fractions import Fraction
"""


def _mdc_euclides(x, y):
    """"Calcular o máximo divisor comum de x, y.

    Função recursiva para implementar o Algoritmo de Euclides.
    Em matemática, o algoritmo de Euclides é um método simples e eficiente de encontrar o máximo divisor
    comum entre dois números inteiros diferentes de zero. É um dos algoritmos mais antigos,
    conhecido desde que surgiu nos Livros VII e X da obra Elementos de Euclides por volta de 300 a.c..
    O algoritmo não exige qualquer fatoração.
    """

    if y == 0:
        return x
    else:
        return _mdc_euclides(y, x % y)


class Fraction:
    """This class implements rational numbers."""

    def __init__(self, numerator, denominator=1):
        """Initialize self."""

        if denominator == 0:
            raise ZeroDivisionError(f'Fraction({numerator}, 0)')
        elif denominator < 0:
            denominator = -denominator
            numerator = -numerator

        _mdc = _mdc_euclides(numerator, denominator)

        self._denominator = denominator // _mdc
        self._numerator = numerator // _mdc

    def __repr__(self):
        """Return repr(self)."""
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'

    def __str__(self):
        """Return str(self). """
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        """Return self + other."""

        if isinstance(other, int):
            other = Fraction(other)

        # somar a fração self com a fração other
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        # construir a fração resultante e retornar.
        return Fraction(new_numerator, new_denominator)

    __radd__ = __add__

    def __mul__(self, other):
        """Return self * other."""

        if isinstance(other, int):
            other = Fraction(other)

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Return self / other."""

        if isinstance(other, int):
            other = Fraction(other)

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)

    __rtruediv__ = __truediv__

    def __eq__(self, other):
        """Return self = =other."""
        return self.numerator == other.numerator and self.denominator == other.denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator
