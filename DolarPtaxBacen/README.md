# Cotações diárias do Dólar Ptax

Consumindo a API [Dólar comercial (venda e compra) - cotações diárias](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios) disponibilizada pelo [Portal Brasileiro de Dados Abertos do Banco Central](https://dadosabertos.bcb.gov.br) utilizando [Python’s Requests Library](https://requests.readthedocs.io).

## Como é calculada a taxa Ptax?
O [Banco Central do Brasil (BCB)](https://www.bcb.gov.br) realiza consultas às taxas do dólar, tanto de venda como de compra, quatro vezes ao dia para calcular a média (entre 10h e 10h10; entre 11h e 11h10; entre 12h e 12h10; e, por fim, entre 13h e 13h10).

A partir dos números registrados em cada uma, o BC calcula a média da taxa de câmbio e a divulga logo após última consulta.

## Para que serve a Ptax?
A Ptax é utilizada em diversos produtos do mercado de câmbio, desde os contratos futuros e de opções de câmbio listados na B3 S.A. (Brasil, Bolsa, Balcão) até os contratos derivativos de balcão negociados no mercado local e no exterior, além de operações financeiras de empresas no segmento de câmbio com entrega física. A Ptax também é usada como taxa de referência para contratos denominados em real em bolsas de mercadorias no exterior, como a Chicago Mercantile Exchange (CME) dos EUA. Na prática, também é a principal referência de cotação para o público em geral e para pesquisadores e analistas econômicos.

## Especificação da API
A Especificação da API está definida no site [Dados Abertos do Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios).
