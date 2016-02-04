"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def least_evenly_divisible_between(n, n2):
  i = n2**2
  while(True):
    for j in xrange(n, n2+1):
      if (i%j==0):
        if(j == n2):
          return i
      else:
        break
    i+=n2

print least_evenly_divisible_between(1,20)