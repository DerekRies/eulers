# coding=utf-8
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""
from utils import memoized

@memoized
def n_paths(m, n):
  if m == 1 or n == 1:
    return 1
  return n_paths(m-1, n) + n_paths(m, n-1)


def main(m, n):
  print n_paths(m+1, n+1)

if __name__ == '__main__':
  main(20,20)