robotframework-pycurllibrary
============================

*PycURLLibrary* is client-side URL transfer test library based on *[PycUrl](http://pycurl.sourceforge.net/)* for Robot Framework.

It supports FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP, SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer resume, http proxy tunneling and more!

[Keyword documentation](http://ivalo.github.io/robotframework-pycurllibrary/).

## Usage

Example:

<table border="1">
  <tr>
    <th>Setting</th>
    <th>Value</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Library</td>
    <td>PycURLLibrary</td>
    <td></td>
  </tr>
</table> 

<table border="1">
  <tr>
    <th>Test Case</th>
    <th>Action</th>
    <th>Argument</th>
    <th>Argument</th>
    <th>Argument</th>
  </tr>
  <tr>
    <td>My Test</td>
    <td>[Documentation]</td>
    <td>Example test</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Verbose</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Insecure Ssl</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Set Url</td>
    <td>http://localhost:53004/soap</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Headers File</td>
    <td>./headers-file.txt</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Client Certificate File</td>
    <td>./client_cert.cer</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Private Key File</td>
    <td>./privkey.pem</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Post Fields File</td>
    <td>./soap-request.xml</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Perform</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Log Response</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Response Status Should Contain</td>
    <td>200</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>${root}=</td>
    <td>Parse Xml</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Should Contain Element</td>
    <td>${root}</td>
    <td>.//{http://ws.poc.jivalo/hello/v1}customer</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>${elem}=</td>
    <td>Find First Element</td>
    <td>${root}</td>
    <td>.//name</td>
 </tr>
  <tr>
    <td></td>
    <td>Element Should Contain</td>
    <td>${elem}</td>
    <td>Hello, world!</td>
    <td></td>
  </tr>
</table> 

## Installation

### Prerequisite

- cURL must be installed
- PycUrl must be installed.
- Python-dev should be installed

**NOTE: PycURL must not be binded with GnuTLS (Unfortunately at least Debian based distribution has wrong SSL library binded with; OpenSSL should be used instead) in order to work properly.**

#### Ubuntu
- sudo apt-get install curl
- sudo apt-get install python-dev

- PycURL build from source; see information below

##### Debian Build OpenSSL PycURL

If connection establishemnt failes with message then GnuTLS is used for SSL connections:

        gnutls_handshake() failed: A TLS fatal alert has been received.

Then OpenSSL must be used for SSH connections. Verify GnuTLS:

        >>> import pycurl
        >>> pycurl.version
        'libcurl/7.22.0 GnuTLS/2.12.14 zlib/1.2.3.4 libidn/1.23 librtmp/2.3'


1. sudo apt-get install build-essential fakeroot dpkg-dev
2. sudo apt-get install libcurl4-openssl-dev
3. mkdir ~/python-pycurl-openssl
4. cd ~/python-pycurl-openssl
5. apt-get source python-pycurl
6. cd pycurl\_7.19.0
7. Edit the debian/control file and replace all instances of "libcurl4-gnutls-dev" to "libcurl4-openssl-dev"
8. Edit the debian/pathes/10\_setup.py.dpatch file and replace HAVE\_CURL\_GNUTLS with HAVE\_CURL\_OPENSSL
9. Edit the debian/changelog file by adding new version
        pycurl (7.19.0-4ubuntu3+openssl) precise; urgency=low

          * Rebuild to use OpenSSL dependency instead GnuTLS.

         -- Markku Saarela <ivalo@iki.fi>  Wed, 18 Sep 2013 09:15:26 +0000
10. dpkg-buildpackage -rfakeroot -b
11. sudo dpkg -i ../python-pycurl\_7.19.0-4ubuntu3+openssl\_amd64.deb

After this procedure output should be following:

        'libcurl/7.22.0 OpenSSL/1.0.1 zlib/1.2.3.4 libidn/1.23 librtmp/2.3'

#### Windows

For cURL and pycURL installation look here:

- cURL downloads: http://curl.haxx.se/download.html.

- pycURL downloads: http://pycurl.sourceforge.net/download/  \(Select OpenSSL version\)

### Installing using pip (recommended)

        pip install robotframework-pycurllibrary

### Installation from source

The source code can be retrieved either as a source distribution or as a clone of the main source repository.

Install it with following command:

        python setup.py install

### Verify installation

        python
        import PycURLLibrary

### Upgrade PycURLLibrary

        pip install robotframework-pycurllibrary --upgrade


