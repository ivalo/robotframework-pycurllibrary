robotframework-pycurllibrary
============================

*PycURLLibrary* is client-side URL transfer test library based on *[PycUrl](http://pycurl.sourceforge.net/)* for Robot Framework.

It supports FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP, SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer resume, http proxy tunneling and more!

[Keyword documentation](http://ivalo.github.io/robotframework-pycurllibrary/).

## Installation

### Prerequisite

- cURL must be installed
- Python-dev should be instaled
- If PycUrl installation failed during *PycURLLibrary* installation, install it separately.

**NOTE: PycURL must be linked with OpenSSL not GnuTLS (Unfortunately at least Debian based distribution has wrong SSL library linked with) in order to work properly.**

#### Ubuntu
- sudo apt-get install curl
- sudo apt-get install python-dev

- PycURL build from source; see information below

##### Debian Build OpenSSH PycURL

If connection establishemnt failes with message then GnuTLS is used for SSH connections:

        gnutls_handshake() failed: A TLS fatal alert has been received.

Then OpenSSH must be used for SSH connections. Verify GnuTLS:

        >>> import pycurl
        >>> pycurl.version
        'libcurl/7.22.0 GnuTLS/2.12.14 zlib/1.2.3.4 libidn/1.23 librtmp/2.3'


1. sudo apt-get install build-essential fakeroot dpkg-dev
2. mkdir ~/python-pycurl-openssl
3. cd ~/python-pycurl-openssl
4. sudo apt-get source python-pycurl
5. sudo apt-get install libcurl4-openssl-dev
6. sudo dpkg-source -x pycurl\_7.19.0-4ubuntu3.dsc \(pycurl\_7* starting file can be other name\)
7. cd pycurl\_7.19.0
8. Edit the debian/control file and replace all instances of "libcurl4-gnutls-dev" to "libcurl4-openssl-dev"
9. sudo dpkg-buildpackage -rfakeroot -b
10. sudo dpkg -i ../python-pycurl\_7.19.0-4ubuntu3\_amd64.deb

After this procedure output should be following:

        'libcurl/7.22.0 OpenSSL/1.0.1 zlib/1.2.3.4 libidn/1.23 librtmp/2.3'

#### Windows

For cURL and pycURL installation look here:

- cURL downloads: http://curl.haxx.se/download.html.

- pycURL downloads: http://pycurl.sourceforge.net/download/  \(Select OpenSSH version\)

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

## Distribution

        python setup.py register
        python setup.py sdist upload

## Generate Keyword document

        python -m robot.libdoc src/PycURLLibrary PycURLLibrary.html


