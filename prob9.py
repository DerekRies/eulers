# coding=utf-8

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import geometry
import utils



def prob9(n):
  for triple in geometry.pythag_3s(n):
    # print triple
    if sum(triple) == n:
      return utils.product(triple)


print prob9(1000)