#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: amortization.py
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


class Amortization:

    def __init__(self):
        self.amortization = list()

    @staticmethod
    def taxa_equivalente(taxa, periodo_da_taxa_atual, periodo_da_taxa_equivalente):
        """Realiza a conversão de uma taxa de juros dada ao ano para taxa de juros ao mês.

        1 + taxa equivalente = (1 + taxa de juros)período da taxa equivalente/período da taxa atual

        Primeiro você deve transformar esses 2% dividindo o número 2 por 100
        para encontrar 0,02 dessa forma: 2% = 2/100 = 0,02. O período da taxa
        equivalente que queremos descobrir é 12 meses.

        O período da taxa atual que temos é de 1 mês, então utilizaremos 12/1 = 12.
        1 + taxa equivalente = (1 + 0,02)12/1
        1 + taxa equivalente = 1,0212
        1 + taxa equivalente = 1,2682
        taxa equivalente = 1,2682 – 1
        taxa equivalente = 0,2682
        taxa equivalente = 26,82%

        A taxa anual de juros equivalente a 2% ao mês é de 26,82%.

        """

        taxa /= 100

        return ((1 + taxa) ** (periodo_da_taxa_equivalente / periodo_da_taxa_atual)) - 1

    def calcular(self):
        """Calcula as parcelas, amortizações, juros e evolução do saldo devedor."""

        # Deve ser implementado nas classes filhas.
        pass

    def show(self):
        """Mostra uma tabela contendo todas as parcelas da operação de financiamento, no padrão:

        #    Parcelas    Amortizações    Juros    Saldo Devedor

        """

        # Realiza o calculo das parcelas a serem pagas durante o financiamento.
        self.calcular()

        # Totalizando os valores pagos durante a operação de financiamento.
        total_parcela = 0
        total_amortization = 0
        total_juros = 0

        print('{:<5}{:<12}{:<16}{:<12}{:<12}'.format('#', 'Parcelas', 'Amortizações', 'Juros', 'Saldo Devedor'))
        for pmt, pgto, amortization, juros, saldo_devedor in self.amortization:
            print(f'{pmt:<5}R${pgto:<10.2f}R${amortization:<16.2f}R${juros:<10.2f}R${saldo_devedor:<10.2f}')

            total_parcela += pgto
            total_amortization += amortization
            total_juros += juros

        print('Parcela = Amortização + Juro')
        print(f'\nValor total pago de Parcelas: R${total_parcela:.2f}')
        print(f'Valor total pago de Amortizações: R${total_amortization:.2f}')
        print(f'Valor total pago de Juros: R${total_juros:.2f}')


class TabelaSAC(Amortization):
    """O Sistema de Amortização Constante (SAC) ou Método Hamburguês consiste na amortização constante da dívida com
    base em pagamentos periódicos decrescentes. Ou seja, quanto mais o tempo passa, menores ficam as parcelas de
    quitação do saldo devedor enquanto o valor é amortizado de maneira constante em todos os períodos.

    De forma geral, os juros e o capital são calculados uma única vez e divididos para o pagamento
    em várias parcelas durante o prazo de quitação.

    """

    def __init__(self, present_value, period, interest_rate):
        """
        Sistema de Amortização Constante (SAC) ou Método Hamburguês

        :param present_value: Valor total do empréstimo ou financiamento.
        :param period: Número de parcelas.
        :param interest_rate: Taxa de juros
        """

        super().__init__()

        self.__present_value = present_value
        self.__period = period
        self.__interest_rate = self.taxa_equivalente(interest_rate, 12, 1)
        self.amortization = []

    def calcular(self):
        """Calcula as parcelas, amortizações, juros e evolução do saldo devedor."""

        amortization = round(self.__present_value / self.__period, 2)
        saldo_devedor = self.__present_value

        # Rotina de cálculo de cada prestação mensal.
        for pmt in range(1, (self.__period + 1)):
            juros = round(saldo_devedor * self.__interest_rate, 2)
            # pagamento = amortização + juros Sobre Saldo Devedor
            pgto = amortization + juros
            saldo_devedor -= amortization
            self.amortization.append([pmt, pgto, amortization, juros, saldo_devedor])


class TabelaPrice(Amortization):
    """O modelo de amortização por Tabela Price é um dos mais conhecidos. Por ele, o montante total é amortizado ao
    longo do contrato e de forma crescente. Assim, o pagamento é feito através de um conjunto de prestações
    sucessivas e constantes.

    Geralmente, as parcelas são pagas mensalmente em valores iguais, já com os juros embutidos. Também pode ser
    chamado de Sistema de Parcelas Fixas ou Sistema Francês.

    """

    def __init__(self, present_value, period, interest_rate):
        """Amortização por Tabela Price

        :param present_value: Valor total do empréstimo ou financiamento.
        :param period: Número de parcelas.
        :param interest_rate: Taxa de juros

        """

        super().__init__()

        self.__present_value = present_value
        self.__period = period
        self.__interest_rate = self.taxa_equivalente(interest_rate, 12, 1)

        self.__parcela = self.payment_value()
        self.amortization = []

    def payment_value(self):
        """A tabela Price usa o regime de juros compostos para calcular o valor das parcelas de um empréstimo e,
        dessa parcela, há uma proporção relativa ao pagamento de juros e amortização do valor emprestado."""

        return (self.__present_value * self.__interest_rate) / (1 - (1 + self.__interest_rate) ** -self.__period)

    def calcular(self):
        """Calcula as parcelas, amortizações, juros e evolução do saldo devedor."""

        saldo_devedor = self.__present_value

        # Rotina de cálculo de cada prestação mensal.
        for pmt in range(1, (self.__period + 1)):
            juros = round(saldo_devedor * self.__interest_rate, 2)
            amortization = self.__parcela - juros
            saldo_devedor -= amortization
            self.amortization.append([pmt, self.__parcela, amortization, juros, saldo_devedor])
