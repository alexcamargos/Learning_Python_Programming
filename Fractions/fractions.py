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

    # Construction
    def __init__(self, numerator, denominator=1):
        """Initialize self."""

        if denominator == 0:
            raise ZeroDivisionError(f'Fraction({numerator}, 0)')
        elif denominator < 0:
            denominator = -denominator
            numerator = -numerator

        _mdc = self._mdc_euclides(numerator, denominator)

        self._denominator = denominator // _mdc
        self._numerator = numerator // _mdc

    # Representation
    def __repr__(self):
        """Return repr(self)."""
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'

    def __str__(self):
        """Return str(self)."""
        return f'{self.numerator}/{self.denominator}'

    # Conversion
    def __float__(self):
        """Return float(self)."""

        return self.numerator / self.denominator

    def __int__(self):
        """Return int(self)."""

        return self.numerator // self.denominator

    # Operations
    def __add__(self, other):
        """Return self + other."""

        if isinstance(other, int):
            other = Fraction(other)

        # soma a fração self com a fração other.
        new_numerator = (other.denominator * self.numerator) + (self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator

        # construa a fração resultante e a retorna.
        return Fraction(new_numerator, new_denominator)

    __radd__ = __add__

    # TODO: Algumas operações de subtração estão retornando com resultado incorreto.
    def __sub__(self, other):
        """Return self - other."""

        if isinstance(other, int):
            other = Fraction(other)

        # subtrai a fração self com a fração other.
        new_numerator = (other.denominator * self.numerator) - (self.denominator * other.numerator)
        new_denominator = self.denominator * other.denominator

        # construa a fração resultante e a retorna.
        return Fraction(new_numerator, new_denominator)

    __rsub__ = __sub__

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

    def __abs__(self):
        """Return the absolute value of self."""

        return Fraction(abs(self.numerator), abs(self.denominator))

    def __invert__(self):

        """Return the inverse of the self. This is equivalent to ~self."""

        return Fraction(self.denominator, self.numerator)

    def __neg__(self):
        """Return obj negated (-self)."""

        return Fraction(-self.numerator, self.denominator)

    # Rich comparisons
    def __lt__(self, other):
        """Return self < other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator < other.numerator / other.denominator

    def __le__(self, other):
        """Return self <= other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator <= other.numerator / other.denominator

    def __eq__(self, other):
        """Return self == other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator == other.numerator / other.denominator

    def __ne__(self, other):
        """Return self != other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator != other.numerator / other.denominator

    def __gt__(self, other):
        """Return self > other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator > other.numerator / other.denominator

    def __ge__(self, other):
        """Return self >= other."""

        if isinstance(other, int):
            other = Fraction(other)

        return self.numerator / self.denominator >= other.numerator / other.denominator

    # Internal methods
    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @staticmethod
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
