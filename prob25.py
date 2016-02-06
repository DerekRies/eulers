# coding=utf-8

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import geometry
import math


def n_digits(n):
  # Basically "count the zeros"
  if n < 10 and n > 0:
    return 1
  return int(math.ceil(math.log(n+1, 10)))


def main():
  i = 1
  for fib in geometry.fib_numbers():
    if n_digits(fib) >= 1000:
      print i
      break
    i += 1 


if __name__ == '__main__':
  main()