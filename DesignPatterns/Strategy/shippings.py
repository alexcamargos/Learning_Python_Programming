#  #!/usr/bin/env python
#  encoding: utf-8
#
#  -----------------------------------------------------------------------------------------------------------------------
#  Name: shippings.py
#  Version: 0.1
#  Summary: Solução modular para cálculo dos valores de frete.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  -----------------------------------------------------------------------------------------------------------------------


"""shippings.py - Solução modular para cálculo dos valores de frete."""

# Valores referencias para os cálculos de fretes.
default_rate = .05
express_rate = .10
total_express_rate = .125


def calculate_default_shipping(order):
    """Cálculo do valor do frete para envio padrão."""
    return order.value * default_rate


def calculate_express_shipping(order):
    """Cálculo do valor do frete para envio express."""
    return order.value * express_rate


def calculate_total_express_shipping(order):
    """Cálculo do valor do frete para envio pela transportadora total express."""
    return order.value * total_express_rate
