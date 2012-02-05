#!/usr/bin/env python
# encoding: utf-8
"""
accession.py
"""

import sys
from optparse import OptionParser
from pronom_ident import pronom_ident
from virusscan import virusscan

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
    out = dict(pronom_ident(filename).items() + virusscan(filename).items())
    for k, v in out.items():
        if v is not None:
            print k + ': ' + str(v)

if __name__ == "__main__":
    sys.exit(main())
