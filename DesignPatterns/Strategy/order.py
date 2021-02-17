#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: order.py
#  Version: 0.1
#  Summary: Representação de uma transação de compra em um ecommerce.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""order.py - Representação de uma transação de compra em um ecommerce."""


class Order:
    """Representa uma compra dentro de um ecommerce."""

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        """Retorna o valor total da compra."""
        return self.__value
