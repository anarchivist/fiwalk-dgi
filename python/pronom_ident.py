#!/usr/bin/env python
# encoding: utf-8
"""
pronom-ident.py - Identify a bitstream against PRONOM; uses fido
"""

import os
import sys
from argparse import ArgumentParser
from fido import fido

# TODO: Add something about signature files/versions used

common_string = "pronomSoftware: fido " + fido.version

match_string = common_string + """
pronomMatchType: %(info.matchtype)s
pronomPuid: %(info.puid)s
pronomFormatName: %(info.formatname)s
pronomSignatureName: %(info.signaturename)s
pronomFormatMimeType: %(info.mimetype)s
pronomFormatVersion: %(info.version)s
pronomFormatAlias: %(info.alias)s
pronomTotalMatches: %(info.group_size)s
"""

no_match_string = common_string + """
pronomTotalMatches: 0
pronomMatchType: fail
"""

def main(arglist=None):
    if arglist == None:
        arglist = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument('file', default=[], metavar='FILE', help='File to identify')
    args = parser.parse_args(arglist)
    
    # Note: fido.main() writes to STDOUT. We don't need to capture or
    # print the output it returns. In an earlier version of this script,
    # I subclassed fido.Fido and added custom methods, but therein lies
    # madness.  Below is the recommended way, according to the following:
    # http://wiki.opf-labs.org/x/kYDNAQ

    fido.main(['-q', # Don't print version header
        '-matchprintf', match_string, # Use our custom match string
        '-nomatchprintf', no_match_string, # Use our custom nonmatch string
        args.file])

if __name__ == "__main__":
    sys.exit(main())
