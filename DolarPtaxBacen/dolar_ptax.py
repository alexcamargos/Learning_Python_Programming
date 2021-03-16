#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: dolar_ptax.py
#  Version: 0.0.1
#  Summary: Consumindo a API Dólar comercial (venda e compra) - cotações diárias
#           disponibilizada pelo Portal Brasileiro de Dados Abertos do Banco Central.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------


"""Dólar Ptax é a média aritmética das taxas obtidas em quatro consultas diárias de câmbio."""

from datetime import date

from dolar_ptax_bacen_api_consumer import DolarPtaxBacen
from dolar_ptax_bacen_api_consumer import ModosConsulta


def cotacao_dolar_ptax_dia(day):
    """Retorna a Cotação de Compra e a Cotação de Venda da moeda Dólar contra a unidade monetária corrente para a
    data informada."""

    cotacao = DolarPtaxBacen(mode=ModosConsulta.por_dia, data_cotacao=day)

    print('Contação por dia:')
    print(f'\tDolar PTAX Valor Compra: R${cotacao.valor_compra}')
    print(f'\tDolar PTAX Valor Venda: R${cotacao.valor_venda}')
    print(f'\tDolar PTAX Data da última cotação: {cotacao.data_ultima_cotacao}')


def contacao_dolar_ptax_periodo(periodo):
    """Retorna a Cotação de Compra e a Cotação de Venda da moeda Dólar contra a unidade monetária corrente para o
    período informado. """

    cotacao = DolarPtaxBacen(mode=ModosConsulta.por_periodo, period=periodo)

    print('Contação por período:')
    print(f'\tDolar PTAX Valor Compra: R${cotacao.valor_compra}')
    print(f'\tDolar PTAX Valor Venda: R${cotacao.valor_venda}')
    print(f'\tDolar PTAX Data da última cotação: {cotacao.data_ultima_cotacao}')


def main():
    # today = date.today()
    # cotacao_dolar_ptax_dia(today)

    periodo = {
        'inicial': date(2012, 1, 1),
        'final': date(2012, 12, 31)
    }
    contacao_dolar_ptax_periodo(periodo)


if __name__ == '__main__':
    main()
