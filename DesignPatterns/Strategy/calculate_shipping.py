#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: calculate_shipping.py
#  Version: 0.1
#  Summary: Implementa o cálculo de frente para uma compra específica.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""calculate_shipping.py - Implementa o cálculo de frente para uma compra específica."""

from shippings import *

class CalculateShipping:
    """Calcula o valor a ser pago por frente para uma compra.

    order é uma instancia da classe order.Order
    """

    def __init__(self, order):
        self.order = order

    def execute_calculation(self, shipping='default'):
        """Calcula de fato o valor da taxa de frete."""

        if shipping.lower() == 'default':
            return calculate_default_shipping(self.order)
        elif shipping.lower() == 'express':
            return calculate_express_shipping(self.order)
        elif shipping.lower() == 'totalexpress':
            return calculate_total_express_shipping(self.order)
        else:
            return 0.0
