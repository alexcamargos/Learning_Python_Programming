#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: insert_data.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Insert data into database."""

from datetime import date as dt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, Author, Genre, Kind, Publisher, Rating

# Configurações
engine = create_engine('sqlite:///books.db', echo=True, future=True)

Session = sessionmaker(bind=engine)
session = Session()

# author
author = Author(author='Douglas Adams')
# Genre
genre = Genre(genre='Ficção científica')
# Publisher
publisher = Publisher(publisher='Arqueiro ')
# Kind
kind = Kind(type='Papel')
# Rating
rating = Rating(rating=5, meaning='foi incrível')
# Dates
started = dt(2020, 8, 6).toordinal()
ended = dt(2020, 8, 25).toordinal()
# Review
review = 'Este é o primeiro título da famosa série escrita por Douglas Adams, que conta as ' \
         'aventuras espaciais do inglês Arthur Dent e de seu amigo Ford Prefect.'

# Book
book = Book(title='O guia do mochileiro das galáxias',
            author=[author],
            genre=[genre],
            publisher=[publisher],
            year_published=2010,
            kind=[kind],
            date_started=started,
            date_finished=ended,
            rating=[rating],
            review=review)

session.add(book)
session.commit()

session.close()
