#!/usr/bin/env python
# encoding: utf-8
"""
pronom-ident.py - Identify a bitstream against PRONOM; uses fido
"""

import sys
import getopt
from fido import fido

help_message = 'Identify a bitsream against PRONOM registry using fido'

printnomatch = 'pronomSoftware: fido ' + fido.version + '\npronomMatch: %(info.matchtype)s\n'
printmatch = printnomatch + 'pronomPuid: %(info.puid)s\npronomFormatName: %(info.formatname)s\npronomSignature: %(info.signaturename)s\npronomMimeType: %(info.mimetype)s\n'

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(help_message)
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
        
    filename = args[0]
    
    f = fido.Fido(quiet=True, printnomatch=printnomatch, printmatch=printmatch)
    f.identify_file(filename)

if __name__ == "__main__":
    sys.exit(main())
