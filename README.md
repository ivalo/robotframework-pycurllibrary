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

#### Ubuntu
- sudo apt-get install curl
- sudo apt-get install python-dev

- sudo apt-get install python-pycurl or sudo pip env ARCHFLAGS="-arch x86_64" pip install pycurl

#### Windows

For cURL and pycURL installation look here:

- cURL downloads: http://curl.haxx.se/download.html.

- pycURL downloads: http://pycurl.sourceforge.net/download/ or try this **pip install pycurl**

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

