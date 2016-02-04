import operator

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

def product(iterable):
    return reduce(operator.mul, iterable, 1)