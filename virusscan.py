#!/usr/bin/env python
# encoding: utf-8
"""
virusscan.py - Scan a bitstream for viruses; depends on clamd and pyclamd
"""

import sys
import getopt
from pyclamd import pyclamd

help_message = '''Scan a bitstream for viruses using clamav'''


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hs", ["help", "socket="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-s", "--socket"):
                socket = value
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
        
    filename = args[0]
    out = {}
    
    clam = pyclamd.ClamdUnixSocket(filename=socket)    
    out['virusScannerVersion'] = clam.version()
    vscan = clam.scan_file(filename)
    if vscan is None:
        out['virusFound'] = 'false'
    else:
        out['virusFound'] = 'true'
        out['virusSignature'] = vscan[filename][1]
    
    for k, v in out.items():
        print k + ': ' + v

if __name__ == "__main__":
    sys.exit(main())
