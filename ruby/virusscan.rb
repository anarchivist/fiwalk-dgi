#!/usr/bin/env ruby

# virusscan.rb: scan a bitstream for viruses; depends on libclamav, clamav gem

require 'rubygems'
require 'clamav'

filename = ARGV[0]
out = {}

clam = ClamAV.instance
clam.loaddb

out['virusScannerVersion'] = clam.version
vscan = clam.scanfile filename

case vscan
when 0
  out['virusFound'] = 'false'
when 2
  out['virusFound'] = 'error'
else
  out['virusFound'] = 'true'
  out['virusSignature'] = vscan
end

out.each do |k, v|
  puts "#{k}: #{v}"
end