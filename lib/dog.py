from models import Dog
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

def create_table(base,engine):
    metadata = MetaData()
    base.metadata.create_all(bind=engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    return session.query(Dog).all()
    pass

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed ==breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    return session.query(Dog).update({
        Dog.breed: breed
    })
    pass