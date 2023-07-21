#!/usr/bin/python3

import re

class Node:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_candy(node):
  if not node.left and not node.right:
    return node.val

  return count_candy(node.left) + count_candy(node.right)

def walk_tree(node):
  if not node.left and not node.right:
    return 0

  return walk_tree(node.left) + walk_tree(node.right) + 4

def get_height(node):
  if not node.left and not node.right:
    return 0

  return max(get_height(node.left), get_height(node.right)) + 1

def solve(root):
  candy = count_candy(root)
  walks = walk_tree(root)
  height = get_height(root)
  print(walks - height, candy)

def read_tree(text):
  if text[0] == '(':
    left, pos = read_tree(text[1:-1])

if __name__ == '__main__':

  root = read_tree('((1 5) 8)')
  solve(root)

  # sample1 = Node(
  #   left=Node(
  #     left=Node(1),
  #     right=Node(5)
  #   ),
  #   right=Node(8)
  # )
  # print(solve(sample1))

  # sample2 = Node(
  #   left=Node(1),
  #   right=Node(3)
  # )
  # print(solve(sample2))

  # sample3 = Node(
  #   left=Node(
  #     left=Node(
  #       left=Node(72),
  #       right=Node(3)
  #     ),
  #     right=Node(
  #       left=Node(6),
  #       right=Node(
  #         left=Node(
  #           left=Node(
  #             left=Node(4),
  #             right=Node(9)
  #           ),
  #           right=Node(15)
  #         ),
  #         right=Node(2)
  #       )
  #     )
  #   ),
  #   right=Node(
  #     left=Node(7),
  #     right=Node(41)
  #   )
  # )
  # solve(sample3)
