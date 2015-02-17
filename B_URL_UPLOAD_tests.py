import unittest
import os
import B_URL_UPLOAD

os.environ['DATABASE_URL'] = 'sqlite:////tmp/test.db'

class HomeTestCase(unittest.TestCase):

#    def setUp(self):
        

#    def tearDown(self):


    def test_ut_validate_url(self):
        url = "http://www.google.com"
        isValid = B_URL_UPLOAD.validate( url )    	
        self.assertTrue( isValid)
    	


    #def ut_test_invalid_url(self):
    	#call method under test with valid url parameter
    	
    	#assert that url is validated successfully



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
        
