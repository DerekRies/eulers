"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

Find the maximum total from top to bottom of the triangle below:
"""

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


grid = []
small_grid = [[3], [7,4], [2,4,6], [8,5,9,3]]

for line in triangle.split("\n")[1:-1]:
  row = [int(n) for n in line.split(" ")]
  grid.append(row)
  # print row

# Solution will be found by collapsing rows upwards from the bottom
# Collapsing a row is achieved by adding the current number in the row
# with the greatest neighboring number from the row below
# ex:
#           3
#          7 4
#         2 4 6
#        8 5 9 3
# 
# 3rd row becomes: 10, 13, 15
# 2nd row becomes: 20, 19
# 1st row becomes 23
# No more rows, answer is 23

def collapse(row, prev_row):
  # Current row will have n-1 items where n = len(prev_row)
  n = len(prev_row)
  for i in xrange(len(row)):
    row[i] += max(prev_row[i], prev_row[i + 1])
  return row

# print collapse([2, 4, 6], [8, 5, 9, 3])

def collapse_grid(g):
  grid_size = len(g)
  for i in xrange(2, grid_size + 1):
    cur_row = g[grid_size - i]
    prev_row = g[grid_size - i + 1]
    g[grid_size - i] = collapse(cur_row, prev_row)
    g[grid_size - i + 1] = []
    # print g[grid_size - i]
  print g[0][0]


def main():
  collapse_grid(grid)

if __name__ == '__main__':
  main()