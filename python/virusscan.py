#!/usr/bin/env python
# encoding: utf-8
"""
virusscan.py - Scan a bitstream for viruses; depends on clamd and pyclamd
"""

import sys
from argparse import ArgumentParser
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

def main(arglist=None):
    if arglist == None:
        arglist = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument('file', default=[], metavar='FILE', help='File to identify')
    parser.add_argument('-m', '--method', default='socket', action='store_true', help='define method of interaction with clamav')
    parser.add_argument('-s', '--socket', default='/tmp/clamd.socket', action='store_true', help='clamav unix socket to use')
    args = parser.parse_args(arglist)

    scan = virusscan(args.file, method=args.method, socket=args.socket)
    for k, v in scan.items():
        sys.stdout.write("%(k)s: %(v)s\n" % {'k': k, 'v': v})

if __name__ == "__main__":
    sys.exit(main())
