# coding=utf-8

from prob18 import collapse, collapse_grid


grid_file_name = 'p067_triangle.txt'
grid = []

with open(grid_file_name) as f:
  for line in f:
    list_line = [int(n) for n in line.replace("\n", "").split(" ")]
    grid.append(list_line)

def main():
  collapse_grid(grid)

if __name__ == '__main__':
  main()