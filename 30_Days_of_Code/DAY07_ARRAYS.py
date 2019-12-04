import math
import os
import random
import re
import sys
n = int(input())
arr = list(map(int, input().rstrip().split()))

j=''
for i in reversed(arr):
    j=j+' '+str(i)
print(j[1:])
