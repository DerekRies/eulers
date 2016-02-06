# coding=utf-8

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import utils
import pickle
import bisect

def is_abundant(n):
  return n < sum(utils.divisors(n))


def abundant_numbers(max_length=0):
  i = 12
  yield i
  n = 1
  while n < max_length or not bool(max_length):
    i += 1
    if is_abundant(i):
      yield i
      n += 1


def make_abundants():
  abundants = []
  try:
    with open('abundants.txt') as f:
      print 'reusing file'
      abundants = pickle.load(f)
  except:
    print 'creating abundant numbers'
    for n in abundant_numbers():
      if n > 28123:
        break
      abundants.append(n)
    with open('abundants.txt', 'w') as f:
      pickle.dump(abundants, f)
  return abundants


def make_abundant_sums(abundants):
  print 'summing abundants'
  sums = []
  try:
    with open('abundantsums.txt') as f:
      print 'reusing file'
      sums = pickle.load(f)
  except:
    print 'creating abundant sums'
    l = len(abundants)
    for i in xrange(l):
      if i%100 == 0:
        print i/100
      for j in xrange(i, l):
        s = abundants[i] + abundants[j]
        if s <= 28123:
          sums.append(s)
        else:
          break
    sums.sort()
    sums = set(sums)
    print 'finished sorting'
    with open('abundantsums.txt', 'w') as f:
      pickle.dump(sums, f)
    print 'finished summing'
  return sums


def main():
  total = 0
  abundants = make_abundants()
  sums = make_abundant_sums(abundants)
  sums = list(sums)
  sums.sort()
  # print len(sums)
  # sums.sort()
  # print 'sorted sums'
  for x in xrange(0, 28123):
    if not utils.list_has(sums, x):
      # print x
      total += x
  # for x in xrange(1, 28124):
  #   for a in abundants:
  #     if a < x:
  #       x2 = x - a
  #       if utils.list_has(abundants, x2):
  #         break
  #     else:
  #       total += x
  #       break
  print total



if __name__ == '__main__':
  main()