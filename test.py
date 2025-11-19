from collections import deque, ChainMap, Counter
import functions
from random import randint
from itertools import permutations
# import matplotlib.pyplot as plt
import math
import copy
import heapq

def b(Books, curB, c):
  if Books[curB] >= 1:
    Books[curB] = Books[curB] - 1
    #
    if not any(Books.values()): # all books are placed
      c[0] = c[0] + 1
      return
    #
    for i in [_ for _ in Books.keys() if _ != curB]:
        b(Books.copy(), i, c)

def run(bio, maths, his):
  Books = {"B": bio, "M": maths, "H": his}
  c, f = [0], 1
  #
  if max([bio, maths, his]) > sum([bio, maths, his]) + 1: 
    print("No such valid placement!")
    return
  #
  for _ in Books.keys():
    b(Books.copy(), _, c)
    if (Books[_] > 0):
      f = f * math.factorial(Books[_])
  # because all books are distinct so must muliply with f
  return c[0]*f

print(run(4,3,2))


# from collections import deque, ChainMap, Counter
# import functions
# from random import randint
# from itertools import permutations
# # import matplotlib.pyplot as plt
# import math
# import copy
# import heapq

# def b(Books, curB, c, lv):
#   if Books[curB] >= 1:
#     Books[curB] = Books[curB] - 1
#     print("------")
#     #
#     if not any(Books.values()): # all books are placed
#       print("leaf")
#       c[0] = c[0] + 1
#       return
#     #
#     for i in [_ for _ in Books.keys() if _ != curB]:
#         print(curB+str(lv), i)
#         b(Books.copy(), i, c, lv + 1)

# def run(bio, maths, his):
#   Books = {"B": bio, "M": maths, "H": his}
#   c, f = [0], 1
#   #
#   if max([bio, maths, his]) > sum([bio, maths, his]) + 1: 
#     print("No such valid placement!")
#     return
#   #
#   for _ in Books.keys():
#     b(Books.copy(), _, c, 1)
#     if (Books[_] > 0):
#       f = f * math.factorial(Books[_])
#   # because all books are distinct so must muliply with f
#   return c[0]*f

# print(run(4,3,2))