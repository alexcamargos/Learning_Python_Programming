#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: connection.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Database connection handler for SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dialects = {
    # sqlite://<nohostname>/<path>
    'sqlite': 'sqlite:///%s',
    'mysql': None,
    'postgresql': None,
    'oracle': None,
    'mssql': None
}


class DataBaseConnectionHandler:

    def __init__(self, dialect, driver_name=None, log_informational=False, path=None):
        self.__dialect = dialect
        self.__driver_name = driver_name
        self.__log_informational = log_informational

        if self.__dialect == 'sqlite':
            self.__engine = self.__create_engine_sqlite(path)

    def __create_engine_sqlite(self, path):
        connection_string = dialects.get('sqlite') % path

        return create_engine(connection_string, echo=self.__log_informational, future=True)

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
