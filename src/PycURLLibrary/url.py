'''
Created on 21 Jul 2013

@author: Markku Saarela
'''
from robot.api import logger
from ctx import Ctx
import pycurl
import cStringIO

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
        self._data = None
        self._verbose = False
        self._include = False
        self._no_buffer = False
        self._insecure = False
        
    def get_data(self):
        return self._data
    
    def set_data(self, data):
        self._data = data
        
    def get_verbose(self):
        return self._verbose
    
    def set_verbose(self, verbose):
        self._verbose = verbose
        
    def get_include(self):
        return self._include
    
    def set_include(self, include):
        self._include = include
        
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

    def get_response(self):
        #if not self.get_context().get_response():
        #    raise Exception(
        #        'No request available, use Perform to create one.')
        return self.get_context().get_response()

        
    def perform(self):
        """
        Issues a URL perform.
        
        `url` is the URL relative to t
        """
        self.get_context().set_response(None)
        c = pycurl.Curl()
        
        if self._data is None:
            self._logger.warn("Data is missing")
            return
        
        if self._verbose:
            c.setopt(pycurl.VERBOSE, True)
        if self._include:
            c.setopt(pycurl.HEADER, True)
        #if self._no_buffer:
        #    c.setopt(pycurl.HEADER, True)
        
        if self._insecure:
            c.setopt(pycurl.SSL_VERIFYPEER, False)
           
        headers = self.get_context().get_headers() 
        if headers:
            c.setopt(pycurl.HTTPHEADER, headers)
        else:
            print 'Empty headers'

        if self.get_context().get_cert() is not None:
            c.setopt(pycurl.SSLCERT, self.get_context().get_cert())
            
        if self.get_context().get_capath() is not None:
            c.setopt(pycurl.CAPATH, self.get_context().get_capath())
            
        if self.get_context().get_key() is not None:
            c.setopt(pycurl.SSLKEY, self.get_context().get_key())
            
        f = open(self._data) 
        c.setopt(pycurl.READDATA, f)
        c.setopt(pycurl.URL, self.get_context().get_url())
        buf = cStringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        logger.info("Performing Perform on %s" % (self.get_context().get_url()))
                                                              
        c.perform()
        
        f.close()
 
        self.get_context().set_response(buf.getvalue())
        buf.close()
                