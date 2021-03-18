#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: model.py
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

"""Provides standard interface to manage the views of Compare Amortization Systems SAC and Price table."""

from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import Qt


class TableModel(QAbstractTableModel):
    """Provides a standard interface for models that represent their data as a two-dimensional array of items."""

    def __init__(self, parent=None):
        """Constructs an abstract table model for the given parent."""

        super().__init__(parent)

        self.my_data = None
        self.header = None

    def set_header(self, header):
        """Defining the head of the columns of the table."""

        self.header = header

    def set_my_data(self, data):
        """Defining the data of the table."""

        self.my_data = data

    def rowCount(self, parent, *args, **kwargs):
        return len(self.my_data)

    def columnCount(self, parent, *args, **kwarg):
        return len(self.my_data[0])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        else:
            return None

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        else:
            # Get the raw value
            value = self.my_data[index.row()][index.column()]
            # Perform per-type checks and render accordingly.
            if isinstance(value, float):
                # Render float to two decimal places.
                return f'R${value :.2f}'
            else:
                # Default (anything not captured above: e.g. int).
                return value
