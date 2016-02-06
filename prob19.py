# coding=utf-8

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


import math


months = [31 for x in xrange(12)]
months[3] = 30
months[8] = 30
months[5] = 30
months[10] = 30
months[1] = 28

print months

def sundays_this_month(day, offset, month, year):
  first_sunday = day + sunday_offset
  
  weeks = math.floor(months[month] / 7)


def main():
  year = 1900
  cur_month = 0
  sunday_offset = 6
  cur_day = 1
  while year <= 2000:
    sundays_this_month
    if cur_month == 0:


if __name__ == '__main__':
  main()