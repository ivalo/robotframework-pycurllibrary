robotframework-pycurllibrary
============================

*PycURLLibrary* is client-side URL transfer test library based on *[PycUrl](http://pycurl.sourceforge.net/)* for Robot Framework.

It supports FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP, SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer resume, http proxy tunneling and more!

[Keyword documentation](http://ivalo.github.io/robotframework-pycurllibrary/).

## Installation

### Installing using pip (recommended)

        pip install robotframework-pycurllibrary

### Installation from source

The source code can be retrieved either as a source distribution or as a clone of the main source repository.

Install it with following command:

        python setup.py install

### Verify installation

        python
        import PycURLLibrary

## Distribution

        python setup.py register
        python setup.py sdist upload

