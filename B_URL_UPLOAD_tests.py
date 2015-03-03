import unittest
import os
import B_URL_UPLOAD
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from B_URL_UPLOAD import Model

engine = create_engine('sqlite:///:memory:', echo=True)
Model.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



class UrlExtModel(Model):
    __tablename__ = 'URL_EXT'
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


class HomeTestCase(unittest.TestCase):

    def setUp(self):
        google_url1 = UrlExtModel(url='www.google.com')
        session.add(google_url1)
        
        google_url2 = UrlExtModel(url='www/google.com')
        session.add(google_url2)
        session.commit()
    

    def tearDown(self):   
        session.close()



    def test_ut_validate_url(self):
        url = "www.google.com"
        isValid = B_URL_UPLOAD.validate( url )    	
        self.assertTrue( isValid)
    	


    def test_ut_invalid_url(self):
        url = "www/google.com"
        isValid = B_URL_UPLOAD.validate( url )      
        self.assertFalse( isValid)



    def test_it_load_data(self):    	
    	try:
            B_URL_UPLOAD.load( session )
            instance = session.query(UrlModel).one()
            self.assertEqual( "www.google.com", instance.url)

        except MultipleResultsFound, e:
            assert "One record expected. More than one found"
        except NoResultFound, e:
            assert "One record expected. No record found"
        except:
            self.fail("Unexpected exception in load()")



if __name__ == '__main__':
    unittest.main()

        
