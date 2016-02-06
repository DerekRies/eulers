# coding=utf-8

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


import utils


def amicable(n):
  d1 = sum(utils.divisors(n))
  if sum(utils.divisors(d1)) == n:
    if d1 != n:
      return d1
    else:
      return 0
  else:
    return 0

def main(n):
  pairs = []
  for a in xrange(n):
    b = amicable(a)
    if bool(b) and a < n and b < n:
      # print a, b
      if utils.list_has(pairs, a) or utils.list_has(pairs, b):
        None
      else:
        pairs.append(a)
        pairs.append(b)
  print sum(pairs)



if __name__ == '__main__':
  main(10000)