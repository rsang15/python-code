#!/usr/bin/env python

import sys
import math
import time

# Constants
MAX_INPUT = 5000000000

def print_usage():
    print( """
    This program accepts one argument...
    """)

primes = [2, 3]

def make_primes(n):
    # Extend list of primes to extend beyond n unless it already is     

def is_prime(n):
    # Return True if n is prime, otherwise false
    def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             

def next_prime(n):
    # Return the next prime greater than n
    n = input('Find the next prime number greater great than n: ')
    print find_next_prime(n+1)

    def find_next_prime(n):
        return find_prime_in_range(n, 2*n)

    def find_prime_in_range(a, b):
        for p in range(a, b):
            for i in range(2, p):
                if p % i == 0:
                    break
                else:
                    return p
                return None

prime_squared = [4, 9]
prime_cubed = [8, 27]
prime_quartic = [16, 81]

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
