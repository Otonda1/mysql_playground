from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
engine = create_engine('mysql+mysqlconnector://otonda:otonda@localhost/newDB')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Parents(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    years = Column(Integer)
    children = relationship('Children', backref='parents')
class Children(Base):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    years = Column(Integer)
    parent_id = Column(Integer, ForeignKey('parents.id'))

parent1 = Parents(name='resper', years=60)
session.add(parent1)
session.commit()
child1 = Children(name='otonda', years=24, parents=parent1)
session.add(child1)
session.commit()
Base.metadata.create_all(engine)
session.commit()
