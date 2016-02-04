# coding=utf-8

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def diff(n):
  sum_of_sqs = sum(n**2 for n in xrange(1,n+1))
  sq_of_sum = sum(n for n in xrange(1,n+1))**2
  return sq_of_sum - sum_of_sqs

print diff(100)