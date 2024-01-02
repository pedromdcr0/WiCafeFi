from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


database_url = "sqlite:///models/cafes.db"
engine = create_engine(database_url)
Base = declarative_base()


class Cafe(Base):
    __tablename__ = 'cafe'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    map_url = Column(String)
    img_url = Column(String)
    location = Column(String)
    has_socket = Column(Boolean)
    has_toilet = Column(Boolean)
    has_wifi = Column(Boolean)
    can_take_calls = Column(Boolean)
    seats = Column(String)
    coffee_price = Column(String)
    cidade = Column(String, default='London')


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


session.commit()


session.close()
