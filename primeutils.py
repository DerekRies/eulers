"""
A collection of prime-number related functions
"""

import math
import itertools as it


def nth(iterable, n, default=None):
    from itertools import islice
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

def primes(n):
  e = erat3()
  for i in xrange(n):
    yield e.next()


def nth_prime(n):
  p = 2
  for prime in primes(n):
    p = prime
  return p


def primes_below(n):
  e = erat3()
  for prime in e:
    if prime < n:
      yield prime
    else:
      break


def is_prime(n):
  if(n%2==0):
    return False
  else:
    for i in xrange(2, int(math.sqrt(n))):
      if (n%i==0):
        return False
    return True