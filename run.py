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

def sortColors(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  l = len(nums)
  if l == 1: return
  elif l == 2:
    if nums[0] > nums[1]:
      nums[0], nums[1] = nums[1], nums[0]
    else: return
  #
  def _swap_(i1, i2):
    nums[i1], nums[i2] = nums[i2], nums[i1]
  #
  for _ in range(l - 2):
    if nums[_] > nums[_ + 1]: _swap_(_, _ + 1)
    if nums[_ + 1] > nums[_ + 2]: _swap_(_ + 1, _ + 2)
    if nums[_] > nums[_ + 1]: _swap_(_, _ + 1)

def moveZeroes(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
  def _swap_(i1, i2):
    nums[i1], nums[i2] = nums[i2], nums[i1]

  l = len(nums)
  # for i in range(l):
  #   a = i
  #   if nums[i] == 0:
  #     while a != l:
  #       if nums[a] != 0: # first non-zero element encounterd
  #         _swap_(i, a)
  #         break
  #       a += 1
  #     else: return

  c = 0 # number of 0s
  index = 0
  while index < l:
    print(c, index)
    a = 0
    if nums[index] == 0: c += 1
    else:
      for i in range(c):
        if (index + i) == l: return
        _swap_(index + i, index - c + i)
        a += 1
      index += a
      continue
    index += + 1

# nums = [0,1,0,3,12,0,4]
# # nums = [1,0]
# moveZeroes(nums)
# print(nums)


def threeSum(nums):
  n = sorted(nums)
  
  r = []
  l = len(n)
  for i in range(l - 2):
    if i > 0:
      if nums[i] != nums[i - 1]: 
        j = i + 1
        k = l - 1
        while j < k:
          s = n[i] + n[j] + n[k]
          if s == 0:
            r.append([n[i], n[j], n[k]])
            j, k = j + 1, k - 1
          elif s < 0: j += 1
          else: k -= 1
  
  return r

