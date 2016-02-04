# coding=utf-8
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

1456
"""

import primeutils
import math


def rotate(s):
  return s[1:] + s[0]

def rotations(n):
  str_n = str(n)
  rs = []
  for i in xrange(len(str_n)):
    str_n = rotate(str_n)
    rs.append(str_n)
  return rs

count = 0
for n in primeutils.primes_below(1000000):
  prime_rotations = [primeutils.is_prime(int(j)) for j in rotations(n)]
  if all(prime_rotations):
    count += 1

print count

# print rotate('197')
# print rotate(rotate('197'))

# print rotations(197)