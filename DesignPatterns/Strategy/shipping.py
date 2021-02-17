#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: shipping.py
#  Version: 0.1
#  Summary: Interface onde realizamos e mostrados as operações.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""shipping.py - Interface onde realizamos e mostrados as operações."""


from calculate_shipping import CalculateShipping
from order import Order


order = Order(250)
shipping = CalculateShipping(order)
print(f'Valor da compra: R${order.value :.2f}')
print(f'Valor do frente normal: R${shipping.execute_calculation() :.2f}')
print(f'Valor do frente expresso: R${shipping.execute_calculation("Express") :.2f}')
