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
Created on 30 May 2013

@author: Markku Saarela
'''

class Ctx(object):
    def __init__(self):
        self._url = None
        self._response = None
        self._capath = None
        self._cert = None
        self._key = None
        self._headers = []
        self._response_header = None
        self._protocol = None
        self._request_method = 'GET'
        
    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url
        self._parse_protocol(url)
        
    def get_capath(self):
        return self._capath
    
    def set_capath(self, capath):
        self._capath = capath
    
    def get_cert(self):
        return self._cert
    
    def set_cert(self, cert):
        self._cert = cert
    
    def get_key(self):
        return self._key
    
    def set_key(self, key):
        self._key = key
    
    def get_request_method(self):
        return self._request_method

    def set_request_method(self, requestMethod):
        self._request_method = requestMethod

    def add_header(self, header):
        self.get_headers().append(header)
        
    def get_headers(self):
        return self._headers
        
    def set_headers(self, headers):
        self._headers = headers
        
    def get_response(self):
        return self._response

    def set_response(self, response):
        self._response = response

    def get_response_header(self):
        return self._response_header

    def set_response_header(self, response_header):
        self._response_header = response_header
        
    def get_protocol(self):
        return self._protocol

    def _parse_protocol(self, url):
        i = url.find(':')
        self._protocol = url[0:i].upper()
        
