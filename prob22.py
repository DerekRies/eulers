# coding=utf-8

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


import string
import bisect


f_name = 'p022_names.txt'
letters = [l for l in string.ascii_uppercase]
nums = [n for n in xrange(1, len(letters)+1)]
alphabet = dict(zip(letters, nums))

def value(name):
  return sum(alphabet[c] for c in name)


def main():
  snames = ['DEREK', 'ZACK', 'ANTHONY', 'ANDREW', 'MIGUEL']
  # print names
  # names.sort()
  # print names
  names = []
  # for name in snames:
  #   bisect.insort(names, name)
  with open(f_name) as f:
    names = f.read()
    names = names.replace('"', '').split(",")
    names.sort()
    total = 0
    for i in xrange(0, len(names)):
      nvalue = value(names[i]) * (i + 1)
      total += nvalue
    print total

if __name__ == '__main__':
  main()