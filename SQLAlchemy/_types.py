#  #!/usr/bin/env python
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

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Kind

# Configurações
engine = create_engine('sqlite:///books.db', echo=True, future=True)

Session = sessionmaker(bind=engine)
session = Session()

# Tipos
types = ['Papel', 'Ebook / Digital', 'Audio Book']

new_types = [Kind(type=kind) for kind in types]

for num in range(len(new_types)):
    session.add(new_types[num])

session.commit()

data = session.query(Kind).all()

print(data)
