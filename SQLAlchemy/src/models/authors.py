#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: authors.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Model to represent information of authors."""

from sqlalchemy import Column, Integer, String, ForeignKey

from database_connection.base import Base


class Author(Base):
    """An entity to represent authors."""

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    author = Column(String(255), nullable=False)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Author(author={self.author}'
