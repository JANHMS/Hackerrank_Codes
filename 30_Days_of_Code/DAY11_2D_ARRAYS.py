import math
import os
import random
import re
import sys

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
x = []
for i in range(4):
    for j in range(4):
        u=sum(arr[i][j:j+3])
        m=(arr[i+1][j+1])
        l= sum(arr[i+2][j:j+3])
        x.append(u+m+l)
print(max(x))
