Fiwalk DGI scripts
==================

These are Domex Gateway Interface ("DGI") scripts for Simson Garfinkel's
[fiwalk](http://afflib.org/software/fiwalk), a command-line tool
that processes a forensic disk image. DGI is a plug-in mechanism for fiwalk
that allows an external program to return metadata or other structured
information to fiwalk as key/value pairs. fiwalk outputs in a variety of
formats including Digital Forensics XML (DFXML) and ARFF.

More information on fiwalk and DFXML can be found in the link above and in Garfinkel 2012 ([10.1016/j.diin.2011.11.002](http://dx.doi.org/10.1016/j.diin.2011.11.002); [preprint available](http://simson.net/ref/2011/dfxml.pdf)).

DGI key-value format
--------------------

fiwalk (as of version 0.6 expects the following format)

    Key-one: Value
    keyTwo: Second value
    YetAnotherKey: And another value still

Calling DGI scripts
-------------------

DGI scripts for fiwalk are called from a `ficonfig`-formatted configuration
file. `ficonfig` uses the following format

    # globpattern    channel    args
    *                dgi        python pronom_ident.py

More information can be found in the fiwalk documentation and the paper linked above. However, note that each glob is *only matched once.*

Included Scripts
----------------

* Python
    * pronom\_ident.py: Uses FIDO for format identification against PRONOM 
    * virusscan.py: Uses ClamAV's clamd and pyclamd for virus/malware scanning
    * accession.py: calls pronom\_ident.py and virusscan.py
* Ruby
    * get-mediainfo.rb: Uses MediaInfo for AV technical metadata extraction
    * virusscan.rb: Uses ClamAV and libclamav gem for virus/malware scanning (slow; proof of concept)

Updating FIDO
-------------

The Python scripts include [FIDO](https://github.com/openplanets/fido) for
file format identification, which has been brought into the source tree
using Git's [subtree merging](http://www.kernel.org/pub/software/scm/git/docs/v1.7.10/howto/using-merge-subtree.html) technique. 

To update FIDO when a new version is released, ensure that you have the
FIDO repository set up as a remote:

    $ git remote add -f fido git://github.com/openplanets/fido

Then pull in the changes accordingly:

    $ git pull -s subtree fido master

Author
------

* Mark A. Matienzo (mark at matienzo dot org)
* Contributors/authors of existing modules is included in source or licenses.
