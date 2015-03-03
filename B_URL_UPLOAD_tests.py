import unittest
import os
import B_URL_UPLOAD
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from B_URL_UPLOAD import Model
from B_URL_UPLOAD import UrlModel, UrlExtModel

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()





class HomeTestCase(unittest.TestCase):

    def setUp(self):
        Model.metadata.create_all(engine)

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
 
        except MultipleResultsFound, e:
            assert "One record expected. More than one found"
        except NoResultFound, e:
            assert "One record expected. No record found"
        except:
            print sys.exc_info()
            self.fail("Unexpected exception in load()")
        
        self.assertEqual( "www.google.com", instance.url)



if __name__ == '__main__':
    unittest.main()

        
