#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: publishers.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models to represent information of publishers."""

from sqlalchemy import Column, Integer, String, ForeignKey

from database_connection.base import Base


class Publisher(Base):
    """An entity to represent publishers."""

    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    publisher = Column(String(128))
    books = Column(Integer, ForeignKey('books.id'))

    def __str__(self):
        return f'Publishers(publisher={self.publisher})'
