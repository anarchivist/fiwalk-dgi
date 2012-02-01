Sample Fiwalk DGI scripts
=========================

These are sample Domex Gateway Interface ("DGI") scripts for Simson
Garfinkel's [fiwalk](http://afflib.org/software/fiwalk), a command-line tool
that processes a forensic disk image. DGI is a plug-in mechanism for fiwalk
that allows an external program to return metadata or other structured
information to fiwalk as key/value pairs. fiwalk outputs in a variety of formats including Digital Forensics XML (DFXML) and ARFF.

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
    *                dgi        python pronom-ident.py

More information can be found in the fiwalk documentation and the paper linked above. However, note that each glob is *only matched once.*

Author
------

* Mark A. Matienzo (mark at matienzo dot org)
