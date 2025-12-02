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

class Gomoku: # 1st arg n as board's size n by n, 2nd arg is not available yet
  # it's actually tic-tac-toe game but the goal is to get 5 consecutive pieces of yours either horizontally, vertically, or diagonally.
  def __init__(self, size = 9, st = "pvp"):
    self.size = size
    # the 1st turn is X: 1, next O: 0
    self.t = 1
    # 1 for pvp, 2 for pve
    self.type = 1 if st == "pvp" else 2
    self.board = [["_" for _ in range(self.size)] for i in range(self.size)]
  #

  def _input_(self):
    while True:
      s = input(f"\n\tLet {'X' if self.t else 'O'} at: ").strip()
      if s == "gg": return s
      for _ in s:
        if _ not in "0123456789 " or ' ' not in s:
          print(f"{'-'*5} Invalid input, please try again {'-'*5}")
          break
      else:
        if (False if int(s.split()[0]) >= self.size or int(s.split()[1]) >= self.size or self.board[int(s.split()[0])][int(s.split()[1])] != '_' else True): break
        else: print(f"{'-'*5} Invalid input, please try again {'-'*5}")
    print("")
    return [int(s.split()[0]), int(s.split()[1])]
  
  def _boardIsFull_(self):
    return True if len([1 for _ in range(self.size) for i in range(self.size) if self.board[_][i] == '_']) == 0 else False
  
  def _win_(self, ip):
    t = 'X' if self.t == 0 else 'O'
    for _ in range(-1, 2):
      for i in range(-1, 2):
        if (_, i) == (0, 0): continue
        c, ipC1, ipC2 = 0, ip.copy(), ip.copy()
        while ipC1[0] in [v for v in range(self.size)] and ipC1[1] in [v for v in range(self.size)] and self.board[ipC1[0]][ipC1[1]] == t: c, ipC1[0], ipC1[1] = c + 1, ipC1[0] + _, ipC1[1] + i
        while ipC2[0] in [v for v in range(self.size)] and ipC2[1] in [v for v in range(self.size)] and self.board[ipC2[0]][ipC2[1]] == t: c, ipC2[0], ipC2[1] = c + 1, ipC2[0] - _, ipC2[1] - i
        if c >= 6: return True
    return False

  def run(self):
    self.showBoard()
    i = self._input_()
    while i != 'gg':
      self.board[i[0]][i[1]], self.t = 'X' if self.t else 'O', (self.t + 1) % 2
      self.showBoard()
      if self._win_(i): break
      if self._boardIsFull_():
        print("\n Tie !!")
        return
      i = self._input_()
    print(f"\n{'X' if self.t == 0 else 'O'} Win!")

  def showBoard(self):
    b = self.board
    for _ in range(self.size): print(f"{"---|"+str(_) if _ == 0 else (int(_/10) if _%10 == 0 else "-")} ", end = ("" if _ != self.size - 1 else "\n"))
    for _ in range(self.size): print(f"{('O ' if self.t == 0 else 'X ') if _ == 0 else ''}{" |"+str(_) if _ == 0 else (_ if _ < 9 else _%10)} ", end = "")
    for _ in range(self.size): print(f"{("\n___|_") if _ == 0 else ("_" if _ != self.size - 1 else "_.")} ", end = "" if _ != self.size - 1 else "\n")
    for _ in range(self.size):
      print(f"{_} {' ' if _ <= 9 else ''}", end = "")
      for i in range(self.size):
        print(f"|{b[_][i]}", end = "")
      print("|")
 