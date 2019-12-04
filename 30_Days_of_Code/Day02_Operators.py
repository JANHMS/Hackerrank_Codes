import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    x= meal_cost*(tip_percent/100 + tax_percent/100 + 1)
    y = int(round(x))
    print(y)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
