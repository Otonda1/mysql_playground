from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+mysqlconnector://otonda:otonda@localhost/newDB')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Manager(Base):
    __tablename__ = 'manager'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    project = relationship('Project', backref='manager')
class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    years = Column(Integer)
    manager_id = Column(Integer, ForeignKey('manager.id'))
Base.metadata.create_all(engine)
manager1 = Manager(name='resper', email='cotonda@gmai.com')
manager2 = Manager(name='micheal', email='motonda@gmail.com')
session.add(manager2)
session.add(manager1)
session.commit()
project1 = Project(name='otonda', years=24, manager=manager1)
project2=Project(name='chege', years=13, manager=manager1)
session.add(project1)
session.add(project2)
session.commit()
