# from collections import deque, ChainMap, Counter
# import functions
# from random import randint
# from itertools import permutations
# import matplotlib.pyplot as plt 
import math, statistics
# import sys
# import time
# import copy
# import heapq
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.cluster import KMeans

# 3d array [a][b][c] : a the depth, b rows and c columns


def convert(s, numRows): # Zigzag Conversion
  l = len(s)
  if numRows == 1 or l <= 1: return numRows
  c = math.ceil(len(s)/(numRows*2 - 2))*(numRows - 1)
  b = [['_' for _ in range(c)] for i in range(numRows)]
  r, c = 0, 0
  i = 1 # 1: downward insertion 0: diagonal insertion
  for _ in s:
    if r == numRows: i, r, c = 0, r - 2, c + 1
    if r == 0: i = 1
    if i:
      b[r][c] = _
      r += 1
    else:
      b[r][c] = _
      r -= 1
      c += 1

  for a in range(len(b)):
    for d in range(len(b[0])):
      print(f"{b[a][d]}|", end = "")
    print("")
  print("")

  result = ''
  for r in range(len(b)):
    for c in range(len(b[0])):
      if b[r][c] != '_':
        result += b[r][c]

  return result
print(convert("PAYPALISHIRING", 4))