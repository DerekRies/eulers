# coding=utf-8
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

words = {
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine',
  '10': 'ten',
  '11': 'eleven',
  '12': 'twelve',
  '13': 'thirteen',
  '14': 'fourteen',
  '15': 'fifteen',
  '16': 'sixteen',
  '17': 'seventeen',
  '18': 'eighteen',
  '19': 'nineteen',
  '20': 'twenty',
  '30': 'thirty',
  '40': 'fourty',
  '50': 'fifty',
  '60': 'sixty',
  '70': 'seventy',
  '80': 'eighty',
  '90': 'ninety',
}

def englishify(n):
  word = ''
  while n > 0:
    str_n = str(n)
    if n >= 1000:
      word += words.get(str_n[0])
      word += ' thousand '
      str_n = str_n[1:]
    elif n >= 100:
      word += words.get(str_n[0])
      word += ' hundred '
      str_n = str_n[1:]
    elif n >= 20:
      if len(word) > 0:
        word += ' and '
      word += words.get(str_n[0] + '0')
      if(n % 10 != 0):
        word += ' ' + words.get(str_n[1])
      str_n = ''
    else:
      if len(word) > 0:
        word += ' and '
      word += words.get(str_n)
      str_n = ''
    try:
      n = int(str_n)
    except:
      n = 0
  return word


def count(word):
  w = word.replace(' ', '')
  print w
  return len(w)

def log(n):
  w = englishify(n)
  c = count(w)
  print '%s: %s (%s letters)' % (n, w, c)


letter_count = 0
for n in xrange(1,1001):
  w = englishify(n).replace(' ', '')
  letter_count += len(w)
print letter_count


# log(342)
# log(115)
