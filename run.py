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

class TicTacToe:
  def __init__(self, s = 9, st = "pvp"):
    self.size = s
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
  
  def _win_(self, i):
    return

  def run(self):
    self.showBoard()
    i = self._input_()
    while i != 'gg':
      self.board[i[0]][i[1]], self.t = 'X' if self.t else 'O', (self.t + 1) % 2
      self.showBoard()
      # check if win
      i = self._input_()

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

game = TicTacToe(9)
game.run()