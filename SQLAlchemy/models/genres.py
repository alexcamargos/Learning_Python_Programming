#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: genres.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models to represent information of genres."""

from sqlalchemy import Column, Integer, String, ForeignKey

from database_connection.base import Base


class Genre(Base):
    """An entity to represent genres."""

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String(128), unique=True)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Genres(genre={self.genre})'
