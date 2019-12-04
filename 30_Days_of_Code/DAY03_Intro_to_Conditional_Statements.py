import math
import os
import random
import re
import sys
N = int(input())
if N%2 == 1 or (N > 5 and N < 21):
    print("Weird")
else:
    print("Not Weird")
