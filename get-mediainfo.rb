#!/usr/bin/env ruby

# get-mediainfo.rb: use MediaInfo to extract metadata from AV files
# requires MediaInfo CLI - http://mediainfo.sourceforge.net/
# requires mediainfo gem - https://github.com/greatseth/mediainfo/ 

require 'rubygems'
require 'mediainfo'

filename = ARGV[0]
info = Mediainfo.new filename

puts "mediainfoStreamCount: #{info.streams.count}"

# make an index/value hash of the array of streams returned by Mediainfo
streams = Hash[ *info.streams.collect {|v| [info.streams.index(v), v]}.flatten ]

# probably overkill, but gives us everything that mediainfo would return.
streams.each do |stream_id, stream|
  stream_type = stream.instance_variable_get(:@stream_type)
  puts "mediainfoStream#{stream_id}_type: #{stream_type}"
  stream.parsed_response[stream_type].each do |element, data|
    puts "mediainfoStream#{stream_id}_#{element}: #{data}"
  end
end