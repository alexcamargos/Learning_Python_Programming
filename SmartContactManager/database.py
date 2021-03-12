#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: database.py
#  Version: 0.0.1
#  Summary: Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""This module provides a database connection."""

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QMessageBox


def create_connection(database_name):
    """Create and open a database connection."""

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(database_name)

    if not connection.open():
        QMessageBox.warning(None,
                            "Smart Contact Manager",
                            f"Database Error: {connection.lastError().text()}")
        return False

    __create_contacts_table()

    return True


def __create_contacts_table():
    """Create the contacts table in the database."""

    create_table_query = QSqlQuery()

    return create_table_query.exec(
        """
        CREATE TABLE Contacts (
            ContactID   INTEGER       PRIMARY KEY AUTOINCREMENT
                                      NOT NULL
                                      UNIQUE,
            Name        VARCHAR (120) NOT NULL,
            Email       VARCHAR (60)  NOT NULL,
            PhoneNumber VARCHAR (12),
            Company     VARCHAR (60)
            );
        """)
