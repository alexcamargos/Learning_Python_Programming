#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: main.py
#  Version: 0.0.1
#  Summary: Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------


"""Smart Contact Manager a contact book GUI application with Python, SQLite, and PyQt."""

import sys

from PyQt5.QtWidgets import QApplication

from database import create_connection
from views import MainWindow

# Some useful variables.
DATABASEPATH = r'resources\data_base\smart_contact_manager.sqlite'


def main():
    """Smart Contact Manager main function."""

    # Create the application.
    app = QApplication(sys.argv)

    # Connect to the database before creating any window.
    if not create_connection(DATABASEPATH):
        sys.exit(1)

    # Create the main window if the connection succeeded.
    window = MainWindow()
    window.show()

    # The event loop.
    sys.exit(app.exec_())
