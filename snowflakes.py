#!/usr/bin/python3

from collections import defaultdict

MAX_SNOWFLAKES = 1e6

def check_right(s1, s2, start):
  for i in range(len(s1)):
    if s1[i] != s2[(i + start) % len(s2)]:
      return False
  return True

def check_left(s1, s2, start):
  for i in range(len(s1)):
    if s1[i] != s2[len(s2) - 1 - i - start]:
      return False
  return True

def check_snowflakes(s1, s2):
  for i in range(len(s1)):
    if check_right(s1, s2, i) or check_left(s1, s2, i):
      return True
  return False

def solve():
  n = int(input())

  snowflakes = defaultdict(list)

  for _ in range(n):
    snowflake = [int(k) for k in input().split()]

    similar = snowflakes[sum(snowflake) % MAX_SNOWFLAKES]

    for i in range(len(similar)):
      if check_snowflakes(snowflake, similar[i]):
        print('Twin snowflakes found.')
        return

    similar.append(snowflake)

  print('No two snowflakes are alike.')
    
if __name__ == '__main__':
  solve()