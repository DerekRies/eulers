"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def is_prime(n):
  if(n%2==0):
    return False
  else:
    for i in xrange(2, int(math.sqrt(n))):
      if (n%i==0):
        return False
    return True


def prime_factors(n):
  # ex: 13195 -> [5,7,13,29]
  primes = []
  sqn = int(math.ceil(math.sqrt(n)))
  for i in xrange(1, sqn+1, 2):
    if (n % i == 0):
      if (is_prime(i)):
        primes.append(i)
  return primes



print max(prime_factors(600851475143))