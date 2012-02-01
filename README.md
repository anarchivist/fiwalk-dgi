Sample Fiwalk DGI scripts
=========================

These are sample Domex Gateway Interface ("DGI") scripts for Simson
Garfinkel's [fiwalk](http://afflib.org/software/fiwalk), a command-line tool
that processes a forensic disk image. DGI is a plug-in mechanism for fiwalk
that allows an external program to return metadata or other structured
information to fiwalk as key/value pairs.

DGI response format
-------------------

fiwalk (as of version 0.6 expects the following format)

    Key-one: Value
    keyTwo: Second value
    YetAnotherKey: And another value still


Author
------

* Mark A. Matienzo (mark at matienzo dot org)
