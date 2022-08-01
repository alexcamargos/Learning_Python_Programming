#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: creating_tables.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Create tables in the database."""

from sqlalchemy import create_engine

from models import metadata

# Configurações
engine = create_engine('sqlite:///books.db', echo=True, future=True)

print('Creating tables...')
metadata.create_all(engine)
