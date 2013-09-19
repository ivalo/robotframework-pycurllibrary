# -*- coding: UTF-8 -*- 
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
import os
from robot.api import logger

from base64 import b64encode
from functools import wraps

import pycurl
from url import Url
import xml.etree.ElementTree as ET

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))

__version__ = VERSION

__all__ = ['include', 'verbose', 'insecure', 'add_header', 'headers_file', 
           'post_fields', 'post_fields_file', 'request_method', 'data_file', 
           'set_url', 'ca_path', 'cert', 'key', 'perform', 'response', 
           'response_header'
          ]

class PycURLLibrary():
    """PycURLLibrary is a library for functional testing with URL syntax, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, 
    HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. 
    PycURLLibrary supports SSL certificates and more.

    PycURLLibrary is based on PycURL [http://pycurl.sourceforge.net/], 
    PycURL is a Python interface to libcurl [http://curl.haxx.se/libcurl/].
    
    xml.etree.ElementTree [http://docs.python.org/2/library/xml.etree.elementtree.html] is used for XML operations.

    Supported XPath syntax (from Python v2.7.5 documentation):

    | Syntax | Meaning |
    | tag    | Selects all child elements with the given tag. For example, spam selects all child elements named spam, spam/egg selects all grandchildren named egg in all children named spam. |
    | *      | Selects all child elements. For example, */egg selects all grandchildren named egg. |
    | .      | Selects the current node. This is mostly useful at the beginning of the path, to indicate that it’s a relative path. |
    | //     | Selects all subelements, on all levels beneath the current element. For example, .//egg selects all egg elements in the entire tree. |
    | ..     | Selects the parent element. |
    | [@attrib] | Selects all elements that have the given attribute. |
    | [@attrib='value'] | Selects all elements for which the given attribute has the given value. The value cannot contain quotes. |
    | [tag]  | Selects all elements that have a child named tag. Only immediate children are supported. |
    | [position] | Selects all elements that are located at the given position. The position can be either an integer (1 is the first position), the expression last() (for the last position), or a position relative to the last position (e.g. last()-1). |
    """
    
    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = "TEST CASE"
    ROBOT_LIBRARY_DOC_FORMAT = "ROBOT"

    def __init__(self):
        self._logger = logger
        self._url = Url()
        
    def verbose(self):
        """Makes the fetching more verbose/talkative.
        
        Mostly useful for debugging. A line starting with '>' means "header data" sent by curl, 
        '<' means "header data" received by curl that is hidden in normal cases, and a line starting with '*' means additional info provided by curl.
        
        Note that if you only want HTTP headers in the output, -i, --include might be the option you're looking for.
        
        If you think this option still doesn't give you enough details, consider using --trace or --trace-ascii instead.
        
        This option overrides previous uses of --trace-ascii or --trace.         
        """
        self._url.set_verbose(True)
        
#    def no_buffer(self):
#        """Disables the buffering of the output stream.
#        
#        In normal work situations, curl will use a standard buffered output stream that will have the effect that it will output the data in chunks, 
#        not necessarily exactly when the data arrives. Using this option will disable that buffering.
#        Note that this is the negated option name documented. You can thus use --buffer to enforce the buffering. 
#        """
        
    def server_connection_establishment_timeout(self, timeout):
        """The maximum time in seconds that you allow the connection to the server to take (long value).
        This only limits the connection phase, once it has connected, this option is of no more use. 
        Set to zero to switch to the default built-in connection timeout - 300 seconds.
        """
        self._url.get_context().set_server_connection_establishment_timeout(long(str(timeout)))
        
    def insecure_ssl(self):
        """(SSL) This option explicitly allows curl to perform "insecure" SSL connections and transfers.
        
        All SSL connections are attempted to be made secure by using the CA certificate bundle installed by default. 
        This makes all connections considered "insecure" fail unless -k, --insecure is used. 
        """
        self._url.set_insecure(True)
        
    def request_method(self, requestMethod):
        """ Set's the request method. Default's to GET if Post Fields keyword is used POST is used
        | Method |
        | GET |
        | POST |
        | PUT |
        | DELETE |
        """
        self._url.get_context().set_request_method(requestMethod)
        
    def add_header(self, header):
        """(HTTP) Extra header to use when getting a web page.
        
        Each *Add Header* keyword is equivalent for one <-H, --header> argument with curl
        
        Examples:
        | Add Header | Content-Type: text/xml; charset=UTF-8 |
        | Add Header | Frame.Version:3.0 |
        """
        self._logger.info('Header %s' % header)
        self._url.get_context().add_header(str(header))
        
    def headers_file(self, headerFile):
        """(HTTP) Extra headers to use when getting a web page.
        
        *headerFile* contains all headers.
        
        One line is one header. Note do not make line feed after last header.

        | Headers File | /data/headers.txt |
        
        Example of content of *headerFile*:
        | Version: 2 |
        | Content-Type: text/xml; charset=UTF-8 |        
        """
        headers = [line.rstrip() for line in open(headerFile, 'r')] 
        self._logger.info('Headers %s' % headers)
        self._url.get_context().set_headers(headers)
        
        
    def post_fields(self, postFields):
        """(HTTP) Sends the specified data in a POST request to the HTTP server, 
        in the same way that a browser does when a user has filled in an HTML form and presses the submit button. 
        This will cause curl to pass the data to the server using the content-type application/x-www-form-urlencoded.

        Equivalent for <--data> argument 
        
        Example:
        | Post Fields | pizza=Quattro+Stagioni&extra=cheese |
        """
        self._url.set_post_fields(postFields)
        if postFields is not None:
            self._url.get_context().set_request_method('POST')

    def post_fields_file(self, postFieldsFile):
        """(HTTP) Sends the specified data in a POST request to the HTTP server, 
        in the same way that a browser does when a user has filled in an HTML form and presses the submit button. 
        This will cause curl to pass the data to the server using the content-type application/x-www-form-urlencoded.

        Equivalent for <--data> @argument 
        
        Example:
        | Post Fields File | /data/message.txt |
        """
        f = open(postFieldsFile, 'r')
        postFields = f.read()
        f.close()
        self._url.set_post_fields(postFields)
        self._url.get_context().set_request_method('POST')

    def set_url(self, url):
        """Specify a URL to fetch.
        """
        self._url.get_context().set_url(str(url))
        
    def ca_path(self, cacertDirectory):
        """((SSL) Tells curl to use the specified certificate directory to verify the peer. 
        Multiple paths can be provided by separating them with ":" (e.g. "path1:path2:path3"). 
        The certificates must be in PEM format. 
        
        Equivalent for <--capath> argument with curl
        """
        self._url.get_context().set_capath(str(cacertDirectory))
        
    def client_certificate_file(self, cert):
        """(SSL) Tells curl to use the specified client certificate file when getting a file with HTTPS, 
        FTPS or another SSL-based protocol. The certificate must be in PEM format

        Equivalent for <--cert> argument with curl
        """
        self._url.get_context().set_client_certificate_file(str(cert))
        
    def private_key_file(self, key):
        """(SSL/SSH) Private key file name. 
        Allows you to provide your private key in this separate file. 

        Equivalent for <--key> argument with curl
        """
        self._url.get_context().set_private_key_file(str(key))
        
    def perform(self):
        """Perform curl perform.
        """
        self._url.perform()
        
    def response(self):
        """Get response from latest perform result
        """
        return self._url.get_context().get_response()

    def response_headers(self):
        """Get response headers from latest perform result for protocols having headers preceding the data (like HTTP)
        """
        return self._url.get_context().get_response_headers()

    def parse_xml(self):
        """Parses an XML section of the response. Returns an root Element instance.
        """
        return ET.fromstring(self._url.get_context().get_response())
    
    def find_elements(self, element, xpath):
        """Returns a list containing all matching elements in document order
        
        XPath Namespace example: './/{http://ws.poc.jivalo/hello/v1}customer'
        """
        assert element is not None, \
            'Element is Null.' 
        xp = str(xpath)
        return element.findall(xp)
    
    def find_first_element(self, element, xpath):
        """Finds the first subelement matching match. match may be a tag name or path. Returns an element instance or None.
        
        XPath Namespace example: './/{http://ws.poc.jivalo/hello/v1}customer'
        """
        assert element is not None, \
            'Element is Null.' 
        xp = str(xpath)
        return element.find(xp)
    
    def should_contain_element(self, element, xpath):
        """Fails if the 'element' does not contain 'xpath' element       
        """
        elements = self.find_elements(element, xpath)
        assert elements, \
            'Element "%s" contains not XPaht element "%s".'  % (
            element.tag, xpath)
            
    def element_should_contain(self, element, text):
        """Fails if the 'element' text value does not contain 'text'      
        """
        assert text == element.text, \
            'Element "%s" does not contains text "%s".'  % (
            element.tag, text)
            
    def http_response_status(self):
        """Get response status from latest HTTP response status line
        """
        return self._url.get_context().get_response_status()

    def log_response(self, log_level='INFO'):
        """
        Logs the response of the URL transfer.

        Specify `log_level` (default: "INFO") to set the log level.
        """        
        if self.response():
            self._logger.write("Response body:", log_level)
            self._logger.write(self.response(), log_level)
        else:
            self._logger.debug("No response received", log_level)

    def log_response_headers(self, log_level='INFO'):
        """
        Logs the response headers for protocols having headers preceding the data (like HTTP), line by line.

        Specify `log_level` (default: "INFO") to set the log level.
        """        
        if self.response_headers():
            self._logger.write("HTTP Response headers:", log_level)
            for header in self.response_headers():
                self._logger.write(header, log_level)
        else:
            self._logger.debug("No HTTP response headers received", log_level)
        

    def log_http_response_status(self, log_level='INFO'):
        """
        Logs the HTTP response header status line.

        Specify `log_level` (default: "INFO") to set the log level.
        """        
        if self.http_response_status():
            self._logger.write("HTTP Response status:", log_level)
            self._logger.write(self.http_response_status(), log_level)
        else:
            self._logger.debug("No HTTP response status received", log_level)
        
    def log_version(self, log_level='INFO'):
        """
        Logs the PycURLLibrary Version.

        Specify `log_level` (default: "INFO") to set the log level.
        """
        self._logger.write("PycURLLibrary version %s" % (self.ROBOT_LIBRARY_VERSION), log_level)
