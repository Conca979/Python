# from collections import deque, ChainMap, Counter
# import functions
# from random import randint
# from itertools import permutations
# import matplotlib.pyplot as plt 
# import math, statistics
# import sys
# import time
# import copy
# import heapq
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.cluster import KMeans

# 3d array [a][b][c] : a the depth, b rows and c columns

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

def threeSum(nums):
  r = []
  l = len(nums)
  n = sorted(nums)

  def binarySearch(nums, target):
    # given nums sorted
    # return target's first index in nums else -1 if not found
    s = len(nums)
    l, r = 0, s - 1
    while l <= r:
      mid = (r + l) // 2
      if nums[mid] < target: l = mid + 1
      elif nums[mid] > target: r = mid - 1
      else: return mid
    
    return -1
  
  for a in range(l - 2):
    for i in range(a + 1, l - 1):
      t = -(n[a] + n[i])
      if binarySearch(n[(i + 1):], t) != -1:
        # print(f"{a}, {binarySearch(n[i + 1:], a)}")
        s = [n[a], n[i], t]
        if s not in r: r.append(s)

  return r

# print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
#              [-4,-1,-1,0,1,2]


def reverseKGroup(head, k):
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  t = ListNode()
  t.next = head
  tmp1 = t
  tmp2 = t

  for _ in range(k - 1):
    if not tmp2: return head
    else:
      tmp2 = tmp2.next

  a = tmp1.next
  b = a.next
  c = tmp2.next
  d = c.next

  tmp1.next = c
  tmp2.next = a
  a.next = d
  c.next = b

  return t.next

head = ListNode()
a = [1,2,3,4,5]
b = head
for _ in a:
  t = ListNode(_)
  b.next = t
  b = b.next
head = head.next

# head = reverseKGroup(head, 2)

# for _ in a:
#   print(head.val)
#   head = head.next

class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def minPathSum(b): # b = 2d board
  r, c = len(b), len(b[0])
  for _ in range(0, r):
    for i in range(0, c):
      if (_, i) == (0, 0): continue
      if i == 0 and _ != 0:
        b[_][i] = b[_][i] + b[_ - 1][i]
      elif i != 0 and _ == 0:
        b[_][i] = b[_][i] + b[_][i - 1]
      else:
        b[_][i] = b[_][i] + min(b[_ - 1][i], b[_][i - 1])
  return b[-1][-1]

def generate(numRows):
  b = [[0 for _ in range(numRows)] for _ in range(numRows)]
  for _ in range(numRows):
    for i in range(numRows):
      if not all([_, i]): b[_][i] = 1
      else:
        b[_][i] = b[_ - 1][i] + b[_][i - 1]
  
  r = []
  for _ in range(numRows):
    row = []
    for i in range(_ + 1):
      row.append(b[i][_ - i])
    r.append(row)

  return r


