"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

import primeutils

print sum(n for n in primeutils.primes_below(2000000))