#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: dolar_ptax_bacen_api_consumer.py
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


"""Consumindo a API Dólar comercial (venda e compra) - cotações diárias disponibilizada pelo Portal Brasileiro de
Dados Abertos do Banco Central.

Dólar comercial (venda e compra) - cotações diárias:
    https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios

Documentação da API:
    Documentação
URL: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao

"""

import json
from datetime import date
from enum import Enum

import requests
from workalendar.america.brazil import BrazilSaoPauloCity as HolidaySaoPaulo


class DadosAbertosBancoCentralException(BaseException):
    pass


class ModosConsulta(Enum):
    """Type of queries enumeration."""
    por_dia = 1
    por_periodo = 2


class DolarPtaxBacen:
    """Dólar Ptax é a média aritmética das taxas obtidas em quatro consultas diárias de câmbio."""

    def __init__(self, mode, data_cotacao=None, period=None):

        self.url = str()
        self.json_string = str()

        if mode == ModosConsulta.por_dia:
            # Check if a day is a holiday or not.
            if self.__is_weekday(data_cotacao):
                raise DadosAbertosBancoCentralException('O mercado fechado aos sábados e domingos.')
            # Check if a day is a working day or not.
            if self.__is_holiday(data_cotacao):
                raise DadosAbertosBancoCentralException('O mercado fechado aos feriados')

            self.url = self.setup_url(mode=mode, data_cotacao=data_cotacao)
        elif mode == ModosConsulta.por_periodo:
            self.url = self.setup_url(mode=mode, period=period)
        else:
            raise DadosAbertosBancoCentralException('Tipo de consulta invalida.')

        response = self.get_data(self.url)
        if response.status_code != requests.codes.ok:
            raise DadosAbertosBancoCentralException(response.raise_for_status())
        else:
            result = response.content.decode('utf-8')
            self.json_string = json.loads(result)

    @staticmethod
    def __is_holiday(day):
        """Check if a day is a holiday or not."""

        calendar_holiday = HolidaySaoPaulo()
        if calendar_holiday.is_working_day(day):
            return False
        else:
            return True

    @staticmethod
    def __is_weekday(day):
        """Check if a day is a working day or not."""

        # Monday == 1, Tuesday == 2, Wednesday == 3, Thursday == 4, Friday == 5, Saturday == 6, Sunday == 7
        if date.weekday(day) in [5, 6]:
            return True
        else:
            return False

    @staticmethod
    def setup_url(mode, data_cotacao=None, period=None):
        """Manipulação os parâmetros para construção da URL de consulta da API."""

        # Endereço padrão da API, dados retornados em formato json.
        url_base = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'

        if mode == ModosConsulta.por_dia:
            data = data_cotacao.strftime('%m-%d-%Y')
            url_resouce = 'CotacaoDolarDia(dataCotacao=@dataCotacao)?'
            url_parameters = f'@dataCotacao=%27{data}%27&$format=json'
        elif mode == ModosConsulta.por_periodo:
            data_inicial_cotacao = period['inicial'].strftime('%m-%d-%Y')
            data_final_cotacao = period['final'].strftime('%m-%d-%Y')
            url_resouce = 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
            url_parameters = f'@dataInicial=%27{data_inicial_cotacao}%27&@dataFinalCotacao=%27{data_final_cotacao}%27&$top=100&$format=json'
        else:
            raise DadosAbertosBancoCentralException('Tipo de consulta invalida.')

        return f'{url_base}{url_resouce}{url_parameters}'

    @staticmethod
    def get_data(url):
        _headers = {
            "Host": "olinda.bcb.gov.br",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36",
            "DNT": "1",
            "Content-Type": "application/json;charset=UTF-8;odata.metadata=minimal",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,mt;q=0.6,gl;q=0.5,he;q=0.4,ru;q=0.3,pl;q=0.2,"
                               "la;q=0.1,es;q=0.1,fr;q=0.1,de;q=0.1,cy;q=0.1,und;q=0.1",
        }

        return requests.get(url, headers=_headers, timeout=None)

    @property
    def valor_compra(self):
        """Cotação de compra do dólar contra a unidade monetária corrente:
        unidade monetária corrente/dólar americano."""
        return self.json_string['value'][0]['cotacaoCompra']

    @property
    def valor_venda(self):
        """Cotação de venda do dólar contra a unidade monetária corrente:
        unidade monetária corrente/dólar americano."""
        return self.json_string['value'][0]['cotacaoVenda']

    @property
    def data_ultima_cotacao(self):
        """Data, hora e minuto das cotações de compra e venda."""
        return self.json_string['value'][0]['dataHoraCotacao']
