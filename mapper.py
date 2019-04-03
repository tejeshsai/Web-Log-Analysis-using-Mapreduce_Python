#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    #Splitting at white spaces
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        
        print '%s\t%s' % (word, 1)
        break
