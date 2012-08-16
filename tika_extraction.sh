#!/bin/sh
#
# tika_extraction.sh 

# extract metadata from files using Apache Tika. presumes Tika server
# is running on localhost on port 9998, e.g.: 
# $ java -jar tika-app-1.2.jar -m -s 9998

nc localhost 9998 < $1