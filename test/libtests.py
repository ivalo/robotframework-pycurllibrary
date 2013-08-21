'''
Created on 28 May 2013

@author: Markku Saarela
'''
import unittest
import testenv
from os.path import join
from PycURLLibrary import PycURLLibrary

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testget(self):
        lib = PycURLLibrary();
        messageFile = join(testenv.ROOT_DIR, 'message_rest.xml')
        print messageFile
        lib.verbose()
        lib.include()
        lib.add_header('Content-Type: text/xml; charset=UTF-8')
        
        #url.set_verbose(True)
        #url.set_include(True)
        #url.set_insecure(True)
        #url.set_data(messageFile)
        lib.set_url('http://www.google.fi:80')
        lib.data_file(messageFile)
        response = lib.perform()
        if response is None:
            raise NotImplementedError
        print 'Response:'
        print response
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
