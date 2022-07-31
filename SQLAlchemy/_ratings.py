#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: _ratings.py
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

from models import Rating

# Configurações
engine = create_engine('sqlite:///books.db', echo=True, future=True)

Session = sessionmaker(bind=engine)
session = Session()

# Ratings
ratings = [1, 2, 3, 4, 5]
# Meanings
ratings_meaning = ['não gostei', 'foi OK', 'gostei', 'gostei muito', 'foi incrível']

new_ratings = [Rating(rating=rating, meaning=meaning) for rating, meaning in zip(ratings, ratings_meaning)]

for i in range(len(new_ratings)):
    session.add(new_ratings[i])

session.commit()

data = session.query(Rating).all()

print(data)
