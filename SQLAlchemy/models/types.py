#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: types.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models to represent information of types."""

from sqlalchemy import Column, Integer, String, ForeignKey

from database_connection.base import Base


class Kind(Base):
    """An entity to represent types.

    kinds are:
        Papel
        Ebook / Digital
        Audio Book

    """

    __tablename__ = 'kind'

    id = Column(Integer, primary_key=True)
    type = Column(String(32), unique=True)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Kind(kind={self.type})'
