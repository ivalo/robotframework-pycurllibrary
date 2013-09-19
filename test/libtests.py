'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
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

    def testSetterStyleKeywords(self):
        lib = PycURLLibrary();
        
        lib.verbose()
        lib.insecure_ssl()
        lib.request_method('GET')
        lib.add_header('Content-Type: text/xml; charset=UTF-8')
        lib.add_header('Version: 1')
        
        lib.set_url('http://localhost:53004/rest')
        lib.ca_path('/tmp')
        lib.client_certificate_file('cert.pem')
        lib.private_key_file('key.pem')
        lib.post_fields('testing')
        postFieldsFile = join(testenv.ROOT_DIR, 'soap-request.xml')
        lib.post_fields_file(postFieldsFile)
        lib.server_connection_establishment_timeout('30')
        pass

    def testget(self):
        lib = PycURLLibrary();
        
        lib.verbose()
        lib.add_header('Content-Type: text/xml; charset=UTF-8')
        lib.add_header('Version: 1')
        
        lib.set_url('http://localhost:53004/rest')

        lib.perform()
        response = lib.response()
        if response is None:
            raise NotImplementedError
        print 'GET Response:'
        print response
        responseHeader = lib.response_headers()
        print 'GET Response Headers:'
        print responseHeader
        pass

    def testgetHeaderFile(self):
        lib = PycURLLibrary();
        
        lib.verbose()
        headerFile = join(testenv.ROOT_DIR, 'headers-file.txt')
        lib.headers_file(headerFile)
        
        lib.set_url('http://localhost:53004/rest')

        lib.perform()
        response = lib.response()
        if response is None:
            raise NotImplementedError
        print 'GET Response:'
        print response
        responseHeader = lib.response_headers()
        print 'GET Response Headers:'
        print responseHeader
        pass

    def testpost(self):
        lib = PycURLLibrary();
        messageFile = join(testenv.ROOT_DIR, 'soap-request.xml')
        print messageFile
        f = open(messageFile, 'r')
        data = f.read()
        f.close()
        
        lib.verbose()
        
        lib.set_url('http://localhost:53004/soap')

        lib.post_fields(data)
        lib.perform()
        response = lib.response()
        if response is None:
            raise NotImplementedError
        print 'POST Response:'
        print response
        responseHeader = lib.response_headers()
        print 'POST Response Headers:'
        print responseHeader
        responseStatus = lib.http_response_status()
        print 'HTTP Response Status:'
        print responseStatus
        root = lib.parse_xml()
        print root
        elems = lib.find_elements(root, 'country')
        print elems
        pass

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
