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
from shippings import Carriers


order = Order(250)
shipping = CalculateShipping(order)
carriers = Carriers()

print(f'Valor da compra: R${order.value :.2f}\n')

print('Valor do frente normal: '
      f'R${shipping.execute_calculation(carriers.calculate_default_shipping) :.2f}')
print('Valor do frente expresso: '
      f'R${shipping.execute_calculation(carriers.calculate_express_shipping) :.2f}')
print('Valor do frente pela Total Express: '
      f'R${shipping.execute_calculation(carriers.calculate_total_express_shipping) :.2f}')
