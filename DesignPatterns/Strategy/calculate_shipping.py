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


class CalculateShipping:
    """Calcula o valor a ser pago por frente para uma compra.

    order é uma instancia da classe order.Order
    """

    def __init__(self, order):
        self.order = order

        # Taxa utilizada para calculo do valor do frete.
        self.default_rate = .05
        self.express_rate = .10

    def execute_calculation(self, shipping='Default'):
        """Calcula de fato o valor da taxa de frete."""

        if shipping == 'Default':
            return self.order.value * self.default_rate
        else:
            return self.order.value * self.express_rate
