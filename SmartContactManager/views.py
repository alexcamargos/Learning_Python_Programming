#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: Smart Contact Manager
#  Version: 0.0.1
#  Summary: Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""Provides views to manage the contacts table."""

from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QVBoxLayout

from model import ContactModel


# Some useful variables.
TITLE = "Smart Contact Manager"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Window(QMainWindow):
    """Smart Contact Manager Main Window."""

    def __init__(self, parent=None):
        """Initializer."""

        super().__init__(parent)
        self.setWindowTitle(TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contacts_model = ContactModel()

        self.setup_app_ui()

    def setup_app_ui(self):
        """Setup the main window's GUI."""

        # Create the table view widget.
        self.table = QTableView()
        self.table.setModel(self.contacts_model.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create the buttons.
        self.add_button = QPushButton("Adicionar...")
        self.edit_button = QPushButton("Editar")
        self.delete_button = QPushButton("Deletar")
        self.clear_all_button = QPushButton("Apagar informações")

        # Populate the layout of the application.
        layout = QVBoxLayout()
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addStretch()
        layout.addWidget(self.clear_all_button)

        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
