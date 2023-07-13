#!/usr/bin/python3

import sys

if __name__ == '__main__':
  words = []
  words_set = set()

  for line in sys.stdin:
    word = line.strip()
    words.append(word)
    words_set.add(word.strip())

  compounds = []

  for word in words:
    for i in range(len(word)):
      prefix = word[:i + 1]
      suffix = word[i + 1:]
      if prefix in words_set and suffix in words_set:
        print(word)
        break

