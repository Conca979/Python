def isArmstrong(digits):
  return digits == sum([int(str(digits)[i])**int(len(str(digits))) for i in range(len(str(digits)))])

def romanToInt(roman):
  values = {'I':1, 'V':5, 'X': 10, 'L':50,'C':100, 'D':500, 'M':1000}
  total = 0
  for i in range(len(roman)):
    if i < len(roman) - 1:
      if values[roman[i]] < values[roman[i+1]]:
        total -= values[roman[i]]
      else:
        total += values[roman[i]]
    else:
      total += values[roman[i]]
  return total

def primesRange(limit):
  return [val for val in range(2, limit+1) if all(val%i for i in range(2, val))]

def braketMatching(str):
  class Node:
    def __init__(self, data=None):
      self.data = data
      self.next = None

  class Stack:
    def __init__(self):
      self.top = None
      self.size = 0

    def push(self, val):
      node = Node(val)
      if self.top:
        node.next = self.top
        self.top = node
      else:
        self.top = node
      self.size += 1

    def pop(self):
      if self.top:
        a, self.top = self.top.data, self.top.next
        self.size -= 1
        return a
      else: return None

  brakes = ['{', '(', '[', '}', ')' , ']']
  st = Stack()
  for ch in str:
    if ch in ['(', '[', '{']:
      st.push(ch)
    elif ch in [')', '}', ']']:
      if st.top:
        if ch != brakes[brakes.index(st.top.data)+3]:
          return False
        else: st.pop()
      else: return False
  return st.size == 0

def braketMatching2(str):
  st = []
  brackets = {')':'(', '}':'{', ']':'['}
  for ch in str:
    if ch in brackets.values():
      st.append(ch)
    elif ch in brackets.keys():
      if not st or st[-1] != brackets[ch]:
        return False
      else: st.pop()
  return not st # empty = True
  # check if the input string is correctly bracket-matched and nested

def dimonShape(size, s = "*"):
  if size % 2 == 0:
    print("Must be in odd size")
    return False
  mid = size//2
  for r in range(size):
    if r > mid: stars = 1 + (2*mid - r)*2
    else: stars = 1 + r*2
    sp = mid - stars//2
    print(" "*sp + s*stars)
# dimonShape(11)

def lengthOfLongestDistinctCharSubstring(s):
  l, m, c = len(s), 0, 0
  for _ in range(l):
    for i in range(_, l):
      if s[i] not in [s[j] for j in range(_, i)]:
        c = c + 1
        if c > m: m = c
      else:
        print(c)
        c = 0
        break
    c = 0
  return m

def addTwoNumbers(l1, l2):
  # l1 and l2: non-empty linked lists (ListNode class) representing two reversed non-negative integers.
  class ListNode():
    def __init__(self, val = 0, next = None):
      self.val = val
      self.next = next

  l, c = ListNode(), 0
  t = l
  while l1 and l2:
    a = l1.val + l2.val
    if c: a, c = a + 1, 0
    if a >= 10: a, c = a - 10, 1
    t.next = ListNode(a)
    l1, l2 = l1.next, l2.next
    t = t.next
  while l1:
    v = l1.val
    if c: v, c = v + 1, 0
    if v >= 10: v, c = v - 10, 1
    t.next, l1 = ListNode(v), l1.next
    t = t.next
  while l2:
    v = l2.val
    if c: v, c = v + 1, 0
    if v >= 10: v, c = v - 10, 1
    t.next, l2 = ListNode(v), l2.next
    t = t.next
  if c: t.next = ListNode(1)
  return l.next

def myAtoi(s):
  # Trim spaces, read optional sign,
  # accumulate digits, clamp to int32.
  if len(s) == 0: return 0
  s, p, sm = s.lstrip(), 0, 0
  mx, mn = 2147483647, -2147483648
  if s[0] == '-': s, p = s[1:], 0
  elif s[0] == '+': s, p = s[1:], 1
  else: p = 1
  for _ in s:
    if _ in '0123456789': sm = sm*10 + int(_)
    else: break
  if p: return (sm if sm <= mx else mx)
  else: return (-sm if -sm > mn else mn)

def threeSum(nums): # this function bad in performance
  # nums: array of nums
  nums, l = sorted(nums), len(nums)
  #
  return list(set(map(tuple,([[nums[a], nums[b], nums[c]] for a in range(l-2) for b in range(a+1, l-1) for c in range(b+1, l) if (nums[a] + nums[b] + nums[c]) == 0]))))

def searchRange(nums, target): # wrong!!
  # Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
  # If target is not found in the array, return [-1, -1].
  # You must write an algorithm with O(log n) runtime complexity.
  l, t, n = len(nums), target, nums
  if t not in n: return [-1, -1] #!!
  lf, r = 0, l - 1
  while lf < r:
    m = (lf + r)//2
    if n[m] < t: lf = m + 1
    elif n[m] > t: r = m - 1
    else: 
      if m < 0 or m >= l: return [-1, -1]
      else: lf, r = m, m
      while lf > 0 and n[lf - 1] == t: lf = lf - 1
      while r < l - 1 and n[r + 1] == t: r = r + 1
      break
  return [lf, r]

#---------------

def isValidSudoku(board):
  def subBox(b, r, c):
    r2, c2 = int(r/3)*3, int(c/3)*3
    return [b[_][i] for _ in range(r2, r2+3) for i in range(c2, c2 + 3) if [_, i] != [r, c] and b[_][i] != "."]

  b = board
  for _ in range(9):
    for i in range(9):
      if b[_][i] != ".":
        t = [b[a][i] for a in range(9) if b[a][i] != "." and a != _] + [b[_][a] for a in range(9) if b[_][a] != "." and a != i] + subBox(b, _, i)
        if b[_][i] in t: return False
  return True

def solveSudoku(b): # b: board[row][column]
  """Do not return anything, modify board in-place instead"""
  def __subBox__(b, r, c):
    r2, c2 = int(r/3)*3, int(c/3)*3
    return [b[_][i] for _ in range(r2, r2+3) for i in range(c2, c2 + 3) if [_, i] != [r, c] and b[_][i] != "."]
  
  def _isValidPosition_(b, r, c, val):
    t = [b[r][a] for a in range(9) if b[r][a] != "." and a != c] + [b[a][c] for a in range(9) if b[a][c] != "." and a != r] + __subBox__(b, r, c)
    return True if val not in t else False
  
  def _validity_(b, r, c):
    t = [b[r][a] for a in range(9) if b[r][a] != "." and a != c] + [b[a][c] for a in range(9) if b[a][c] != "." and a != r] + __subBox__(b, r, c)
    return [_ for _ in "123456789" if _ not in t]
  
  def _emptyGrid_(b):
    return sorted({f"{_}{i}":len(_validity_(b, _, i)) for _ in range(9) for i in range(9) if b[_][i] == "."}.items(), key = lambda _: _[1])

  def _solveSudoku2_(b): # using Minimum Remaining Values (MRV)
    g = _emptyGrid_(b)
    if len(g): # if ∃ empty grid
      g = [int(g[0][0][0]), int(g[0][0][1])]
      for _ in _validity_(b, g[0], g[1]):
        if _isValidPosition_(b, g[0], g[1], _):
          b[g[0]][g[1]] = _
          if _solveSudoku2_(b): return True
          else: b[g[0]][g[1]] = "."
      else: return False
    else: return True

  def _solveSudoku_(b, r, c): # raw backtracking
    if c == 9: r, c = r + 1, 0
    if r == 9: return True
    #
    if b[r][c] != ".":
      return _solveSudoku_(b, r, c + 1)
    else: # empty grid
      for _ in _validity_(b, r, c):
        if _isValidPosition_(b, r, c, _):
          b[r][c] = _
          if _solveSudoku_(b, r, c + 1): return True
          else: b[r][c] = "."
      else: return False

  _solveSudoku2_(b)

def showBoard(b): # board[n][n]
  print("\n  ", end = "")
  for _ in range(len(b)): print(f" {_}", end = "")
  print("\n")
  for _ in range(len(b)):
    print(f"{_} ", end = "")
    for i in range(len(b)):
      print(f"|{b[_][i] if b[_][i] in "123456789" else "_"}", end = "")
    print("")

#--------------------

def reverse(x):
  # the mathematical identity requires: a = (a // b)*b + r
  # Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
  mx, mn, rv, p = 2147483647, -2147483648, 0, 0
  #
  p = 0 if x < 0 else 1
  for _ in str(x)[::-1] if p else str(x)[1:][::-1]:
    if p:
      if int(mx/10) < rv: return 0
      elif int(mx/10) == rv:
        if mx%10 < int(_): return 0
        else: rv = rv*10 + int(_)
      else: rv = rv*10 + int(_)
    else:
      if int(mn/10) > rv: return 0
      elif int(mn/10) == rv:
        if mn%10 < int(_): return 0
        else: rv = rv*10 - int(_)
      else: rv = rv*10 - int(_)
  return rv

def longestPalindrome(s):
  # s: string
  m, c, ln = 0, 1, len(s)
  #
  if ln == 1: return s
  if ln == 2: return (s[0] if s[0] != s[1] else s)
  #
  rs = ""
  for _ in range(1, ln):
    l, r = _ - 1, _ + 1
    if r >= ln: break
    while True:
      if s[l] == s[r]:
        c = c + 2
        if c > m: m, rs = c, s[l:r + 1]
        if l >= 1 and r < ln - 1: l, r = l - 1, r + 1
        else:
          c = 0
          break
      else:
        if c > m: m, rs = c, s[l + 1:r]
        c = 0
        break
  for _ in range(ln):
    l, r = _, _ + 1
    if r >= ln: break
    while True:
      if s[l] == s[r]:
        c = c + 2
        if c > m: m, rs = c, s[l:r + 1]
        if l >= 1 and r < ln - 1: l, r = l - 1, r + 1
        else:
          c = 0
          break
      else:
        if c > m: m, rs = c, s[l + 1:r]
        c = 0
        break
  return rs

def countNonAdjacentBookArrangements(Books):
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

  c, f = [0], 1
  #
  if max(Books.values()) > sum(Books.values()) + 1: 
    print("No such valid placement!")
    return
  #
  for _ in Books.keys():
    b(Books.copy(), _, c)
    if (Books[_] > 0):
      f = f * math.factorial(Books[_])
  # books within the same subject are distinct so must muliply with f
  return c[0]*f

  # to run this code:
  # pass in a list of (subject:books)
  # run print(countNonAdjacentBookdArrangements(Books))""")

class SortBy():
  def b(self, arr): # bubble sort
    for _ in range(len(arr)-1):
      for i in range(len(arr)-1-_):
        if arr[i] > arr[i+1]: arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
  
  def i(self, arr): # insertion sort
    for _ in range(1, len(arr)):
      for i in range(_):
        if arr[i] > arr[i-1]: arr[i], arr[i-1] = arr[i-1], arr[i]
        else: break
    return arr
  
  def s(self, arr): # selection sort
    for _ in range(len(arr)):
      t = _
      for i in range(_, len(arr)):
        if arr[i] < arr[t]: t = i
      arr[_], arr[t] = arr[t], arr[_]
    return arr
  
  # def s(self, arr): # quick sort

def stackImplementation():
  print(r"""class Node:"
  def __init__(self, data=None):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, val):
    node = Node(val)
    if self.top:
      node.next = self.top
      self.top = node
    else:
      self.top = node
    self.size += 1

  def pop(self):
    if self.top:
      a, self.top = self.top.data, self.top.next
      self.size -= 1
      return a
    else: return None

  def printStack(st):
    if st.top:
      print(st.top.data)
      st.top = st.top.next
      return printStack(st)""")
  
def queueImplementation():
  print(r"""class Queue:
  def __init__(self):
    self.InBound_st = []
    self.OutBound_st = []

  def enQueue(self, val):
    self.InBound_st.append(val)
  
  def deQueue(self):
    if not self.OutBound_st:
      while self.InBound_st:
        self.OutBound_st.append(self.InBound_st.pop())
    return self.OutBound_st.pop()

  def printQueue(self):
    print("top")
    for val in self.OutBound_st[::-1]:
      print("[{}]".format(val))
    for val in self.InBound_st[::]:
      print("[{}]".format(val))""")
  
def queueDoubleLinkedList():
  print(r"""class Node:
  def __init__(self, val, next = None, prv = None):
    self.data = val
    self.next = next
    self.prv = prv

class Queue:
  def __init__(self):
    self.top = None
    self.tail = None
    self.count = 0

  def enQueue(self, val):
    newNode = Node(val)
    if not self.tail: # if empty
      self.top = newNode
      self.tail = newNode
    else:
      newNode.next = self.tail
      self.tail.prv = newNode
      self.tail = newNode
    self.count += 1

  def deQueue(self):
    if self.top:
      self.top, a = self.top.prv, self.top.data
      self.count -= 1
      return a
    else: return None

  def printQueue(self):
    print("Top")
    temp = self.top
    while temp:
      print("[{}]".format(temp.data))
      temp = temp.prv""")
  
def BSTreeImplementation():
  print(r'''class Node:
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class BSTree:
  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, val):
    if not self.root: # empty tree
      self.root = Node(val)
    else: self._insert(val, self.root)

  def _insert(self, val, node):
    if node.data < val:
      if node.rChild: self._insert(val, node.rChild)
      else: node.rChild, self.size = Node(val), self.size + 1
    else:
      if node.lChild: self._insert(val, node.lChild)
      else: node.lChild, self.size = Node(val), self.size + 1

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


  def LOT(self, val):
    if not self.findNode(val): return None
    else: return self._LOT(val, self.root, 0)

  def _LOT(self, val, node, c):
    if node.data == val: return c
    elif val < node.data: return self._LOT(val, node.lChild, c + 1)
    else: return self._LOT(val, node.rChild, c + 1)

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

  def findNode(self, val):
    if not self.root: return None
    else: return self._findNode(val, self.root)

  def _findNode(self, val, node):
    if node is None: return None
    elif node.data == val: return node
    elif val < node.data: return self._findNode(val, node.lChild)
    else: return self._findNode(val, node.rChild)

  def _prt(self, val):
    if not self.root: return None
    else:
      if not self.findNode(val) or self.LOT(val) == 0: return None
      else: return self.__prt(val, self.root)

  def __prt(self, val, node):
    if node.data > val: 
      if node.lChild.data == val: return node
      else: return self.__prt(val, node.lChild)
    else:
      if node.rChild.data == val: return node
      else: return self.__prt(val, node.rChild)

  def delRandNodes(self):
    self.treeVisual()
    a = self.allNodes()
    for _ in range(len(a)):
      print("-----------------------------------------")
      r = randint(0, len(a)-1)
      print(f"del {a[r]}")
      self.delNode(a[r])
      self.treeVisual()
      del a[r]

  def deBugging(self):
    print("Node\trChild\tlChild\tprt\tLOT")
    print("-----------------------------------")
    for _ in self.allNodes():
      n, p = self.findNode(_), self._prt(_)
      print(f"{n.data}\t{n.lChild.data if n.lChild else None}\t{n.rChild.data if n.rChild else None}\t{p.data if p else None}\t{self.LOT(_)}")

  def delNode(self, val):
    removeN = self.findNode(val)
    if removeN == None: return None
    # if leaf node
    if not removeN.lChild and not removeN.rChild:
      if self.maxLOT() == 0:
        self.root = None
        return
      else:
        prt = self._prt(val)
        if prt.rChild:
          if prt.rChild.data == val:
            prt.rChild = None
            return
        prt.lChild = None
        return
    # if has 1 or 2 child nodes
    if removeN.lChild or removeN.rChild:
      if removeN.rChild: # right child preceded
        r = removeN.rChild
        # print(f"right [{removeN.data}|{r.data}]")
        if r.lChild:
          while r.lChild.lChild: r = r.lChild
          removeN.data = r.lChild.data
          r.lChild = r.lChild.rChild
        else:
          removeN.data = r.data
          removeN.rChild = r.rChild
      else:
        r = removeN.lChild
        # print(f"left [{removeN.data}|{r.data}]")
        if r.rChild:
          while r.rChild.rChild: r = r.rChild
          removeN.data = r.rChild.data
          r.rChild = r.rChild.lChild
        else:
          removeN.data = r.data
          removeN.lChild = r.lChild

tree = BSTree()
arr = [20, 10, 21, 6, 29, 1, 7, 28, 30, 9, 26, 8, 27]
for _ in arr:
  tree.insert(_)''')
