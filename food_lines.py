#!/usr/bin/python3

import collections
import heapq

def heap_solve(m, lines):
  heapq.heapify(lines)

  for i in range(m):
    print(lines[0])
    heapq.heapreplace(lines, lines[0] + 1)

def naive_solve(m, lines):
  for i in range(m):
    shortest = 0
    for j in range(len(lines)):
      if lines[j] < lines[shortest]:
        shortest = j
    print(lines[shortest])
    lines[shortest] += 1

if __name__ == '__main__':
  n, m = [int(i) for i in input().split()]
  lines = [int(i) for i in input().split()]

  heap_solve(m, lines)