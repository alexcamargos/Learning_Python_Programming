#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: select_data.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Select data from database."""

from datetime import date as dt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, Author, Genre, Kind, Publisher, Rating

# Configurações
engine = create_engine('sqlite:///books.db', echo=False, future=True)

Session = sessionmaker(bind=engine)
session = Session()

rating = session.query(Rating).all()

print(rating)

books = session.query(Book) \
    .join(Author, Genre, Kind, Publisher, Rating) \
    .with_entities(Book.title,
                   Author.author,
                   Genre.genre,
                   Publisher.publisher,
                   Book.year_published,
                   Kind.type,
                   Book.date_started,
                   Book.date_finished,
                   Rating.rating,
                   Rating.meaning,
                   Book.review) \
    .all()

for row in books:
    print('-' * 78)
    print(f'Title: {row.title}')
    print(f'Author: {row.author}')
    print(f'Genre: {row.genre}')
    print(f'Publisher: {row.publisher}')
    print(f'Year published: {row.year_published}')
    print(f'Kind: {row.type}')
    print(f'Date started: {dt.fromordinal(row.date_started).strftime("%d/%m/%Y")}')
    print(f'Date finished: {dt.fromordinal(row.date_finished).strftime("%d/%m/%Y")}')
    print(f'Rating: {row.rating} - {row.meaning}')
    print(f'Review: {row.review}')
    print('-' * 78)

session.close()
