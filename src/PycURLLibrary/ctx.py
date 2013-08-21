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
        
    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url
        
    def get_capath(self):
        return self._capath
    
    def set__capath(self, capath):
        self._capath = capath
    
    def get_cert(self):
        return self._cert
    
    def set_cert(self, cert):
        self._cert = cert
    
    def get_key(self):
        return self._key
    
    def set_key(self, key):
        self._key = key
    
    def add_header(self, header):
        self.get_headers().append(header)
        
    def get_headers(self):
        return self._headers
        
    def get_response(self):
        return self._response

    def set_response(self, response):
        self._response = response
