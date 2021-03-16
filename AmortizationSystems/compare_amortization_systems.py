#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: compare_amortization_systems.py
#  Version: 0.0.1
#  Summary: Para que a dívida seja totalmente paga, o tomador deve quitar o montante inicial adicionado aos juros
#  acrescidos. A forma como o valor total do saldo devedor será calculado é definida de acordo com o sistema de
#  amortização aplicado. Ele caracteriza como a dívida vai ser diminuída até chegar a sua total liquidação.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------


from amortization import TabelaPrice
from amortization import TabelaSAC


def tabela_sac():
    """Sistema de Amortização Constante (SAC)."""

    t_sac = TabelaSAC(100000, 360, 5)
    t_sac.show()


def tabela_price():
    """Amortização por Tabela Price."""

    t_price = TabelaPrice(100000, 360, 5)
    t_price.show()


def main():
    """Função para teste das classes de amortização TabelaSAC e TabelaPrice"""

    tabela_sac()
    print('\n\n')
    tabela_price()


if __name__ == '__main__':
    main()
