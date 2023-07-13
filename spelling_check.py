#!/usr/bin/python3

def initial_solve(first, second):
  offset = 0
  diff_i = len(first) - 1
  for i in range(len(second)):
    if i + offset < len(first) and first[i + offset] != second[i]:
      offset += 1
      diff_i = i

  if offset > 1:
    print(0)
    exit()

  for i in range(diff_i, len(second)):
    if first[i + offset] != second[i]:
      print(0)
      exit()

  count = 0
  posns = []
  for i in range(diff_i, -1, -1):
    if first[i] == first[diff_i]:
      count += 1
      posns.append(i)
    else:
      break

  print(count)
  print(' '.join([str(p + 1) for p in reversed(posns)]))

def len_lcp(first, second):
  length = 0
  for i in range(len(second)):
    if first[i] == second[i]:
      length += 1
    else:
      break
  return length

def len_lcs(first, second):
  length = 0
  for i in range(len(first) - 1, 0, -1):
    if first[i] == second[i - 1]:
      length += 1
    else:
      break
  return length

def solve(first, second):
  lcp_len = len_lcp(first, second)
  lcs_len = len_lcs(first, second)

  # print(lcp_len, lcs_len, (lcp_len + 1) - (len(first) - lcs_len - 1))

  # size of the overlap between lcp + 1 and lcs - 1
  overlap = (lcp_len + 1) - (len(first) - lcs_len - 1)

  if overlap < 0:
    print(0)
    return
  
  print(overlap)
  print(' '.join([str(i + len(first) - lcs_len) for i in range(overlap)]))

if __name__ == '__main__':
  first = input()
  second = input()

  solve(first, second)