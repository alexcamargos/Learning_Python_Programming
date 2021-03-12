#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: model.py
#  Version: 0.0.1
#  Summary: Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""A model to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ContactModel:
    """Hold the data model."""

    def __init__(self):
        """Initializer."""
        self.model = self.__crete_model()

    def add_contact(self, data):
        """Add a contact to the database."""

        rows = self.model.rowCount()
        self.model.insertRow(rows)

        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)

        self.model.submitAll()
        self.model.select()

    def delete_contact(self, row):
        """Remove a contact from the database."""

        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    @staticmethod
    def __crete_model():
        """Create and set uo the model."""

        table_model = QSqlTableModel()
        table_model.setTable("Contacts")
        table_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        table_model.select()
        headers = ("ID", 'NOME', "E-MAIL", "TELEFONE", "EMPRESA")
        for column_index, header in enumerate(headers):
            table_model.setHeaderData(column_index, Qt.Horizontal, header)

        return table_model
