# coding=utf-8

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_reflected(s, s1):
  return s == s1[::-1]

def is_palindrome(n):
  sn = str(n)
  l = len(sn)
  l2 = int(l / 2)
  if(l % 2 == 0):
    return is_reflected(sn[0:l2], sn[l2:])
  else:
    return is_reflected(sn[0:l2], sn[l2+1:])


def palindrome_products_between(n1, n2):
  palindromes = []
  for i in xrange(n1, n2):
    for j in xrange(i + 1, n2):
      product = i * j
      if (is_palindrome(product)):
        palindromes.append(product)
  return palindromes



# print is_palindrome(9009)
print max(palindrome_products_between(100,1000))