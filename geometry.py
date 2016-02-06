import math


def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def pythag_3s(max_c):
  a = 2
  running = True
  while running:
    a += 1
    b = a + 1
    while True:
      c_squared = (a**2) + (b**2)
      c = int(math.sqrt(c_squared))
      if c <= max_c:
        # print 'under max at a: %s, b: %s, c: %s' % (a, b, c)
        if is_square(c_squared):
          # print 'triple a: %s, b: %s, c: %s' % (a, b, c)
          yield (a, b, c)
        b += 1
      else:
        # print c
        if b == a + 1:
          # print 'breaking at a: %s, b: %s' % (a, b)
          running = False
        break


def fib_numbers(max_length=0):
  fs1 = 1
  fs2 = 1
  i = 2
  yield fs1
  yield fs2
  while i < max_length or not bool(max_length):
    i += 1
    temp = fs1
    fs1 += fs2
    fs2 = temp
    yield fs1


def triangle_numbers(max_length=0):
  n = 0
  i = 0
  while i < max_length or not bool(max_length):
    i += 1
    n += i
    yield n

def pent_numbers(max_length=0):
  n = 0
  while n < max_length or not bool(max_length):
    n += 1
    yield int((n * ((3 * n) - 1)) / 2)

def hex_numbers(max_length=0):
  n = 0
  while n < max_length or not bool(max_length):
    n += 1
    yield int(((2 * n) - 1) * n)