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
Created on 21 Jul 2013

@author: Markku Saarela
'''
from robot.api import logger
from ctx import Ctx
import pycurl
import cStringIO

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

class Url(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._logger = logger
        self._context = Ctx()
        self._post_fields = None
        self._verbose = False
        self._no_buffer = False
        self._insecure = False
        
    def get_post_fields(self):
        return self._data
    
    def set_post_fields(self, postFields):
        self._post_fields = postFields
        
    def get_verbose(self):
        return self._verbose
    
    def set_verbose(self, verbose):
        self._verbose = verbose
        
    def get_no_buffer(self):
        return self._no_buffer
    
    def set_no_buffer(self, no_buffer):
        self._no_buffer = no_buffer
        
    def get_insecure(self):
        return self._insecure
    
    def set_insecure(self, insecure):
        self._insecure = insecure
        
    def get_context(self):
        return self._context

    def set_context(self, context):
        self._context = context

    def perform(self):
        """
        Issues a URL perform.
        
        `url` is the URL relative to t
        """
        self.get_context().set_response(None)
        self.get_context().set_response_headers(None)
        c = pycurl.Curl()
        
        protocol = self.get_context().get_protocol()
        self._logger.info("Protocol %s" % (protocol))
        bufResponseHeader = None
        for case in switch(protocol):
            if case('HTTP'):
                bufResponseHeader = self._prepareHTTP(c)
                break
            if case('HTTPS'):
                bufResponseHeader = self._prepareHTTPS(c)
                break
            if case(): # default
                self._logger.warn("Unknown Protocol %s !" % (protocol))
                # No need to break here, it'll stop anyway
        
        self._setCurlSetopts(c)
        
        bufResponse = cStringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, bufResponse.write)
        
        self._logger.info("Perform %s" % (self.get_context().get_url()))
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
                                                     
        c.perform()
        
        for case in switch(protocol):
            if case('HTTP'):
                if bufResponseHeader is not None:
                    self.get_context().set_response_headers(bufResponseHeader.getvalue())
                    bufResponseHeader.close()
                break
            if case('HTTPS'):
                if bufResponseHeader is not None:
                    self.get_context().set_response_headers(bufResponseHeader.getvalue())
                    bufResponseHeader.close()
                break
            if case(): # default
                break
                # No need to break here, it'll stop anyway
                
        self.get_context().set_response(bufResponse.getvalue())
        bufResponse.close()
        
    def _setCurlSetopts(self, c):
        """
        """
        if self._verbose:
            c.setopt(pycurl.VERBOSE, True)
        
        if self._insecure:
            self._logger.info("Insecure SSL enabled")
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
            c.setopt(pycurl.SSL_VERIFYPEER, 0)
           
        if self.get_context().get_client_certificate_file() is not None:
            cert = self.get_context().get_client_certificate_file();
            self._logger.info("Client Certificate File %s" % (cert))
            try:
                c.setopt(pycurl.SSLCERT, cert)
            except TypeError, t:
                self._logger.warn("Wrong setopt SSLCERT value %s" % (cert))
                raise TypeError(t)

        if self.get_context().get_server_connection_establishment_timeout() is not None:
            self._logger.info("Server Connection Establishment Timeout %d" % (self.get_context().get_server_connection_establishment_timeout()))
            try:
                c.setopt(pycurl.CONNECTTIMEOUT, self.get_context().get_server_connection_establishment_timeout())
            except TypeError, t:
                self._logger.warn("Wrong setopt CONNECTTIMEOUT value %d" % (self.get_context().get_server_connection_establishment_timeout()))
                raise TypeError(t)
            
        if self.get_context().get_capath() is not None:
            capath = self.get_context().get_capath();
            self._logger.info("CA Path %s" % (capath))
            try:
                c.setopt(pycurl.CAPATH, capath)
            except TypeError, t:
                self._logger.warn("Wrong setopt CAPATH value %s" % (capath))
                raise TypeError(t)
            
        if self.get_context().get_private_key_file() is not None:
            privateKey = self.get_context().get_private_key_file()
            self._logger.info("Private Key File %s" % (privateKey))
            try:
                c.setopt(pycurl.SSLKEY, privateKey)
            except TypeError, t:
                self._logger.warn("Wrong setopt SSLKEY value %s" % (privateKey))
                raise TypeError(t)
            
        try:
            c.setopt(pycurl.URL, self.get_context().get_url())
        except TypeError, t:
            self._logger.warn("Wrong setopt URL value %s" % (self.get_context().get_url()))
            raise TypeError(t)
    
    def _prepareCommonHTTP(self, c):
        """
        """
        if self._post_fields is None:
            self._logger.info("No Post Fields")
        else:
            self._logger.info("Post Fields %s" % (self._post_fields))
            try:
                c.setopt(pycurl.POSTFIELDS, str(self._post_fields))
            except TypeError, t:
                self._logger.warn("Wrong setopt POSTFIELDS value %s" % (self._post_fields))
                raise TypeError(t)

        headers = self.get_context().get_headers() 
        
        self._logger.info(headers)
        if headers:
            self._logger.info("Headers %s" % (headers))
            try:
                c.setopt(pycurl.HTTPHEADER, headers)
            except TypeError, t:
                self._logger.warn("Wrong setopt HTTPHEADER value %s" % (headers))
                raise TypeError(t)
        else:
            self._logger.info("Empty headers")

        bufResponseHeader = cStringIO.StringIO()
        c.setopt(pycurl.HEADERFUNCTION, bufResponseHeader.write)
        return bufResponseHeader
               
    def _prepareHTTP(self, c):
        """
        """
        bufResponseHeader = self._prepareCommonHTTP(c)
        return bufResponseHeader    
    
    def _prepareHTTPS(self, c):
        """
        """
        bufResponseHeader = self._prepareCommonHTTP(c)
        return bufResponseHeader