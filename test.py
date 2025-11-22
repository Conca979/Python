from collections import deque, ChainMap, Counter
import functions
from random import randint
from itertools import permutations
# import matplotlib.pyplot as plt 
import math
import time
import copy
import heapq
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# 3d array [a][b][c] : a the deth, b rows and c columns

start = time.perf_counter()
x = np.array([[1],[2],[3],[4]])
y = np.array([2,4,6,8])
model = LinearRegression().fit(x,y)
print(model.predict([[5]]))
end = time.perf_counter()

print(f"Execution time: {end - start}s")