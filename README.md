Fiwalk DGI scripts
==================

These are Domex Gateway Interface ("DGI") scripts for [fiwalk](https://github.com/sleuthkit/sleuthkit/tree/master/tools/fiwalk),
a command-line tool that uses [The Sleuth Kit](http://sleuthkit.org/) to
extract metadata from a forensic disk image. DGI is a plug-in mechanism for
fiwalk that allows an external program to return metadata or other structured
information to fiwalk as key/value pairs. fiwalk outputs in a variety of
formats including Digital Forensics XML (DFXML) and ARFF.

More information on fiwalk and DFXML can be found in the link above and in Garfinkel 2012 ([doi:10.1016/j.diin.2011.11.002](http://dx.doi.org/10.1016/j.diin.2011.11.002); [preprint available](http://simson.net/ref/2011/dfxml.pdf)).

DGI key-value format
--------------------

fiwalk (as of version 0.6) expects the following format:

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

The dependencies for the Python scripts can be installed with the following commands:

    $ cd python ; pip install -r requirements.txt

Author
------

* Mark A. Matienzo (mark at matienzo dot org)
* Contributors/authors of included code listed in source or licenses where
applicable.

License
-------

Apache 2.0

Feel free to contact me if for some reason this will not work for your use.