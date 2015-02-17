import unittest
import os
import B_URL_UPLOAD
import sqlalchemy

#os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'

class HomeTestCase(unittest.TestCase):

#    def setUp(self):
        

#    def tearDown(self):


    def test_ut_validate_url(self):
        url = "www.google.com"
        isValid = B_URL_UPLOAD.validate( url )    	
        self.assertTrue( isValid)
    	


    def test_ut_invalid_url(self):
        url = "www/google.com"
        isValid = B_URL_UPLOAD.validate( url )      
        self.assertFalse( isValid)



    #def integration_test_load_data(self):
    	#setup: load test data into tmp_ext table with valid url field
    	
    	#call validation method under test
    	
    	#assert that data loaded into url table 
        #self.assertEqual( , )


if __name__ == '__main__':
    unittest.main()

    #def integration_test_reject_data(self):
    	#setup: load test data into tmp_ext table with invalid url field
    	
    	#call validation method under test
    	
    	#assert that data not loaded into url table 
        
