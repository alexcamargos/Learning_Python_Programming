#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: _types.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Construct a base class for declarative class definitions."""

from sqlalchemy.ext.declarative import declarative_base

# Construct a base class for declarative class definitions.
Base = declarative_base()

metadata = Base.metadata
