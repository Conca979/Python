from collections import deque, ChainMap, Counter
import functions
from random import randint
# import matplotlib.pyplot as plt
import math
import copy

class Node:
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class BSTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, val, tree = 0):
    if tree == 0: # first default method call
      self.insert(val, self.root)
    elif not tree: # root is empty
      newNode = Node(val)
      self.root = newNode
    else:
      if tree.data < val and not tree.rChild:
        newNode = Node(val)
        tree.rChild = newNode
      elif tree.data < val and tree.rChild:
        self.insert(val, tree.rChild)
      elif tree.data > val and not tree.lChild:
        newNode = Node(val)
        tree.lChild = newNode
      else:
        self.insert(val, tree.lChild)

  def allNodes(self, order = 0):
    nodes = []
    def run(order, tree):
      if tree:
        if order == "desc":
          if tree.rChild: run(order, tree.rChild)
          nodes.append(tree.data)
          if tree.lChild: run(order, tree.lChild)
        elif order == "asc":
          if tree.lChild: run(order, tree.lChild)
          nodes.append(tree.data)
          if tree.rChild: run(order, tree.rChild)
        else:
          nodes.append(tree.data)
          if tree.lChild: run(order, tree.lChild)
          if tree.rChild: run(order, tree.rChild)
    run(order, self.root)
    return nodes


  def LOT(self, val, tree = 0, count = 1):
    if tree == 0:
      tree = self.root
      return self.LOT(val, tree, count)
    elif tree:
      if tree.data == val:
        return count - 1
      else:
        a, b = 0, 0
        if tree.rChild:
          a = self.LOT(val, tree.rChild, count+1)
        if tree.lChild:
          b = self.LOT(val, tree.lChild, count+1)
        return max(a, b)
    else: return count - 1

  def maxNode(self):
    temp, max = self.root, self.root.data
    while temp:
      max = temp.data if temp.data > max else max
      temp = temp.rChild
    return max
  
  def minNode(self):
    temp, min = self.root, self.root.data
    while temp:
      min = temp.data if temp.data < min else min
      temp = temp.lChild
    return min
  
  def maxLOT(self, tree = 0, level = 0):
    if tree == 0:
      tree = self.root
      return self.maxLOT(tree, level) - 1
    elif tree:
      a = self.maxLOT(tree.rChild, level + 1)
      b = self.maxLOT(tree.lChild, level + 1)
      # print(f"[Node: {a}| LOT: {b}]")
      return max(a, b)
    else: return level

  def listSortedTree(self):
    sortedList = []
    def nodes(tree):
      if tree:
        nodes(tree.lChild)
        sortedList.append(tree.data)
        nodes(tree.rChild)
    nodes(self.root)
    return sortedList
  
  def ValsInLevel(self, level):
    return [val for val in self.allNodes() if self.LOT(val) == level]

  
  def treeVisual(self):
    def post(val):
      return leftCount(val)*len(str(self.maxNode()))
    
    def leftCount( value):
      return len([val for val in self.listSortedTree() if val < value])
    
    for i in range(self.maxLOT()+1):
      spaces = post(max(self.ValsInLevel(i)))
      for s in range(spaces+1):
        found, val = 0, 0
        for _ in self.ValsInLevel(i):
          if s == post(_):
            found, val = 1, _
        print(f"{val}", end = "") if found else print(" ", end = "")
      print("")

  def findNode(self, val, tree = 0):
    if tree == 0:
      return self.findNode(val, self.root)
    elif tree:
      if tree.data == val:
        return tree
      else:
        a, b = None, None
        if tree.lChild: a = self.findNode(val, tree.lChild)
        if tree.rChild: b = self.findNode(val, tree.rChild)
        return a or b
    else: return tree

  def prt(self, val, tree = 0):
    if tree == 0: return self.prt(val, self.root)
    elif tree:
      if tree.lChild:
        if tree.lChild.data == val: return tree
      if tree.rChild:
        if tree.rChild.data == val: return tree
      return self.prt(val, tree.rChild) or self.prt(val, tree.lChild)
    else: return tree


  def delNode(self, val): #not complete yet
    nodeRemove = self.findNode(val)
    """if not found""" 
    if nodeRemove == None: return None
    # if leaf node
    if not nodeRemove.lChild and not nodeRemove.rChild:
      """if its root"""
      if self.maxLOT() == 0:
        self.root = None
        return
      else:
        prt = self.prt(val)
        if prt.rChild:
          if prt.rChild.data == val:
            prt.rChild = None
            return
        prt.lChild = None
        return
    # if has 1 or 2 child nodes
    if nodeRemove.lChild or nodeRemove.rChild:
      if nodeRemove.rChild: # right child preceded
        r, move = nodeRemove.rChild, 0
        print(f"right [{nodeRemove.data}|{r.data}]")
        while r.lChild and r.lChild.lChild: r, move = r.lChild, 1
        if move:
          nodeRemove.data = r.lChild.data
          r.lChild = r.lChild.rChild
        else:
          nodeRemove.data = r.data
          nodeRemove.rChild = r.rChild
      else:
        r, move = nodeRemove.lChild, 0
        print(f"left [{nodeRemove.data}|{r.data}]")
        while r.rChild and r.rChild.rChild: r, move = r.rChild, 1
        if move:
          nodeRemove.data = r.rChild.data
          r.rChild = r.rChild.lChild
        else:
          nodeRemove.data = r.data
          nodeRemove.lChild = r.lChild

tree = BSTree()
arr = [20, 10, 21, 6, 29, 1, 7, 28, 30, 9, 26, 8, 27]
arr = [20, 18, 21, 17, 22, 10, 30, 15, 25, 14, 26]
for _ in arr:
  tree.insert(_)
tree.treeVisual()
print("-----------------------------------------")

tree.delNode(22)
tree.treeVisual()

# a = tree.allNodes()
# for _ in range(len(a)):
#   r = randint(0, len(a)-1)
#   print(f"del {a[r]}")
#   tree.delNode(a[r])
#   tree.treeVisual()
#   del a[r]
#   print("-----------------------------------------")


# for _ in tree.allNodes():
#   print(f"[{_}|{tree.prt(_).data if tree.prt(_) else tree.prt(_)}]")