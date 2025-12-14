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
