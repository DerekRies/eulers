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


def triangle_numbers():
  n = 0
  i = 0
  while True:
    i += 1
    n += i
    yield n