import math
import os
import random
import re
import sys

n = int(input().strip())
numbers = str(bin(n)[2:]).split('0')
lenght= [len(num) for num in numbers]
print(max(lenght))
