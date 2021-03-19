from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://kani:1@localhost:5432/postgres')
print('connected')

Base = declarative_base()

class Deputy(Base):
    __tablename__ = 'deputy'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    fraction = Column(String)
    commitet = Column(String)
    tel = Column(String)

    def __init__(self, fullname, fraction, commitet, tel):
        self.fullname = fullname
        self.fraction = fraction
        self.commitet = commitet
        self.tel = tel

Base.metadata.create_all(engine)
print('Table created')

from parsing import main

Session = sessionmaker(bind=engine)
session = Session()

data = main()
for one_data in data:
    session.add(Deputy(*one_data))
    print('successfully added')
    session.commit()

    

