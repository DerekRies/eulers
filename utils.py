import collections
import functools
import operator
from bisect import bisect_left


class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).

   Memoize decorator from https://wiki.python.org/moin/PythonDecoratorLibrary
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)


def n_divisors(n):
  if n == 1:
    return 1
  upper_bound = n
  i = 2
  num_of_divisors = 2
  while i < upper_bound:
    if (n % i == 0 and i != n):
      upper_bound = min(upper_bound, int(n / i))
      num_of_divisors += 2
    i += 1
  return num_of_divisors

def divisors(n):
  ds = [1]
  if n == 1:
    return ds
  upper_bound = n
  i = 2
  while i < upper_bound:
    if (n % i == 0 and i != n):
      d2 = int(n/i)
      ds.append(i)
      ds.append(d2)
      upper_bound = min(upper_bound, d2)
    i += 1
  return ds


def product(iterable):
    return reduce(operator.mul, iterable, 1)


def list_has(a, x):
  i = bisect_left(a, x)
  if i != len(a) and a[i] == x:
      return True
  return False