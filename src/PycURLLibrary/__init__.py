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

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))

__version__ = VERSION

__all__ = ['include', 'verbose', 'add_header', 'insecure', 
           'data_file', 'set_url', 'ca_path', 'cert', 'key', 'perform', 'response'
          ]

class PycURLLibrary():
    """PycURLLibrary is a library for functional testing with URL syntax, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, 
    HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. 
    PycURLLibrary supports SSL certificates and more.

    PycURLLibrary is based on PycURL [http://pycurl.sourceforge.net/], 
    PycURL is a Python interface to libcurl [http://curl.haxx.se/libcurl/].
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
        
    def no_buffer(self):
        """Disables the buffering of the output stream.
        
        In normal work situations, curl will use a standard buffered output stream that will have the effect that it will output the data in chunks, 
        not necessarily exactly when the data arrives. Using this option will disable that buffering.

        Note that this is the negated option name documented. You can thus use --buffer to enforce the buffering. 
        """
        
    def insecure(self):
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

    def set_url(self, url):
        """Specify a URL to fetch.
        """
        self._url.get_context().set_url(str(url))
        
    def ca_path(self, cacert):
        """((SSL) Tells curl to use the specified certificate directory to verify the peer. 
        Multiple paths can be provided by separating them with ":" (e.g. "path1:path2:path3"). 
        The certificates must be in PEM format. 
        
        Equivalent for <--capath> argument with curl
        """
        self._url.get_context().set_cacert(cacert)
        
    def cert(self, cert):
        """(SSL) Tells curl to use the specified client certificate file when getting a file with HTTPS, 
        FTPS or another SSL-based protocol. The certificate must be in PEM format

        Equivalent for <--cert> argument with curl
        """
        self._url.get_context().set_cert(cert)
        
    def key(self, key):
        """(SSL/SSH) Private key file name. 
        Allows you to provide your private key in this separate file. 

        Equivalent for <--key> argument with curl
        """
        self._url.get_context().set_key(key)
        
    def perform(self):
        """Perform curl perform.
        """
        self._url.perform()
        
    def response(self):
        """Get response from latest perform result
        """
        return self._url.get_response()

    def response_header(self):
        """Get response header from latest perform result
        """
        return self._url.get_response_header()
