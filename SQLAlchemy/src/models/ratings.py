#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: ratings.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models to represent information of ratings."""

from sqlalchemy import Column, Integer, String, ForeignKey

from database_connection.base import Base


class Rating(Base):
    """An entity to represent ratings.

    The meaning of the rating is stored in the database as a string,
    but the rating is stored as an integer.

    ratings are:
         1 - não gostei
         2 - foi OK
         3 - gostei
         4 - gostei muito
         5 - foi incrível

    """

    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, unique=True)
    meaning = Column(String(64))
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Ratings(rating={self.rating} - {self.meaning})'
