#!/usr/bin/env python
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
Created on 22 Aug 2013

@author: Markku Saarela
'''

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
import os
import ssl


class TestRequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200, "No payment required")
        self.send_header('x-powered-by', 'PHP')
        self.send_header('x-request-user-agent', self.headers.get(
            'user-agent', '(unknown)'))
        self.end_headers()

    def do_DELETE(self):
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write(self.requestline)
        self.finish()

    def do_PATCH(self):
        self.send_response(200, "Patch request ok")
        self.end_headers()
        self.wfile.write("Got a patch request")
        self.finish()

    def do_GET(self):
        if self.path == '/rest':
            print self.headers
            #print self.headers['Content-Type']
            #print self.headers['Version']
            self.send_response(200, "OK")
            #self.send_header('Location', '/200')
            self.end_headers()            
            self.wfile.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><customer id="1"><name>Hello, world!</name></customer>')
            self.finish()
        else:
            self.send_error(500)

    def do_POST(self, *args, **kwargs):
        if self.path == '/soap':
            data = self.rfile.read(int(self.headers['Content-Length']))
            print data
            responseFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'soap-response.xml'))
            print responseFile
            f = open(responseFile, 'r')
            responseData = f.read()
            f.close()

            self.rfile.close()
            self.send_response(200, "OK")
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(responseData)
            self.finish()
        elif self.path == '/kill':
            global server
            self.send_response(201, "Killing myself")
            server.socket.close()
            sys.exit(0)
        else:
            self.send_error(500)

    do_PUT = do_POST

PORT = int(sys.argv[1])
try:

    server = HTTPServer(('localhost', PORT), TestRequestHandler)
    scheme = 'http'
        
    print 'Starting server on %s://localhost:%d/' % (scheme, PORT)
    
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    