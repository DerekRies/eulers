# coding=utf-8

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def spiral(size):
  rsize = 1
  last = 1
  yield [last]
  while rsize < size:
    rsize += 2
    nums = 2 * rsize
    nums += 2 * (rsize - 2)
    ring = range(last + 1, last + nums + 1)
    last = ring[-1]
    diagonals = [last]
    for i in xrange(1,4):
      pos = (rsize - 1) * i * -1
      diagonals.append(ring[pos - 1])
    yield diagonals




total = 0
for ring in spiral(1001):
  total += sum(ring)
print total