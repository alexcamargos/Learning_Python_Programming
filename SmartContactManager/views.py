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
