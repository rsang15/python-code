#!/usr/bin/env python

import sys
import math
import time

# Constants
MAX_INPUT = 4000000

def print_usage():
    print """
    This program accepts three arguments...
    """

def main():
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(2)
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    n = int(sys.argv[3])
    if p < 1:
        print "The first argument must be greater than or equal to 1"
        sys.exit(2)
    if p > q or p > n:
        print "The first argument must be less than the other two"
        sys.exit(2)
    if q > n:
        print "The second argument must be less than the third"
        sys.exit(2)
    if n > MAX_INPUT:
        print "The third argument must be less than", MAX_INPUT
        sys.exit(2)
    start = time.time()
    n_p = math.floor(n / p)
    if n % p == 0:
        n_p -= 1
    p_sum = p * n_p * (n_p + 1) / 2
    if q % p == 0:
        ans = p_sum
    else:
        n_q = math.floor(n / q)
        if n % q == 0:
            n_q -= 1
        q_sum = q * n_q * (n_q + 1) /2
        n_pq = math.floor(n /(p * q))
        if n % (p * q) == 0:
            n_pq -= 1
        pq_sum = p * q * n_pq * (n_pq + 1) / 2
        ans = p_sum + q_sum - pq_sum
    print int(ans)
    end = time.time()
    print "Time spent = {} seconds".format(end - start)

if __name__ == '__main__':
    main()
