#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: views.py
#  Version: 0.0.1
#  Summary: Para que a dívida seja totalmente paga, o tomador deve quitar o montante inicial adicionado aos juros
#  acrescidos. A forma como o valor total do saldo devedor será calculado é definida de acordo com o sistema de
#  amortização aplicado. Ele caracteriza como a dívida vai ser diminuída até chegar a sua total liquidação.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------

"""Provides views to manage the data of Compare Amortization Systems SAC and Price table."""


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFormLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QWidget

from amortization import TabelaPrice
from amortization import TabelaSAC
from model import TableModel


class MainWindow(QMainWindow):
    """Building an application's user interface"""

    def __init__(self, parent=None):
        """Constructs an application for the given parent."""

        super().__init__(parent)

        self.setWindowTitle('Compare Amortization Systems SAC and Price table')
        self.resize(800, 600)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.model_sac = TableModel()
        self.model_price = TableModel()

        self.setup_window_ui()

    def setup_window_ui(self):
        """Setup the main window's GUI."""

        # Create the interface.
        self.__create_status_bar()

        self.__create_valor_emprestimo_financiamento()

        self.__create_numero_parcelas()

        self.__create_taxa_juros()

        self.__create_calcular_push_button()

        ###
        self.valor_emprestimo_financiamento_line_edit.setText('100000')
        self.numero_parcelas_line_edit.setText('360')
        self.taxa_juros_line_edit.setText('5')
        ###

        self.tabela_sac_table_view = QTableView()
        self.tabela_price_table_view = QTableView()

        # Populate the layout of the application.
        self.__populate_layout_application()

    def __create_status_bar(self):
        """Setup the status bar."""

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Aplicação pronta para uso.", 5000)

    def __create_valor_emprestimo_financiamento(self):
        """Setup the valor emprestimo financiamento label."""

        self.valor_emprestimo_financiamento_label = QLabel()
        self.valor_emprestimo_financiamento_label.setText('Valor do empréstimo ou financiamento:')
        self.valor_emprestimo_financiamento_line_edit = QLineEdit()

    def __create_numero_parcelas(self):
        """Setup the numero parcelas label."""

        self.numero_parcelas_label = QLabel()
        self.numero_parcelas_label.setText('Número de parcelas:')
        self.numero_parcelas_line_edit = QLineEdit()

    def __create_taxa_juros(self):
        """Setup the taxa juros label."""

        self.taxa_juros_label = QLabel()
        self.taxa_juros_label.setText('Taxa de juros:')
        self.taxa_juros_line_edit = QLineEdit()

    def __create_calcular_push_button(self):
        """Setup the calcular push button."""

        self.calcular_push_button = QPushButton('&Calcular')
        self.calcular_push_button.clicked.connect(self.populate_information)

    def __populate_layout_application(self):
        """Populate the layout of the application."""

        input_valor_emprestimo_financiamento_layout = QHBoxLayout()
        input_valor_emprestimo_financiamento_layout.addWidget(self.valor_emprestimo_financiamento_label)
        input_valor_emprestimo_financiamento_layout.addWidget(self.valor_emprestimo_financiamento_line_edit)

        input_numero_parcelas_layout = QHBoxLayout()
        input_numero_parcelas_layout.addWidget(self.numero_parcelas_label)
        input_numero_parcelas_layout.addWidget(self.numero_parcelas_line_edit)

        input_taxa_juros_layout = QHBoxLayout()
        input_taxa_juros_layout.addWidget(self.taxa_juros_label)
        input_taxa_juros_layout.addWidget(self.taxa_juros_line_edit)

        table_view_layout = QHBoxLayout()
        table_view_layout.addWidget(self.tabela_sac_table_view)
        table_view_layout.addWidget(self.tabela_price_table_view)

        inputs_layout = QFormLayout()
        inputs_layout.addRow(input_valor_emprestimo_financiamento_layout)
        inputs_layout.addRow(input_numero_parcelas_layout)
        inputs_layout.addRow(input_taxa_juros_layout)
        inputs_layout.addRow(self.calcular_push_button)
        inputs_layout.addRow(table_view_layout)
        self.layout.addLayout(inputs_layout)

    def populate_information(self):
        present_value = int(self.valor_emprestimo_financiamento_line_edit.text())
        period = int(self.numero_parcelas_line_edit.text())
        interest_rate = int(self.taxa_juros_line_edit.text())

        headers = ['#', 'Parcelas', 'Amortizações', 'Juros', 'Saldo Devedor']

        # TABELA SAC
        tabela_sac = TabelaSAC(present_value, period, interest_rate)
        tabela_sac.calcular()
        data_sac = tabela_sac.amortization

        self.model_sac.set_header(headers)
        self.model_sac.set_my_data(data_sac)

        for column_index, header in enumerate(headers):
            self.model_sac.setHeaderData(column_index, Qt.Horizontal, header)

        self.tabela_sac_table_view.setModel(self.model_sac)
        self.tabela_sac_table_view.resizeColumnsToContents()

        # TABELA PRICE
        tabela_price = TabelaPrice(present_value, period, interest_rate)
        tabela_price.calcular()
        data_price = tabela_price.amortization

        self.model_price.set_header(headers)
        self.model_price.set_my_data(data_price)

        for column_index, header in enumerate(headers):
            self.model_price.setHeaderData(column_index, Qt.Horizontal, header)

        self.tabela_price_table_view.setModel(self.model_price)
        self.tabela_price_table_view.resizeColumnsToContents()
