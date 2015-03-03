import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

Model = declarative_base()

class UrlModel(Model):
    __tablename__ = 'URL'
    id = Column(Integer, primary_key=True)
    url = Column(String(1000))
    
    def __init__(self, url):
        self.url = url
    
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {

           "url" : self.url

       }    



def validate( url ):
    p = re.compile('^[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU)[a-zA-Z0-9\-\./]*$')
    m = p.match(url)

    if m:
        is_match = True
    else:
        is_match = False

    return is_match



def load(session):
    for instance in session.query(UrlExtModel).order_by(UrlExtModel.url):
        if validate( instance.url ):
            url = UrlModel(url=instance.url)
            session.add(url)
    session.commit()        


#if __name__ == '__main__':
    #TODO initialise DB session

