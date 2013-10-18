#!/usr/bin/env python
# encoding: utf-8
"""
accession.py
"""

import sys
from argparse import ArgumentParser
from pronom_ident import main as pronom_ident
from virusscan import main as virusscan

def main(arglist=None):
    if arglist == None:
        arglist = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument('file', default=[], metavar='FILE', help='File to identify')
    parser.add_argument('-m', '--method', dest='method',
        default='socket', help='define method of interaction with clamav')
    parser.add_argument('-s', '--socket', dest='socket',
        default='/tmp/clamd.socket', help='clamav unix socket to use')
    args = parser.parse_args(arglist)
    virusscan(arglist)
    pronom_ident(arglist)

if __name__ == "__main__":
    sys.exit(main())
