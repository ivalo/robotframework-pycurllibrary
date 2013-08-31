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
        
        if self._verbose:
            c.setopt(pycurl.VERBOSE, True)
        
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
        
        if self._insecure:
            c.setopt(pycurl.SSL_VERIFYPEER, False)
           
        if self.get_context().get_cert() is not None:
            c.setopt(pycurl.SSLCERT, self.get_context().get_cert())
            
        if self.get_context().get_capath() is not None:
            c.setopt(pycurl.CAPATH, self.get_context().get_capath())
            
        if self.get_context().get_key() is not None:
            c.setopt(pycurl.SSLKEY, self.get_context().get_key())
            
        c.setopt(pycurl.URL, self.get_context().get_url())
        bufResponse = cStringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, bufResponse.write)
        self._logger.info("Perform for %s" % (self.get_context().get_url()))
                                                              
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
        self._logger.info(self.get_context().get_response())
        
                
    def _prepareCommonHTTP(self, c):
        """
        """
        if self._post_fields is None:
            self._logger.info("No Post Fields")
        else:
            self._logger.info("Post Fields %s" % (self._post_fields))
            c.setopt(pycurl.POSTFIELDS, str(self._post_fields))

        headers = self.get_context().get_headers() 
        
        self._logger.info(headers)
        if headers:
            c.setopt(pycurl.HTTPHEADER, headers)
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