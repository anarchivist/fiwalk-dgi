#!/usr/bin/env python
# encoding: utf-8
"""
virusscan.py - Scan a bitstream for viruses; depends on clamd and pyclamd
"""

import sys
from optparse import OptionParser
from pyclamd import pyclamd
import dateutil.parser

def virusscan(fn, method='socket', socket='/tmp/clamd.socket'):
    out = {}
    if method != 'socket':
        raise NotImplementedError
    else:
        clam = pyclamd.ClamdUnixSocket(filename=socket)    
        vers = clam.version().split('/')
        out['virusScannerVersion'] = vers[0]
        out['virusScannerSignatureVersion'] = vers[1]
        out['virusScannerSignatureDate'] = dateutil.parser.parse(vers[2]).strftime("%Y-%m-%dT%H:%M:%S")
        vscan = clam.scan_file(fn)
        if vscan is None:
            out['virusFound'] = 'false'
        else:
            out['virusFound'] = 'true'
            out['virusSignature'] = vscan[fn][1]
    return out

def main():
    parser = OptionParser()
    parser.add_option('-m', '--method', dest='method',
        default='socket', help='define method of interaction with clamav')
    parser.add_option('-s', '--socket', dest='socket',
        default='/tmp/clamd.socket', help='clamav unix socket to use')
    opts, args = parser.parse_args()

    if len(args) < 1:
        parser.print_help()
        exit(-1)
        
    filename = args[0]
    scan = virusscan(filename, method=opts.method, socket=opts.socket)
    for k, v in scan.items():
        print k + ': ' + v

if __name__ == "__main__":
    sys.exit(main())
