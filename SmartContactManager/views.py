#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: views.py
#  Version: 0.0.1
#  Summary: Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""Provides views to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from model import ContactModel

# Some useful variables.
TITLE = 'Smart Contact Manager'
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600


class MainWindow(QMainWindow):
    """Smart Contact Manager Main MainWindow."""

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

        self.setup_window_ui()

    def setup_window_ui(self):
        """Setup the main window's GUI."""

        # Create the table view widget.
        self.table = QTableView()
        self.table.setModel(self.contacts_model.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create the buttons.
        self.add_button = QPushButton('Adicionar...')
        self.add_button.clicked.connect(self.open_add_dialog)

        self.edit_button = QPushButton('Editar')
        self.edit_button.clicked.connect(self.open_edit_dialog)

        self.delete_button = QPushButton('Deletar')
        self.delete_button.clicked.connect(self.delete_contact)

        self.clear_all_button = QPushButton('Apagar informações')
        self.clear_all_button.clicked.connect(self.clear_contacts_database)

        # Populate the layout of the application.
        layout = QVBoxLayout()
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addStretch()
        layout.addWidget(self.clear_all_button)

        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def open_add_dialog(self):
        """Open the Add Contact dialog."""

        dialog = ContactAddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contacts_model.add_contact(dialog.data)
            self.table.resizeColumnsToContents()

    def open_edit_dialog(self):
        """Open the Edit Contact dialog."""

        row = self.table.currentIndex().row()
        if row > 0:
            record = self.contacts_model.model.record(row)

            dialog = ContactEditDialog(record)
            if dialog.exec() == QDialog.Accepted:
                self.contacts_model.edit_contact(row, dialog.data)
                self.table.resizeColumnsToContents()
        else:
            QMessageBox.warning(self,
                                'Warming!',
                                'Please select a row would you like to update.',
                                QMessageBox.Ok)

    def delete_contact(self):
        """Delete the selected contact from the database."""

        row = self.table.currentIndex().row()
        if row < 0:
            QMessageBox.warning(self,
                                'Warming!',
                                'Please select a row would you like to delete.',
                                QMessageBox.Ok)
        else:
            message_box = QMessageBox.critical(self,
                                               'Warming!',
                                               'Do you want remove the selected contact?',
                                               QMessageBox.Ok | QMessageBox.Cancel)

            if message_box == QMessageBox.Ok:
                self.contacts_model.delete_contact(row)

    def clear_contacts_database(self):
        """Remove all contacts from the database."""

        message_box = QMessageBox.warning(self,
                                          'Warning!',
                                          'Do you want to remove all your contacts?',
                                          QMessageBox.Ok | QMessageBox.Cancel)

        if message_box == QMessageBox.Ok:
            self.contacts_model.clear_database_contacts()


class ContactAddDialog(QDialog):
    """Add contact dialog."""

    def __init__(self, parent=None):
        """Initializer."""

        super().__init__(parent=parent)
        self.setWindowTitle('Adicionar Contato...')
        self.resize(400, 250)
        self.layout = QVBoxLayout()
        self.buttons_box = QDialogButtonBox(self)

        self.setLayout(self.layout)
        self.data = None

        self.setup_dialog_ui()

    def setup_dialog_ui(self):
        """Setup the Add Contact dialog's GUI."""

        # Create line edits for data fields.
        self.name_field = QLineEdit()
        self.name_field.setObjectName('NOME')

        self.email_field = QLineEdit()
        self.email_field.setObjectName('E-MAIL')

        self.phone_field = QLineEdit()
        self.phone_field.setObjectName('TELEFONE')

        self.company_field = QLineEdit()
        self.company_field.setObjectName('EMPRESA')

        # Populate the data layout fields.
        layout = QFormLayout()
        layout.addRow('NOME:', self.name_field)
        layout.addRow('E-MAIL:', self.email_field)
        layout.addRow('TELEFONE:', self.phone_field)
        layout.addRow('EMPRESA:', self.company_field)
        self.layout.addLayout(layout)

        # Add standard buttons to the dialog and connect them.
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons_box.accepted.connect(self.dialog_accept)
        self.buttons_box.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons_box)

    def dialog_accept(self):
        """Accept the data provided through the dialog."""

        self.data = list()

        for field in (self.name_field, self.email_field, self.phone_field, self.company_field):
            if not field.text():
                QMessageBox.critical(self,
                                     'Error!',
                                     f"You must provide a contact's {field.objectName()}")
                # Reset self.data
                self.data = None
                return

            self.data.append(field.text())

            if not self.data:
                return

            super().accept()


class ContactEditDialog(QDialog):
    """Edit contact dialog."""

    def __init__(self, data, parent=None):
        """Initializer."""

        super().__init__(parent=parent)
        self.setWindowTitle('Editar Contato...')
        self.resize(400, 250)
        self.layout = QVBoxLayout()
        self.buttons_box = QDialogButtonBox(self)

        self.setLayout(self.layout)
        self.data = data

        self.setup_dialog_ui()

    def setup_dialog_ui(self):
        """Setup the Add Contact dialog's GUI."""

        # Create line edits for data fields.
        self.name_field = QLineEdit()
        self.name_field.setObjectName('NOME')
        self.name_field.setText(self.data.field(1).value())

        self.email_field = QLineEdit()
        self.email_field.setObjectName('E-MAIL')
        self.email_field.setText(self.data.field(2).value())

        self.phone_field = QLineEdit()
        self.phone_field.setObjectName('TELEFONE')
        self.phone_field.setText(self.data.field(3).value())

        self.company_field = QLineEdit()
        self.company_field.setObjectName('EMPRESA')
        self.company_field.setText(self.data.field(4).value())

        # Populate the data layout fields.
        layout = QFormLayout()
        layout.addRow('NOME:', self.name_field)
        layout.addRow('E-MAIL', self.email_field)
        layout.addRow('TELEFONE', self.phone_field)
        layout.addRow('EMPRESA', self.company_field)
        self.layout.addLayout(layout)

        # Add standard buttons to the dialog and connect them.
        self.buttons_box.setOrientation(Qt.Horizontal)
        self.buttons_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons_box.accepted.connect(self.dialog_accept)
        self.buttons_box.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons_box)

    def dialog_accept(self):
        """Accept the data provided through the dialog."""

        self.data = list()

        for field in (self.name_field, self.email_field, self.phone_field, self.company_field):
            self.data.append(field.text())

            if not self.data:
                return

            super().accept()
