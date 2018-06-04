#!/usr/bin/env python

import sys
import math
import time

# Constants
MAX_INPUT = 40755

def print_usage():
    print """
    This program accepts one argument...
    """
# THe following two equations came from wikipedia

def is_hex(h):
    n1 = (math.sqrt(8* h + 1 ) + 1) / 4
    return n1.is_integer()

def is_pentagonal(p):
    n2 = (math.sqrt(24* p + 1 ) + 1) / 6
    return n2.is_integer()

def main():
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(2)
    n = int(sys.argv[1])
    if n < 1:
        print "The argument must be greater than or equal to 1"
    if n > MAX_INPUT:
        print "The argument must be less than", MAX_INPUT
        sys.exit(2)
    
    start = time.time()
    if n < 40755:
        print 40755
    else:
        found = False
        i = n + 1
        while found is False:
            i += 1
            if is_hex(i) and is_pentagonal(i):
                found = True
        print i
    end = time.time()
    print "Time spent = {} seconds".format(end - start)

if __name__ == '__main__':
    main()